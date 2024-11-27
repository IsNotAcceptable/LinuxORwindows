import sys
import statistics

def get_answers():
    answers = []
    print("Ответьте на следующие вопросы, используя шкалу от 1 до 5 (1 - совсем не важно, 5 - очень важно):")
    questions = ["Насколько для вас важна стабильность операционной системы?",
                 "Насколько для вас важна безопасность операционной системы?",
                 "Насколько для вас важна производительность операционной системы?",
                 "Насколько для вас важна совместимость операционной системы с различным программным обеспечением?",
                 "Насколько для вас важна стоимость операционной системы?"]
    for question in questions:
        answer = int(input(question + " "))
        answers.append(answer)
    return answers

def analyze_answers(answers):
    windows_score = (answers[0] + answers[1] + answers[2]) / 3
    linux_score = (answers[3] + answers[4]) / 2

    if windows_score > linux_score:
        return "Windows"
    else:
        return "Linux"

answers = get_answers()
result = analyze_answers(answers)
print("Наиболее подходящая для вас операционная система:", result)
