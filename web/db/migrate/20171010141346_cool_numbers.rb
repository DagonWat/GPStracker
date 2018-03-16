class CoolNumbers < ActiveRecord::Migration[5.1]
  def change
    change_column_null(:trackers, :lat, true)
    change_column_null(:trackers, :lon, true)
  end
end
