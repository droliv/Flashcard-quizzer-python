import sys
import random


# if len(sys.argv) <2:
#     print('Por favor, forneça o arquivo para o flashcard.')
#     sys.exit(0)

# flashcard_file = sys.argv[1]
file = open('quizz.txt', encoding="utf8")

quizz_dict = {}
for line in file:
    entry = line.strip().split(',')
    question = entry[0]
    answers = []
    for e in range(1,len(entry)):
        answers.append(entry[e])
    quizz_dict[question] = answers

    
file.close()

print('Bem vindo ao Flash Card game')
print("a qualquer momento digite 'quit' para encerrar")

questions = list(quizz_dict.keys())


while True:
    question = random.choice(questions)
    answers = quizz_dict[question]
    correct_answer = answers[0]
    
    print('Pergunta:' + question)
    
    sorted_options = sorted(answers)
    
    dict_options = {}
    
    for i, option in enumerate(sorted_options):
        print(str(i) + ': ' + option + '\n')
        dict_options[str(i)]=option
        
    user_input = input('Sua resposta: ')
    
    if user_input == 'quit':
        print('Obrigada por jogar, até mais...')
        break
    if dict_options[user_input].strip() == correct_answer.strip():
        print('Você acertou!')
    else:
        print('Sinto muito, você errou!')