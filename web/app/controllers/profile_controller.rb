class ProfileController < ApplicationController
  before_action :require_login, except: [:new, :create, :activate]

  def new
    @user = User.new
  end

  def show
    @trackers = Tracker.order(:created_at)
  end

  def index
    @trackers = Tracker.order(:created_at)

    @from = Time.now.strftime('%Y-%m-%d 00:00:00')
    @until = Time.now.strftime('%Y-%m-%d 23:59:59')

    @today = Tracker.where('created_at >= :start_date AND created_at <= :end_date',
      {start_date: @from, end_date: @until})
  end

  def create
    @user = User.new(user_params)

    if @user.save
      UserMailer.activation_needed_email(@user).deliver_now
      redirect_to root_path
      flash[:notice] = 'User was succesfully created. We have sent you an email with activation.'
    else
      render :new
    end
  end


  def edit
    @trackers = Tracker.order(:created_at)
  end

  def update
    @trackers = Tracker.order(:created_at)

    if current_user.update(user_params)
      redirect_to admin_dashboard_path, notice: 'Password for ' + current_user.email + ' was successfully updated.'
    else
      render :edit
    end
  end

  def activate
    if (@user = User.load_from_activation_token(params[:id]))
      @user.activate!
      if !current_user
        redirect_to login_path, notice: 'User was successfully activated.'
      elsif current_user.admin
        redirect_to admin_index_path, notice: 'User ' + @user.email + ' was successfully activated.'
      end
    else
      not_authenticated
    end
  end

  def destroy
    @trackers = Tracker.order(:created_at)
    current_user.destroy
    redirect_to root_path, notice: current_user.email + ' was successfully destroyed.'
  end

  private
    def user_params
      params.require(:user).permit(:email, :password, :password_confirmation)
    end

end
