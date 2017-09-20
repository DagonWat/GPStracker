class TrackerController < ApplicationController
    skip_before_action :verify_authenticity_token

    def create
        @tracker = Tracker.new(params[:latitude], params[:longitude])

        @tracker.save
        redirect_to @tracker

        p params[:latitude]
        render json: {status: "success"}
    end
end
