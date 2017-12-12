module Admin
  class DashboardController < BaseController
    before_action :check_if_admin
    before_action :require_login

    def show
    end

    protected
      def check_if_admin
        redirect_to profile_index_path unless current_user.admin
      end
  end
end
