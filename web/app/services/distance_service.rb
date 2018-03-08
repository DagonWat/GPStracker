class DistanceService
  attr_reader :track_old, :track_new

  def initialize(track1, track2)
    @track_old = track1
    @track_new = track2
  end

  def make_good()
    diff_x = (track_old.lat - track_new.lat) * 71240.3572324
    diff_y = (track_old.lon - track_new.lon) * 111134.86111
    distance = Math.hypot(diff_x, diff_y);

    # 3 is pretty big speed of person in m/s
    max_distance = (track_new.created_at - track_old.created_at) * 3
    p distance
    p max_distance

    if (max_distance < distance)
      new_x_distance = Math.sin(Math.atan2(diff_x, diff_y)) * max_distance
      new_y_distance = Math.cos(Math.atan2(diff_x, diff_y)) * max_distance
      p new_x_distance
      p new_y_distance
      new_x = new_x_distance / 71240.3572324
      new_y = new_y_distance / 111134.86111
      p new_x
      p new_y
      list = [new_x, new_y]
    else
      list = [track_new.lat, track_new.lon]
    end

    return list
  end

end
