class DashboardController < ApplicationController
  skip_before_action :verify_authenticity_token

  def index
    @trackers = Tracker.order(:created_at)
  end

end
