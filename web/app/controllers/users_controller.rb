class UsersController < ApplicationController
  skip_before_action :require_login, only: [:new, :create]
  before_action :set_user, only: [:show, :edit, :update, :destroy]

  def index
    @trackers = Tracker.order(:created_at)

    @from = Time.now.strftime("%Y-%m-%d 00:00:00")

    @until = Time.now.strftime("%Y-%m-%d 23:59:59")

    @today = Tracker.where("created_at >= :start_date AND created_at <= :end_date",
      {start_date: @from, end_date: @until})
  end

  def show
    @trackers = Tracker.order(:created_at)
  end

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
      redirect_to root
      flash[:notice] = 'User was succesfully created.'
    else
      render :new
    end
  end

  def update
    @trackers = Tracker.order(:created_at)
    if @user.update(user_params)
      redirect_to @user, notice: "User was successfully updated."
    else
      render :edit
    end
  end

  def destroy
    @user.destroy
    @trackers = Tracker.order(:created_at)
    redirect_to users_url, notice: "User was successfully destroyed."
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user
      @user = User.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_params
      params.require(:user).permit(:email, :password, :password_confirmation, admin: 0)
    end
end
