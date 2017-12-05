Rails.application.routes.draw do

  get 'password_resets/create'

  get 'password_resets/edit'

  get 'password_resets/update'

  resources :user_sessions

  resources :users

  resources :admin, except: [:show]
  get 'admin/users'

  resources :guest, only: [:index] do
    member do
      get :activate
    end
  end

  get 'login' => 'user_sessions#new', :as => :login
  post 'logout' => 'user_sessions#destroy', :as => :logout

  namespace :api do
    resources :tracker, only: [:create]
  end

  root "admin#index"

  resources :dashboard, only: [:show]

  resources :password_resets

end
