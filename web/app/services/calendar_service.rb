class CalendarService
  attr_reader :current_user, :current_date

  COLORS = %w[#072c66 #234882 #637231 #6ead3e #9af754 #e5493d #bc2e23 #e84610 #dba14a #a3670d #ad6c47 #29518e]

  def initialize(current_user, current_date = nil)
    @current_user = current_user
    @current_date = convert_current_date(current_date)
  end

  def dates_w_tracking_data
    @available_dates ||=
        current_user.
            trackers.select('DISTINCT DATE(created_at) AS date').
            where('created_at BETWEEN ? AND ?', current_date.beginning_of_month, current_date.end_of_month).
            map(&:date)
    p 111111111111111111111
    p 111111111111111111111
    p @available_dates.last
  end

  def current_month_color
    COLORS[current_date.month-1]
  end

  def current_month_dates
    @current_month_dates ||=
      (current_date.beginning_of_month..current_date.end_of_month).to_a
  end

  def prev_month_start_date
    current_date.prev_month.beginning_of_month
  end

  def next_month_start_date
    current_date.next_month.beginning_of_month
  end

  def user_id
    current_user.id
  end

  protected

  def convert_current_date(current_date)
    Time.zone.parse(current_date).to_date
  rescue TypeError, ArgumentError
    # current_date is nil
    # current_date has incorrect format
    Time.zone.today
  end
end
