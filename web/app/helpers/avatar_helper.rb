module AvatarHelper
  def user_avatar_thumb(user)
    user.custom_avatar==nil ? user.avatar.thumb.url : user.custom_avatar_thumb
  end
  def user_avatar_medium(user)
    user.custom_avatar==nil ? user.avatar.medium.url : user.custom_avatar
  end
end
