class CalendarController < ApplicationController
  before_action :require_login
  before_action :check_user

  def index
    @calendar_service = CalendarService.new(current_user, params[:date])
  end

  protected

  def check_user
    redirect_to admin_dashboard_url if current_user.admin
  end
end
