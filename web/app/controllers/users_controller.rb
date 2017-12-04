class UsersController < ApplicationController
  before_action :set_user, only: [:show, :edit, :update, :destroy]

  def index
    @trackers = Tracker.order(:created_at)

    @from = Time.now.strftime("%Y-%m-%d 00:00:00")

    @until = Time.now.strftime("%Y-%m-%d 23:59:59")

    @today = Tracker.where("created_at >= :start_date AND created_at <= :end_date",
      {start_date: @from, end_date: @until})
  end

  # GET /users/1/edit
  def edit
    @act = "Edit User"
    @trackers = Tracker.order(:created_at)
  end

  def new
    @act = "New User"
    @user = User.new
  end


  # POST /users
  # POST /users.json
  def create
    @user = User.new(user_params)

    if @user.save
      UserMailer.activation_needed_email(@user).deliver_now
      redirect_to root
      flash[:notice] = 'User was succesfully created.'
    else
      if current_user.admin
        redirect_to new_admin_path
      else
        render :new
      end
    end
  end

  # PATCH/PUT /users/1
  # PATCH/PUT /users/1.json
  def update
    if @user.update(user_params)
      redirect_to @user, notice: "User was successfully updated."
    else
      render :edit
    end
  end

  # DELETE /users/1
  # DELETE /users/1.json
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
