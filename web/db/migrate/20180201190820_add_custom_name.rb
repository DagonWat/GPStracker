class AddCustomName < ActiveRecord::Migration[5.1]
  def change
    add_column :trackers, :custom_name, :string
  end
end
