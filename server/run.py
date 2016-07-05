from app import app

app.debug = True
app.use_reloader = True

if __name__ == "__main__":
    app.run(debug = True)