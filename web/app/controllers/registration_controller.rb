class RegistrationController < ApplicationController
  skip_before_action :require_login

  def new
    @user = User.new
  end

  def create
    @user = User.new(user_params)

    if @user.save
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
