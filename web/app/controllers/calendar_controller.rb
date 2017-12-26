class CalendarController < ApplicationController
  before_action :require_login

  def index
    user = User.find(params[:id])

    if user && current_user.friends.include?(params[:id].to_i)
      @calendar_service = CalendarService.new(user, params[:date])
    else
      @calendar_service = CalendarService.new(current_user, params[:date])
    end
  end
end
