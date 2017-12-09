class GuestController < ApplicationController
  skip_before_action :require_login
  before_action :check_user

  def index
  end

  protected
    def check_user
      redirect_to admin_dashboard_path if current_user
    end
end
