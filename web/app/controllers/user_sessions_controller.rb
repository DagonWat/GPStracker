class UserSessionsController < ApplicationController
  skip_before_action :require_login
  skip_before_action :check_if_admin

  def new
    @user = User.new
  end

  def create
    if @user = login(params[:email], params[:password])
      redirect_back_or_to(:root)
    else
      flash.now[:alert] = 'Email or password is incorrect'
      @email = params[:email]
      render action: 'new'
    end
  end

  def destroy
    logout
    redirect_to(:root)
  end
end
