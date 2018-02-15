module Api
  class TrackerController < ApplicationController
    skip_before_action :verify_authenticity_token
    skip_before_action :require_login

    def create
      user = User.where(tracker_token: params[:token])[0]

      if params[:latitude].abs < 90 && params[:longitude].abs < 90 && user
        @tracker = Tracker.new(lat: params[:latitude], lon: params[:longitude], user_id: user.id, group: -1)
		    @tracker.save
		 	  render json: {status: "success"}
      end
  	end

    def change_group
      @from = Tracker.find(params[:id]).created_at.beginning_of_day
      @until = Tracker.find(params[:id]).created_at.end_of_day

      tracks = ((params[:id] && (current_user.friends.include? params[:id].to_i)) ? User.where(id: params[:id])[0] : current_user).trackers.order(:created_at)

      @paths = tracks.where('created_at BETWEEN ? AND ?', @from, @until)
      @i = Tracker.find(params[:id]).group
      @tracker = Tracker.find(params[:id])
      tracks.update_all(custom_name: params[:group_name])
    end
  end
end
