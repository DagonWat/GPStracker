class ProfileController < ApplicationController
  before_action :require_login

  def index
    @trackers = Tracker.order(:created_at)

    @from = Time.now.strftime('%Y-%m-%d 00:00:00')
    @until = Time.now.strftime('%Y-%m-%d 23:59:59')

    @today = Tracker.where('created_at >= :start_date AND created_at <= :end_date',
      {start_date: @from, end_date: @until})
  end

  def edit
    @trackers = Tracker.order(:created_at)
  end

  def update
    @trackers = Tracker.order(:created_at)

    if current_user.update(user_params) && !params[:user][:password].blank?
      redirect_to admin_dashboard_path, notice: 'Password for ' + current_user.email + ' was successfully updated.'
    else
      render :edit
    end
  end

  private
    def user_params
      params.require(:user).permit(:email, :password, :password_confirmation)
    end

end
