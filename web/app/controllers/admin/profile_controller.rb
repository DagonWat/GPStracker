module Admin
  class ProfileController < BaseController

    def edit
    end

    def update
      if current_user.update(user_params) && !params[:user][:password].blank?
        redirect_to admin_dashboard_url, notice: "Password for #{current_user.email} was successfully updated."
      else
        render :edit
      end
    end

    protected

    def user_params
      params.require(:user).permit(:password, :password_confirmation)
    end
  end
end
