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
end
