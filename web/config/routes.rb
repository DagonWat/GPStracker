Rails.application.routes.draw do
    get 'welcome/index'

    post "api/sometest" => "tracker#create"

    resources :articles do
        resources :comments

        member do
            #get '/lol', to: 'articles#lol', via: :get
            #match '/lol' => 'articles#lol', via: :get
        end
    end

    root "welcome#index"

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
