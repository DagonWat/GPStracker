class AddUserIdToTrackers < ActiveRecord::Migration[5.1]
  def change
    add_column :trackers, :user_id, :integer, :null => false
  end
end
