class TrackerController < ApplicationController
  skip_before_action :verify_authenticity_token

	def create

    if params[:latitude] > 0 and params[:longitude] > 0
      @tracker = Tracker.new(lat: params[:latitude], lon: params[:longitude])

			@tracker.save

			p params[:latitude]
			render json: {status: "success"}
		end
	end
end
