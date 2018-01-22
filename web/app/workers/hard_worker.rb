class HardWorker
  include Sidekiq::Worker
  #Sidekiq::Cron::Job.create(name: '5 min worker', cron: '*/5 * * * *', class: 'HardWorker')
  def perform()
    while (Tracker.order(:created_at).where(group: -1).length() > 0)
      tracks = Tracker.order(:created_at).where(group: -1)
      user = User.find(tracks[0].user_id)
      from = tracks[0].created_at.beginning_of_day
      to = tracks[0].created_at.end_of_day

      tracks = Tracker.order(:created_at).where(group: -1).where(user_id: user.id).where('created_at BETWEEN ? AND ?', from, to)
      used_tracks = Tracker.order(:created_at).where('"group" > 0').where(user_id: user.id).where('created_at BETWEEN ? AND ?', from, to)

      i = used_tracks.any? ? used_tracks.last.group : 1
      time = used_tracks.any? ? used_tracks.last.created_at : tracks[0].created_at

      tracks.each do |track|
        if (track.created_at > time + 15.minutes)
          i += 1
          time = track.created_at
        else
          time = track.created_at
        end
        track.update(group: i)
      end
    end
  end
end
