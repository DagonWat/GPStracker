Rails.application.routes.draw do

  namespace :api do
    resources :tracker, only: [:create]
  end

  root "dashboard#index"

  resources :dashboard, only: [:show]

end
