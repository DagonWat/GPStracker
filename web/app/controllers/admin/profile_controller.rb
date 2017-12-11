module Admin
  class ProfileController < ApplicationController
    before_action :check_if_admin
    before_action :require_login
    before_action :user_params, only: [:update]

    def edit
      @user = current_user
    end

    def update
      if current_user.update(user_params) && !params[:user][:password].blank?
        redirect_to admin_dashboard_path, notice: 'Password for ' + current_user.email + ' was successfully updated.'
      else
        render :edit
      end
    end

    protected
      def check_if_admin
        redirect_to profile_index_path unless current_user.admin
      end

      def user_params
        params.require(:user).permit(:email, :password, :password_confirmation)
      end
  end
end
