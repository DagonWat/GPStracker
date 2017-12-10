Rails.application.routes.draw do
  # UNREGISTERED ROUTES START
  get  'login'  => 'user_sessions#new'
  post 'login'  => 'user_sessions#create'
  post 'logout' => 'user_sessions#destroy', :as => :logout

  resource  :password_reset, only: [:new],                    controller: :password_reset
  resources :password_reset, only: [:edit, :update, :create], controller: :password_reset
  # UNREGISTERED ROUTES END

  # ADMIN ROUTES START
  namespace :admin do
    resource  :dashboard,  only: [:show, :index],                   controller: :dashboard
    resource  :profile,    only: [:show, :destroy],                 controller: :profile
    resource  :users,      only: [:show]
    resources :user,       only: [:show, :edit, :update, :destroy], controller: :user
  end
  # ADMIN ROUTES END

  # USER ROUTES START
  resource  :profile, only: [:show, :new, :create, :edit, :update, :destroy], controller: :profile
  resources :profile, only: [] do
    member do
      get :activate
    end
  end
  get 'profile/index' => 'profile#index'
  # USER ROUTES END

  # TRACKER ROUTES START
  resources :dashboard, only: [:show]

  namespace :api do
    resources :tracker, only: [:create]
  end
  # TRACKER ROUTES END

  root "guest#index"
end
