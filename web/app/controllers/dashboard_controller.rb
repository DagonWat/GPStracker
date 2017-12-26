class DashboardController < ApplicationController
  skip_before_action :verify_authenticity_token
  before_action :require_login

  def show
    if params[:date].present?
      date = Time.zone.parse(params[:date])

      @from = date.beginning_of_day
      @until = date.end_of_day

      @paths = []
      current_path = []

      # checking if user trying to get his tracks or friends one
      ((params[:id] && (current_user.friends.include? params[:id].to_i)) ? User.where(id: params[:id])[0] : current_user).trackers.order(:created_at).where('created_at BETWEEN ? AND ?', @from, @until).each do |tracker|
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
    else
      @trackers = Tracker.where(user_id: current_user.id).order(:created_at)

      @from = Time.now.strftime('%Y-%m-%d 00:00:00')
      @until = Time.now.strftime('%Y-%m-%d 23:59:59')

      @today = Tracker.where(user_id: current_user.id).where('created_at >= :start_date AND created_at <= :end_date',
                                                                       {start_date: @from, end_date: @until})
    end
  end
end
