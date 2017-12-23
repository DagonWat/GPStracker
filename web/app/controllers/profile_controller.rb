class ProfileController < ApplicationController
  before_action :require_login
  before_action :check_user

  def edit
    @trackers = Tracker.order(:created_at)
  end

  def update
    @trackers = Tracker.order(:created_at)

    if current_user.update(user_params)
      if !params[:user][:password].blank?
        redirect_to admin_dashboard_url, notice: "Password for #{current_user.email} was successfully updated."
        current_user.update(image: params[:image])
      else
        redirect_to admin_dashboard_url, notice: "Image for #{current_user.email} was successfully changed."
        current_user.update(image: params[:image])
      end
    else
      render :edit
    end
  end

  def generate_token
    current_user.update(tracker_token: SecureRandom.hex(4))
    redirect_to root_url
  end

  protected

  def user_params
    params.require(:user).permit(:password, :password_confirmation)
  end

  def check_user
    redirect_to admin_dashboard_url if current_user.admin
  end
end
