client_id = ''
client_secret = ''

def setup():
    client_id = config.client_id
    client_secret = config.client_secret
    run_command(Fore.BLACK, f"export SPOTIPY_CLIENT_ID='{client_id}' && export SPOTIPY_CLIENT_SECRET='{client_secret}' && export SPOTIPY_REDIRECT_URI='https://example.com'")
