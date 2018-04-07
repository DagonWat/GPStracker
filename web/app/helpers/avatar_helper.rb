module AvatarHelper
  def user_avatar_thumb(user)
    user.custom_avatar.present? ? user.custom_avatar_thumb : user.avatar.thumb.url
  end

  def user_avatar_medium(user)
    user.custom_avatar.present? ? user.custom_avatar : user.avatar.medium.url
  end
end
