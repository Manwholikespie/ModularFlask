from appname import create_app

app = create_app('config')
app.run(debug=True)