class GuestController < ApplicationController
  skip_before_action :require_login
  skip_before_action :check_if_admin
  before_action :check_user

  def index
    HardWorker.perform_in(10.seconds)
  end

  protected

  def check_user
    redirect_to dashboard_url if current_user
  end
end
