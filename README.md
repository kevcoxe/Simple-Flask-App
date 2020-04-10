### Simple Flask App Tutorial

This is the output of the tutorial I built [here](http://kevcoxe.github.io/Simple-Flask-App/)!. To get this up and running easy you can use Docker or Docker Compose.

Example docker command
```
docker run kevcoxe/simple-flask-app -p 5000:5000 --name=simple-flask-app
# will start the app at (http://localhost:5000)
```

Example docker-compose command
```
# clone this repo
# cd into the repo
docker-compose up

# will start the app at (http://localhost:8000)
```

Example running this just as python
```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python app.py
# will start the app at (http://localhost:5000)
```


