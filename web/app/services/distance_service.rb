class DistanceService
  attr_reader :track_old, :track_new

  def initialize(track1, track2)
    @track_old = track1
    @track_new = track2
  end

  def make_good()
    distance_x = (track_old.lat - track_new.lat) * 71.2403572324
    distance_y = (track_old.lon - track_new.lon) * 111.13486111
    distance = Math.hypot(distance_y, distance_x);

    # 3 is pretty big speed of person in m/s
    max_distance = (track_new.created_at - track_old.created_at) * 3
    p distance

    if (max_distance < distance)
      new_x = Math.sin(Math.atan2(distance_x, distance_y)) * max_distance
      new_y = Math.cos(Math.atan2(distance_x, distance_y)) * max_distance
      list = [new_x, new_y]
    else
      list = [track_new.lat, track_new.lon]
    end

    return list
  end

end
