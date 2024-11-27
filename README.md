# Quiz bot
This is a basic version of an interactive quiz bot that engages users in quizzes, evaluates their responses, and provides a final score based on their answers. In this we use Django channels websocket communication, redis as message broker, and Django sessions for temporary data storage.

## Handling Cases
1. `Validations` : Invalid option, No answer provided.
2. Generate next question by based on `number of answers` & `current_qid` ( this approach because even if qid is updated, number of questioned answers list can never go wrong. It is just to keep track the number of answers).
3. Enter `restart` to restart quiz.
4. Once quiz is completed, user cannot answer again until they `restart`.

### Steps to run the project with Docker

1. Install Docker and Docker Compose (https://docs.docker.com/compose/install/)
2. Docker should be running
3. In the project root run `docker-compose build` and `docker-compose up`
4. Go to `localhost` to view the chatbot


### Steps to run the project without Docker

1. Install required packages by running `pip install -r requirements.txt`
2. Install and run postgresql, and change the `DATABASES` config in `settings.py`, if required.
3. Install and run redis, and update the `CHANNEL_LAYERS` config in `settings.py`, if required.
4. In the project root run `python manage.py runserver`
4. Go to `127.0.0.1:8000` to view the chatbot
