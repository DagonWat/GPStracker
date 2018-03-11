module Api
  class TrackerController < ApplicationController
    skip_before_action :verify_authenticity_token
    skip_before_action :require_login
    skip_before_action :check_if_admin

    def create
      user = User.where(tracker_token: params[:token])[0]
      if params[:latitude].to_f.abs < 90 && params[:longitude].to_f.abs < 90 && user
        @tracker = Tracker.new(lat: params[:latitude].to_f, lon: params[:longitude].to_f, user_id: user.id, group: -1)
        @tracker.save
        p user.trackers.last(2)[0]
        distance_service = DistanceService.new(user.trackers.last(2)[0], user.trackers.last(2)[1])
        new_coords = distance_service.make_good()
        @tracker.update(lat: new_coords.first, lon: new_coords.second)

		 	  render json: {status: 'success'}
      end
  	end

    def change_group
      @from = Tracker.find(params[:id]).created_at.beginning_of_day
      @until = Tracker.find(params[:id]).created_at.end_of_day

      tracks = ((params[:id] && (current_user.friends.include? params[:id].to_i)) ? User.where(id: params[:id])[0] : current_user).trackers.order(:created_at)

      @paths = tracks.where('created_at BETWEEN ? AND ?', @from, @until)
      @i = Tracker.find(params[:id]).group
      @tracker = Tracker.find(params[:id])
      tracks_to_change = @paths.where(group: @tracker.group)
      tracks_to_change.update_all(custom_name: params[:group_name])
    end
  end
end
