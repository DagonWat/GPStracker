class AdminController < ApplicationController
  before_action :check_if_admin
  skip_before_action :require_login

  def index
    @trackers = Tracker.order(:created_at)
  end

  def new
    @act = "New User"
    @email_f = ""
    @user = User.new
    @trackers = Tracker.order(:created_at)
  end

  def update
    if @user.update(user_params)
      redirect_to @user, notice: "User was successfully updated."
    else
      render :edit
    end
  end

  def edit
    @act = "Edit Admin"
    @email_f = current_user.email
    @trackers = Tracker.order(:created_at)
  end

  def destroy
    @user.destroy
    @trackers = Tracker.order(:created_at)
    redirect_to root, notice: "User was successfully destroyed."
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

end
