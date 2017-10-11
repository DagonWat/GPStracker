Rails.application.routes.draw do

  namespace :api do
    resources :tracker, path: 'sometest'
  end
  
end
