Rails.application.routes.draw do

  get 'password_resets/create'

  get 'password_resets/edit'

  get 'password_resets/update'

  resources :user_sessions, only: [:new, :create, :destroy]

  resources :profile, only: [:show, :index]

  get 'admin/users'
  resources :admin

  resources :users, only: [:new, :create, :edit, :update, :destroy] do
    member do
      get :activate
    end
  end

  resources :guest, only: [:index]

  get 'login' => 'user_sessions#new', :as => :login
  post 'logout' => 'user_sessions#destroy', :as => :logout

  namespace :api do
    resources :tracker, only: [:create]
  end

  root "admin#index"

  resources :dashboard, only: [:show]

  resources :password_resets

end
