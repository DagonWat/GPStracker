class EvenBetterNums < ActiveRecord::Migration[5.1]
  def change
    change_column_null :trackers, :lat, false
    change_column_null :trackers, :lon, false
  end
end
