module Admin
  class UsersController < BaseController
    before_action :set_user, only: [:show, :edit, :update, :destroy]

    def new
      @user = User.new
    end

    def index
      @users = User.all
    end

    def show
    end

    def edit
    end

    def update
      if @user.update(user_params_password)
        redirect_to admin_dashboard_url, notice: "Password for #{@user.email} was successfully updated."
      else
        render :edit
      end
    end

    def create
      @user = User.new(user_params)
      @user.admin = false
      @user.tracker_token = SecureRandom.hex(4)

      if @user.save
        @user.activate!
        redirect_to admin_users_url, notice: "User #{@user.email} was succesfully created."
      else
        render :new
      end
    end

    def destroy
      @user.destroy
      redirect_to admin_users_url, notice: "#{@user.email} was successfully destroyed."
    end

    protected

    def set_user
      @user = User.find(params[:id])
    end

    def user_params_password
      params.require(:user).permit(:password, :password_confirmation)
    end

    def user_params
      params.require(:user).permit(:email, :password, :password_confirmation)
    end
  end
end
