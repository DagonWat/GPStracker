class AddCustomThumbImage < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :custom_avatar_thumb, :string
  end
end
