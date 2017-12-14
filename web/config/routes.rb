Rails.application.routes.draw do
  # UNREGISTERED ROUTES START
  get  'login'  => 'user_sessions#new'
  post 'login'  => 'user_sessions#create'
  post 'logout' => 'user_sessions#destroy', :as => :logout
  resource :registration, only: [:new, :create], controller: :registration do
    member do
      get :activate
    end
  end

  resource  :password_reset, only: [:new, :edit, :update, :create], controller: :password_reset
  # UNREGISTERED ROUTES END

  # ADMIN ROUTES START
  namespace :admin do
    resource :dashboard, only: [:show],          controller: :dashboard
    resource :profile,   only: [:edit, :update], controller: :profile
    resources :users
  end
  # ADMIN ROUTES END

  # USER ROUTES START
  resource  :profile, only: [:edit, :update], controller: :profile

  resource :dashboard, only: [:show], controller: :dashboard
  # USER ROUTES END

  # TRACKER ROUTES START
  namespace :api do
    resources :tracker, only: [:create]
  end
  # TRACKER ROUTES END

  root "guest#index"
end
