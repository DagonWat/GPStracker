class CalendarController < ApplicationController
  before_action :require_login
  before_action :check_user

  def index
    if params[:id] && User.where(id: params[:id]).length > 0 && params[:id].to_i.in?(current_user.friends)
      @calendar_service = CalendarService.new(User.where(id: params[:id])[0], params[:date])
    else
      @calendar_service = CalendarService.new(current_user, params[:date])
    end
  end

  protected

  def check_user
    redirect_to admin_dashboard_url if current_user.admin
  end
end
