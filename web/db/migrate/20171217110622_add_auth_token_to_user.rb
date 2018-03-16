class AddAuthTokenToUser < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :tracker_token, :string
  end
end
