class GuestController < ApplicationController
  skip_before_action :require_login
  before_action :check_user

  def index
  end

  protected

  def check_user
    redirect_to dashboard_url if current_user
  end
end
