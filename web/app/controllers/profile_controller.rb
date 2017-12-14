class ProfileController < ApplicationController
  before_action :require_login

  def edit
    @trackers = Tracker.order(:created_at)
  end

  def update
    @trackers = Tracker.order(:created_at)

    if current_user.update(user_params) && !params[:user][:password].blank?
      redirect_to admin_dashboard_url, notice: "Password for #{current_user.email} was successfully updated."
    else
      render :edit
    end
  end

  protected

  def user_params
    params.require(:user).permit(:password, :password_confirmation)
  end

end
