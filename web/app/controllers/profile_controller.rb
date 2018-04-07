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
    images = Dir.glob("app/assets/images/*_medium.png")

    #changing number while random image is the same as current image
    loop do
      @number = rand(images.length)
      break if !current_user.custom_avatar.present? || current_user.custom_avatar != images[@number][18..-1]
    end

    current_user.update(custom_avatar: images[@number][18..-1])
    thumb = images[@number].split("_")[0][18..-1] + "_thumb.png"
    current_user.update(custom_avatar_thumb: thumb)
    redirect_to root_url
  end

  protected

  def user_params
    params.require(:user).permit(:password, :password_confirmation)
  end
end
