Rails.application.routes.draw do

  resources :user_sessions
  resources :users

  get 'login' => 'user_sessions#new', :as => :login
  post 'logout' => 'user_sessions#destroy', :as => :logout

  namespace :api do
    resources :tracker, only: [:create]
  end

  root "dashboard#index"

  resources :dashboard, only: [:show]

end
