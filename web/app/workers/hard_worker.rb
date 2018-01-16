class HardWorker
  include Sidekiq::Worker
  #Sidekiq::Cron::Job.create(name: '5 min worker', cron: '*/5 * * * *', class: 'HardWorker')
  def perform()
    tracks = Tracker.order(:created_at).where(group: -1)
    for i in 0..(tracks.length() - 1)
      user = User.find(tracks[i].user_id)
      saved_track = Tracker.order(:created_at).where(user_id: user.id).where(group: 0..Float::INFINITY)

      if (saved_track.any?)
        last_tr = saved_track.last
        if (tracks[i].created_at - 15.minutes > last_tr.created_at)
          tracks[i].update(group: last_tr.group += 1)
        else
          tracks[i].update(group: last_tr.group)
        end
      else
        tracks[i].update(group: 0)
      end
    end
  end
end
