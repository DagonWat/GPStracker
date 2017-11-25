class UsersController < ApplicationController
  skip_before_action :require_login, only: [:create, :activate, :new]
  before_action :set_user, only: [:show, :edit, :update, :destroy]

  # GET /users
  # GET /users.json
  def index
    @users = User.all
    @trackers = Tracker.order(:created_at)
  end

  # GET /users/1
  # GET /users/1.json
  def show
    @trackers = Tracker.order(:created_at)
  end

  # GET /users/new
  def new
    @act = "New User"
    @user = User.new
  end

  # GET /users/1/edit
  def edit
    @act = "Edit User"
    @trackers = Tracker.order(:created_at)
  end

  # POST /users
  # POST /users.json
  def create
    @user = User.new(user_params)

    if @user.save
      UserMailer.activation_needed_email(@user).deliver_now
      redirect_to @user
      flash[:notice] = 'User was succesfully created.'
    else
      render :new
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

  def activate
    if (@user = User.load_from_activation_token(params[:id]))
      @user.activate!
      redirect_to login_path, notice: "User was successfully activated."
    else
      not_authenticated
    end
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
