class ProfileController < ApplicationController
  before_action :require_login

  def edit
    @trackers = Tracker.order(:created_at)
  end

  def update
    @trackers = Tracker.order(:created_at)

    if current_user.update(user_params)
      if params[:user][:password].present?
        redirect_to admin_dashboard_url, notice: "Password for #{current_user.email} was successfully updated."
      end
    else
      render :edit
    end
  end

  def generate_token
    current_user.update(tracker_token: SecureRandom.hex(4))
    redirect_to root_url
  end

  def generate_avatar
    images = Dir.glob("public/assets/fallback/*_medium.png")

    #changing number while random image is the same as current image
    loop do
      @number = rand(images.length)
      break if current_user.avatar.medium.file.file.split("/").last != "medium_" + images[@number].split("/").last
    end

    current_user.update(avatar: Rails.root.join(images[@number]).open)
    redirect_to root_url
  end

  protected

  def user_params
    params.require(:user).permit(:password, :password_confirmation)
  end
end
