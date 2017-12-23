class FriendsController < ApplicationController
  before_action :require_login
  before_action :check_user

  def index
    if !params[:email]
      @friends = User.where(id: current_user.friends)
    else
      @friends = User.where("email LIKE :email",
                {email: "#{params[:email]}%"})
      @friends.delete(current_user.id)
    end
  end

  def remove
    list = [current_user.id, params[:id]]

    for i in 0..1
      ActiveRecord::Base.connection.
            execute("UPDATE #{"users"} SET #{"friends"} = array_remove(#{"friends"}, #{list[i]}) WHERE #{"users"}.#{"id"} = #{list[1 - i]}")
    end

    redirect_to friends_url, notice: "#{User.where(id: params[:id])[0].email} was successfully deleted from your friend list."
  end

  def propose
    if !User.where(id: params[:id])[0].friends_pending.include? current_user.id
      ActiveRecord::Base.connection.
        execute("UPDATE #{"users"} SET #{"friends_pending"} = array_append(#{"friends_pending"}, #{current_user.id}) WHERE #{"users"}.#{"id"} = #{params[:id]}")
      text = "You have sent friend request to #{User.where(id: params[:id])[0].email}."
    else
      text = "You have already sent request to #{User.where(id: params[:id])[0].email}!"
    end

    redirect_to friends_url, notice: text
  end

  def answer
    text = "You have rejected friend request from #{User.where(id: params[:id])[0].email}."

    if params[:ans] == '1'
      list = [current_user.id, params[:id]]

      for i in 0..1
        ActiveRecord::Base.connection.
          execute("UPDATE #{"users"} SET #{"friends"} = array_append(#{"friends"}, #{list[i]}) WHERE #{"users"}.#{"id"} = #{list[1 - i]}")
      end

      text = "You have accepted friend request from #{User.where(id: params[:id])[0].email}."
    end

    ActiveRecord::Base.connection.
      execute("UPDATE #{"users"} SET #{"friends_pending"} = array_remove(#{"friends_pending"}, #{params[:id]}) WHERE #{"users"}.#{"id"} = #{current_user[:id]}")

    redirect_to friends_url, notice: text
  end

  protected

  def check_user
    redirect_to admin_dashboard_url if current_user.admin
  end
end
