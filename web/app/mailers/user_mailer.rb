class UserMailer < ApplicationMailer
  
  def activation_needed_email(user)
    @user = user
    @url = activate_registration_url(id: user.activation_token)
    mail(to: user.email, subject: 'Welcome to tracker-dev!')
  end

  def activation_success_email(user)
    @user = user
    @url  = login_url()
    mail(to: user.email, subject: 'Your account is now activated')
  end

  def reset_password_email(user)
    @user = User.find user.id
    @url  = edit_password_reset_url(@user.reset_password_token)
    mail(to: user.email, subject: 'Reset your password')
  end
end
