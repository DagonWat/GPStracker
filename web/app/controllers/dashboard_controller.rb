class DashboardController < ApplicationController
  skip_before_action :verify_authenticity_token
  skip_before_action :require_login

  def index
    @trackers = Tracker.order(:created_at)

    @from = Time.now.strftime("%Y-%m-%d 00:00:00")

    @until = Time.now.strftime("%Y-%m-%d 23:59:59")

    @today = Tracker.where("created_at >= :start_date AND created_at <= :end_date",
      {start_date: @from, end_date: @until})

    @anyuser = true

    if :require_login
      @anyuser = false
    end

  end

  def show
    @from = Tracker.find(params[:id]).created_at.strftime("%Y-%m-%d 00:00:00")

    @until = Tracker.find(params[:id]).created_at.strftime("%Y-%m-%d 23:59:59")

    @trackers = Tracker.order(:created_at)

    @paths = []
    current_path = []

    Tracker.order(:created_at).where("created_at >= :start_date AND created_at <= :end_date", {start_date: @from, end_date: @until}).each do |tracker|
      if current_path.empty?
        current_path << tracker
        next
      end

      if current_path.last.created_at + 15.minutes < tracker.created_at
        @paths << current_path
        current_path = [tracker]
      else
        current_path << tracker
      end
    end

    @paths << current_path if current_path.any?
  end

end
