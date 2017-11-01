module Api
  class TrackerController < ApplicationController
    skip_before_action :verify_authenticity_token

    def create
      if params[:latitude].abs < 90 && params[:longitude].abs < 90
        @tracker = Tracker.new(lat: params[:latitude], lon: params[:longitude])
		    @tracker.save

		 	  render json: {status: "success"}
      end
	  end

  end
end
