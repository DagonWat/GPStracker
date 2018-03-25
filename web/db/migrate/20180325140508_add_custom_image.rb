class AddCustomImage < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :custom_avatar, :string
  end
end
