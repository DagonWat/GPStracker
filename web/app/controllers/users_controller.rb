class UsersController < ApplicationController
  skip_before_action :require_login, only: [:new, :create, :activate]
  before_action :set_user, only: [:edit, :update, :destroy]

  def edit
    @trackers = Tracker.order(:created_at)
  end

  def new
    @user = User.new
  end

  def create
    @user = User.new(user_params)

    if @user.save
      UserMailer.activation_needed_email(@user).deliver_now
      redirect_to admin_index_path
      flash[:notice] = 'User was succesfully created. We have sent you an email with activation.'
    else
      render :new
    end
  end

  def update
    @trackers = Tracker.order(:created_at)
    if @user.update(user_params)
      redirect_to admin_index_path, notice: 'Password for ' + @user.email + ' was successfully updated.'
    else
      render :edit
    end
  end

  def activate
    if (@user = User.load_from_activation_token(params[:id]))
      @user.activate!
      if !current_user
        redirect_to login_path, notice: 'User was successfully activated.'
      elsif current_user.admin
        redirect_to admin_index_path, notice: 'User ' + @user.email + ' was successfully activated.'
      end
    else
      not_authenticated
    end
  end

  def destroy
    @user.destroy
    @trackers = Tracker.order(:created_at)
    redirect_to admin_users_path, notice: @user.email + ' was successfully destroyed.'
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user
      @user = User.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_params
      params.require(:user).permit(:email, :password, :password_confirmation)
    end
end
