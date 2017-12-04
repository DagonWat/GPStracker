class GuestController < ApplicationController
  skip_before_action :require_login

  def index
  end

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

  def new
    @act = "New User"
    @user = User.new
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
