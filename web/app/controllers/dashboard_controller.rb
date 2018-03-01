class DashboardController < ApplicationController
  skip_before_action :verify_authenticity_token
  before_action :require_login

  def show
    if params[:date].present?
      date = Time.zone.parse(params[:date])

      @from = date.beginning_of_day
      @until = date.end_of_day

      tracks = ((params[:id] && (current_user.friends.include? params[:id].to_i)) ? User.where(id: params[:id])[0] : current_user).trackers.order(:created_at)
      p 1111111111
      p 1111111111
      p tracks.last.id
      @paths = tracks.where('created_at BETWEEN ? AND ?', @from, @until)
      p @paths.last.id
    else
      @trackers = Tracker.where(user_id: current_user.id).order(:created_at)

      @from = Time.now.strftime('%Y-%m-%d 00:00:00')
      @until = Time.now.strftime('%Y-%m-%d 23:59:59')

      @today = Tracker.where(user_id: current_user.id).where('created_at >= :start_date AND created_at <= :end_date',
                                                                       {start_date: @from, end_date: @until})
    end
  end
end
