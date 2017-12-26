class RegistrationController < ApplicationController
  skip_before_action :require_login
  skip_before_action :check_if_admin

  def new
    @user = User.new
  end

  def create
    @user = User.new(user_params)
    @user.tracker_token = SecureRandom.hex(4)

    if @user.save
      @user.tracker_token = SecureRandom.hex(4)
      UserMailer.activation_needed_email(@user).deliver_now
      redirect_to root_url
      flash[:notice] = 'User was succesfully created. We have sent you an email with activation.'
    else
      render :new
    end
  end

  def activate
    if (@user = User.load_from_activation_token(params[:id]))
      @user.activate!
      redirect_to login_url, notice: 'User was successfully activated.'
    else
      not_authenticated
    end
  end

  protected

  def user_params
    params.require(:user).permit(:email, :password, :password_confirmation)
  end
end
