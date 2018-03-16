class AddGroupToTracker < ActiveRecord::Migration[5.1]
  def change
    add_column :trackers, :group, :integer
  end
end
