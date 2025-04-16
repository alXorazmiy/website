import pusher

pusher_client = pusher.Pusher(
    app_id='1975067',
    key='a1dd35e4fe0e49e62d9b',
    secret='d09640f96bb2e81faa8b',
    cluster='us2',
    ssl=True
)

# pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})