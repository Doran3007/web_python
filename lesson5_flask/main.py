from lesson5_flask.store_app import store_app

store_app.config.update(
    DEBUG=True,
)

if __name__=='__main__':
    store_app.run(debug=True)