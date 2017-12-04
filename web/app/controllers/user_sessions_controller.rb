class UserSessionsController < ApplicationController
  skip_before_action :require_login

  def new
    @user = User.new
  end

  def create

    p params[:email]
    p params[:password]
    p login(params[:email], params[:password])

    if @user = login(params[:email], params[:password])
      redirect_back_or_to(:root)
    else
      flash.now[:alert] = 'Email or password is incorrect'
      render action: 'new'
    end
  end

  def destroy
    logout
    redirect_to(:root)
  end
end
