class CreateTrackers < ActiveRecord::Migration[5.1]
  def change
    create_table :trackers do |t|
      t.float :lat
      t.float :lon

      t.timestamps
    end
  end
end
