module Admin
  class UserController < ApplicationController
    before_action :check_if_admin
    before_action :require_login
    before_action :set_user

    def show
    end

    def edit
    end

    def update
      if @user.update(user_params)
        redirect_to admin_dashboard_path, notice: 'Password for ' + @user.email + ' was successfully updated.'
      else
        render :edit
      end
    end

    def destroy
      @user.destroy
      redirect_to admin_dashboard_path, notice: @user.email + ' was successfully destroyed.'
    end

    protected
      def check_if_admin
        redirect_to profile_index_path unless current_user.admin
      end

    private
      def set_user
        @user = User.find(params[:id])
      end

      def user_params
        params.require(:user).permit(:email, :password, :password_confirmation)
      end
  end
end
