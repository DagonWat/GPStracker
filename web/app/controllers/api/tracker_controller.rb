module Api
  class TrackerController < ApplicationController
    skip_before_action :verify_authenticity_token

    def index
      @trackers = Tracker.all
    end

    def create
      if params[:latitude] > 0 and params[:longitude] > 0
        @tracker = Tracker.new(lat: params[:latitude], lon: params[:longitude])
		    @tracker.save

		 	  render json: {status: "success"}
      end
	  end

  end
end
