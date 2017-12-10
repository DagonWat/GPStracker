module Admin
  class ProfileController < ApplicationController
    before_action :check_if_admin
    before_action :require_login

    def show
    end

    def destroy
      current_user.destroy
      redirect_to root_path, notice: current_user.email + ' was successfully destroyed.'
    end

    protected
      def check_if_admin
        redirect_to profile_index_path unless current_user.admin
      end
  end
end
