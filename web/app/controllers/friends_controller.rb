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

  def propose
    user = User.where(id: params[:id])[0]

    if !user.friends_pending.include? current_user.id
      user.update(friends_pending: user.friends_pending += [current_user.id])
      text = "You have sent friend request to #{user.email}."
    else
      text = "You have already sent request to #{user.email}!"
    end

    redirect_to friends_url, notice: text
  end

  def answer
    friend1 = User.where(id: current_user.id)[0]
    friend2 = User.where(id: params[:id])[0]

    text = "You have rejected friend request from #{friend2.email}."

    # if the answer is YES
    if params[:ans] == '1'
      frined1.update(friends: friend1.friends += [friend2.id])
      friend2.update(friends: friend2.friends += [friend1.id])

      text = "You have accepted friend request from #{friend2.email}."
    end

    # anyway deleting user in params from pending friends
    friend1.update(friends_pending: friend1.friends_pending -= [friend2.id])
    redirect_to friends_url, notice: text
  end

  def remove
    friend1 = User.where(id: current_user.id)[0]
    friend2 = User.where(id: params[:id])[0]

    friend1.update(friends: friend1.friends -= [friend2.id])
    friend2.update(friends: friend2.friends -= [friend1.id])

    redirect_to friends_url, notice: "#{friend2.email} was successfully deleted from your friend list."
  end

  protected

  def check_user
    redirect_to admin_dashboard_url if current_user.admin
  end
end
