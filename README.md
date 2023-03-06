# sentiment_analysis_backend
Sentiment analysis with connection to the twitter social network searching for published tweets

# Build an image from a Dockerfile

docker build -t sentiments . 

Permite crear el proyecto desde cero
docker-compose run backend django-admin.py startproject senti .

docker-compose run backend python manage.py startapp api    

docker-compose down
docker-compose build