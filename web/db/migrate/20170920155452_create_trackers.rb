class CreateTrackers < ActiveRecord::Migration[5.1]
  def change
    create_table :trackers do |t|
      t.integer :lat
      t.integer :lon

      t.timestamps
    end
  end
end
