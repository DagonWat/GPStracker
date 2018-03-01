class CalendarController < ApplicationController
  before_action :require_login

  def index
    if params[:id].present? && current_user.friends.include?(params[:id].to_i)
      @calendar_service = CalendarService.new(User.find(params[:id]), params[:date])
    else
      @calendar_service = CalendarService.new(current_user, params[:date])
    end
  end
end
