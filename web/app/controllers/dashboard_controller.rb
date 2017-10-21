class DashboardController < ApplicationController
  skip_before_action :verify_authenticity_token

  def index
    @trackers = Tracker.order(:created_at)

    @from = Time.now.strftime("%Y-%m-%d 00:00:00")

    @until = Time.now.strftime("%Y-%m-%d 23:59:59")
    
    @today = Tracker.where("created_at >= :start_date AND created_at <= :end_date",
      {start_date: @from, end_date: @until})
  end

  def show
    @from = Tracker.find(params[:id]).created_at.strftime("%Y-%m-%d 00:00:00")

    @until = Tracker.find(params[:id]).created_at.strftime("%Y-%m-%d 23:59:59")

    @trackers = Tracker.order(:created_at)

    @path = Tracker.where("created_at >= :start_date AND created_at <= :end_date",
      {start_date: @from, end_date: @until})
  end

end
