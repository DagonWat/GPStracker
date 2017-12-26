# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

user = User.create(created_at: Time.zone.now.change(hour: 13) - 7.days, updated_at: Time.zone.now.change(hour: 13) - 7.days,
              email: 'aa@bb', password: 'root', password_confirmation: 'root', tracker_token: '00000000')
user.activate!

track = [
  [Time.zone.now.change(hour: 16),
    [
      [53.654861, 23.801670],
      [53.655783, 23.800672],
      [53.654555, 23.797032],
      [53.653564, 23.793054],
      [53.653619, 23.793033],
      [53.655171, 23.786725],
      [53.657867, 23.781961],
      [53.660817, 23.782562],
      [53.665928, 23.786210],
      [53.666233, 23.785266],
      [53.665814, 23.783528],
      [53.665686, 23.781253],
      [53.659075, 23.775266]
    ]
  ],
  [Time.zone.now.change(hour: 11),
    [
      [53.654970, 23.801537],
      [53.654665, 23.800335],
      [53.654665, 23.800335],
      [53.654525, 23.797159],
      [53.655745, 23.800550],
      [53.656737, 23.803425],
      [53.657869, 23.806494],
      [53.658670, 23.808811],
      [53.659420, 23.810871],
      [53.661429, 23.816150],
      [53.662332, 23.817501],
      [53.664850, 23.819282],
      [53.666273, 23.820291],
      [53.668346, 23.822179],
      [53.669312, 23.822995],
      [53.671613, 23.825655],
      [53.673291, 23.827822],
      [53.674511, 23.828981],
      [53.675846, 23.829346],
      [53.676074, 23.828531]
    ]
  ],
  [Time.zone.now.change(hour: 15) - 7.days,
    [
      [53.660857, 23.787933],
      [53.660914, 23.787278],
      [53.659776, 23.786602],
      [53.658467, 23.785787],
      [53.658162, 23.786055],
      [53.657494, 23.785916],
      [53.656114, 23.786710],
      [53.655415, 23.787428],
      [53.655033, 23.787160],
      [53.654200, 23.789735],
      [53.653545, 23.792171],
      [53.653609, 23.794048],
      [53.653412, 23.794252],
      [53.654499, 23.797149],
      [53.655765, 23.800786],
      [53.654868, 23.801666]
    ]
  ],
  [Time.zone.now.change(hour: 12) - 4.days,
    [
      [53.700847, 23.813702],
      [53.699171, 23.814367],
      [53.698993, 23.815375],
      [53.699196, 23.818315],
      [53.699387, 23.820461],
      [53.699882, 23.824817],
      [53.699882, 23.824817],
      [53.700847, 23.833958],
      [53.701165, 23.833990],
      [53.700886, 23.835106],
      [53.700758, 23.839312],
      [53.699818, 23.839741],
      [53.697309, 23.839778],
      [53.695302, 23.839692],
      [53.692151, 23.837933],
      [53.689064, 23.836281],
      [53.687081, 23.835036],
      [53.685582, 23.835229],
      [53.683206, 23.835251],
      [53.682735, 23.833341],
      [53.682583, 23.832354],
      [53.680778, 23.830852],
      [53.678846, 23.829328],
      [53.678211, 23.830358],
      [53.675821, 23.829200],
      [53.674220, 23.828813],
      [53.671614, 23.825702],
      [53.669326, 23.822934],
      [53.668487, 23.822784],
      [53.667877, 23.821475],
      [53.664912, 23.819301],
      [53.662128, 23.817262],
      [53.659114, 23.809967],
      [53.655770, 23.800740],
      [53.654829, 23.801727]
    ]
  ]
]

track.each do |time, list|
  i = 0
  list.each do |coordinates|
    Tracker.create(created_at: time + i.minutes, updated_at: time + i.minutes, lat: coordinates[0], lon: coordinates[1], user_id: user.id)
    i += 1
  end
end
