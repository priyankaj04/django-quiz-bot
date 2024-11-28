# Quiz bot
This is a basic version of an interactive quiz bot that engages users in quizzes, evaluates their responses, and provides a final score based on their answers. In this we use Django channels websocket communication, redis as message broker, and Django sessions for temporary data storage.

## Handling Scenarios
1. Validations:

  * Ensures users provide valid input by handling cases like:
    * `Invalid options`: If the selected option is not among the provided choices.
    * `No answer provided`: If the user submits an empty response.

2. Next Question Logic:

  * Determines the next question based on:
    * `The number of answers recorded so far`: This ensures that the sequence is always accurate, even if the question ID is updated.
    * `The current question ID`: Tracks the user's progress through the quiz seamlessly.
 * This approach guarantees the quiz flow remains consistent and error-free.
   
3. Restart Functionality:

  * Users can type `restart` at any point to reset the quiz.
  * Once the quiz is completed, users are restricted from answering further until they explicitly restart.

4. Completion Handling:

  * Prevents users from submitting answers after the quiz has ended.
  * Provides a clear summary of results and prompts users to restart if they wish to retake the quiz.

5. Exception Handling:

  * Implements robust `try-catch blocks` in every function to ensure errors are handled gracefully.
  * Adheres to best coding practices by:
    * Printing error messages in terminal for easier debugging.
    * Avoiding application crashes due to unexpected input or system issues.
  * This ensures a smooth and reliable user experience.

These structured approaches enhance the quiz application's robustness, maintainability, and user-friendliness, making it a scalable solution.

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
5. 
