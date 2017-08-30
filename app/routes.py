from app import config

config.add_route("home", "")

config.add_route("quotes", "/quotes")
config.add_route("random_quote", "/quotes/random")
config.add_route("quote", "/quotes/{number:\d+}")

config.add_route("dashboard", "/dashboard")
