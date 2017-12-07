class ProfileController < ApplicationController
  before_action :require_login
  before_action :set_user, only: [:show, :index]

  def show
  end

  def index
    @from = Time.now.strftime('%Y-%m-%d 00:00:00')

    @until = Time.now.strftime('%Y-%m-%d 23:59:59')

    @today = Tracker.where('created_at >= :start_date AND created_at <= :end_date',
      {start_date: @from, end_date: @until})
  end

  private
    def set_user
      @user = current_user
      @trackers = Tracker.order(:created_at)
    end
end
