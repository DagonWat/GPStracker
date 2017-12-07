class AdminController < ApplicationController
  before_action :check_if_admin
  skip_before_action :require_login
  before_action :set_user, only: [:show, :destroy]

  def show
  end

  def index
  end

  def users
    @users = User.all
  end

  protected
    def check_if_admin
      if !current_user
        redirect_to guest_index_path
      elsif !current_user.admin
        redirect_to profile_index_path(current_user.id)
      end
    end

  private
    def set_user
      @user = User.find(params[:id])
    end
end
