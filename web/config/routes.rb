Rails.application.routes.draw do

    resources :tracker, path: '/api/sometest'

    root "welcome#index"
end
