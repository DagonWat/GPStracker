module Api
  class TrackerController < ApplicationController
    skip_before_action :verify_authenticity_token
    skip_before_action :require_login

    def create
      if params[:latitude].abs < 90 && params[:longitude].abs < 90
        if User.where(tracker_token: params[:token]).any?
          @tracker = Tracker.new(lat: params[:latitude], lon: params[:longitude], user_id: User.where(tracker_token: params[:token])[0].id)
  		    @tracker.save
        end
		 	  render json: {status: "success"}
      end
	  end

  end
end
