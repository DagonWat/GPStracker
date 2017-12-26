class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  before_action :require_login
  before_action :check_if_admin

  protected

  def check_if_admin
    redirect_to admin_dashboard_url if current_user.admin?
  end
end
