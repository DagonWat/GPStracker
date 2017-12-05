class AdminController < ApplicationController
  before_action :check_if_admin
  skip_before_action :require_login
  before_action :set_user, only: [:show, :edit, :update, :destroy]

  def index
    @trackers = Tracker.order(:created_at)
  end

  def new
    @act = 'New User'
    @trackers = Tracker.order(:created_at)
    @user = User.new
  end

  def edit
    @act = 'Edit Admin'
    @email_f = current_user.email
    @trackers = Tracker.order(:created_at)
  end

  def create
    @tracker = Tracker.order(:created_at)
    @user = User.new(user_params)

    if @user.save
      UserMailer.activation_needed_email(@user).deliver_now
      redirect_to root_path
      flash[:notice] = 'User was succesfully created.'
    else
      render admin_new_path
    end
  end

  def update
    if @user.update(user_params)
      redirect_to @user, notice: 'Admin was successfully updated.'
    else
      render :edit
    end
  end

  def destroy
    @user.destroy
    @trackers = Tracker.order(:created_at)
    redirect_to root, notice: 'User was successfully destroyed.'
  end

  def users
    @users = User.all
    @trackers = Tracker.order(:created_at)
  end

  protected

  def check_if_admin
    if !current_user
      redirect_to guest_index_path
    elsif !current_user.admin
      redirect_to users_path
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user
      @user = User.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_params
      params.require(:admin).permit(:email, :password, :password_confirmation)
    end

end
