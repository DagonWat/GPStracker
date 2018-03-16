class ChangeAdminToBoolean < ActiveRecord::Migration[5.1]
  def change
    change_column :users, :admin, 'boolean USING CAST(admin AS boolean)'
  end
end
