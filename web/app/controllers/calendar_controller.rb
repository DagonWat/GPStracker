class CalendarController < ApplicationController
  before_action :require_login
  before_action :check_user

  def index
    @calendar_service = CalendarService.new(current_user, params[:date])


    # @trackers = Tracker.where(user_id: current_user.id)
    # @begin = Time.local(2017, "jan", 1)
    # @colors = ['#072c66', '#234882', '#637231', '#6ead3e', '#9af754', '#e5493d',
    #                 '#bc2e23', '#e84610', '#dba14a', '#a3670d', '#ad6c47', '#29518e']
    #
    # if params[:date].present? && params[:date].to_i >= 0
    #   from_begin = @begin + params[:date].to_i.month
    #   @month = from_begin.strftime("%B")
    #   @year = from_begin.year
    #   @state = from_begin
    # elsif params[:date].to_i < 0
    #   @state = Time.zone.now
    #   @year = Time.zone.now.year
    #   @month = Time.zone.now.strftime("%B")
    #   redirect_to calendar_index_url
    # else
    #   @state = @begin + (Time.zone.now.month - 1).month
    #   @year = Time.zone.now.year
    #   @month = Time.zone.now.strftime("%B")
    # end
    #
    # @last = Date.civil(@state.year, @state.month, -1).day
    #
    # @ids = {}
    # for i in 1..(@last)
    #   @from = (@state + (i - 1).day).strftime('%Y-%m-%d 00:00:00')
    #   @until = (@state + (i - 1).day).strftime('%Y-%m-%d 23:59:59')
    #   # .all not needed
    #   @track = Tracker.all.where(user_id: current_user.id).where('created_at >= :start_date AND created_at <= :end_date',
    #     {start_date: @from, end_date: @until}).first
    #   if @track
    #     @id = @track.id
    #     if @id > 0
    #       @ids[i] = @id
    #     end
    #   end
    # end
    #
    # @color = @colors[@state.month - 1]
    # @diff = (@state.year - @begin.year) * 12 + @state.month - @begin.month
  end

  protected

  def check_user
    redirect_to admin_dashboard_url if current_user.admin
  end
end
