import random


def answer(question):
    answers = [
        "Bien sûr mon petit",
        "Comme tu veux",
        "Selon ta demande",
        "Bien volontier",
    ]

    return {
        "error": False,
        "result": question.upper(),
        "answer": random.choice(answers),
    }

