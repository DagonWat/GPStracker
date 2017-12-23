class AddFriendsToUser < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :friends_pending, :integer, array: true, default: []
    add_column :users, :friends, :integer, array: true, default: []
  end
end
