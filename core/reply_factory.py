
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if current_question_id is None:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id, session)
    answers = session.get("answers", {})

    if next_question_id is not None:
        bot_responses.append(next_question)
        session["current_question_id"] = next_question_id
    elif len(answers) == len(PYTHON_QUESTION_LIST):
        final_response = generate_final_response(session)
        bot_responses.append(final_response)
        session["current_question_id"] = int(len(PYTHON_QUESTION_LIST)+1)
    elif len(answers) > len(PYTHON_QUESTION_LIST):
        bot_responses.append(next_question)

    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
    if current_question_id is None:
        return True, ""

    if not answer:
        return False, "Please provide an answer"

    answers = session.get("answers", {})

    if current_question_id >= len(PYTHON_QUESTION_LIST):
        return False, "Invalid question ID"

    current_question = PYTHON_QUESTION_LIST[current_question_id]

    if answer.lower() not in [opt.lower() for opt in current_question["options"]]:
        return False, "Please select a valid option"

    answers[current_question_id] = answer
    session["answers"] = answers

    return True, ""


def get_next_question(current_question_id, session):
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''
    answers = session.get("answers", {})
    if len(answers) == len(PYTHON_QUESTION_LIST):
        return "Quiz completed! Thank you for participating.", None

    if current_question_id is None:
        next_id = 0
    else:
        next_id = current_question_id + 1

    if next_id >= len(PYTHON_QUESTION_LIST):
        return "Quiz completed! Thank you for participating.", next_id

    question = PYTHON_QUESTION_LIST[next_id]
    formatted_question = f"{question.get('question_text')}\n\nOptions:\n"
    for option in question.get("options", []):
        formatted_question += f"{option},\n"
    return formatted_question, next_id


def generate_final_response(session):
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''
    answers = session.get("answers", {})
    correct_count = 0

    for index, question in enumerate(PYTHON_QUESTION_LIST):
        correct_answer = question.get("answer")
        user_answer = answers.get(index)
        if user_answer and user_answer.lower() == correct_answer.lower():
            correct_count += 1

    total_questions = len(PYTHON_QUESTION_LIST)
    score_percentage = (correct_count / total_questions) * 100

    response = f"Quiz completed!\n\n"
    response += f"You answered {correct_count} out of {total_questions} questions correctly.\n"
    response += f"Your score: {score_percentage:.1f}%\n\n"

    if score_percentage >= 80:
        response += "Excellent work! 🎉"
    elif score_percentage >= 60:
        response += "Good job! Keep practicing! 👍"
    else:
        response += "Keep learning and try again! 💪"

    return response
