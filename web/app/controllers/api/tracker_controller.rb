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

    def change_name
      respond_to do |format|
        format.html
        format.json
      end
    end


  end
end
