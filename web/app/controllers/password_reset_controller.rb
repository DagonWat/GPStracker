class PasswordResetController < ApplicationController
  skip_before_action :require_login
  skip_before_action :check_if_admin

  def new
  end

  # request password reset.
  # you get here when the user entered his email in the reset password form and submitted it.
  def create
    @user = User.where(email: params[:email]).first
    UserMailer.reset_password_email(@user).deliver_now if @user.present?
    flash.now[:alert] = 'Instructions have been sent to your email.'
    render action: 'new'
  end

  # This is the reset password form.
  def edit
    @token = params[:id]
    @user = User.load_from_reset_password_token(params[:id])

    if @user.blank?
      not_authenticated
      return
    end
  end

  # This action fires when the user has sent the reset password form.
  def update
    @token = params[:id]
    @user = User.load_from_reset_password_token(params[:id])

    if @user.blank?
      not_authenticated
      return
    end

    # the next line makes the password confirmation validation work
    @user.password_confirmation = params[:user][:password_confirmation]
    # the next line clears the temporary token and updates the password
    if @user.change_password!(params[:user][:password])
      redirect_to(root_path, :notice => 'Password was successfully updated.')
    else
      render :action => "edit"
    end
  end
end
