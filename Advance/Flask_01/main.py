from products import app

if __name__ == '__main__':
	app.config.from_object('config.ConfigDev')
	app.run(debug=True)


