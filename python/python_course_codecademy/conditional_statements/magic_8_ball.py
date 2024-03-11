import random

#name = 'Tim'
name = input('What is your name? ')
#question = 'Will it be sunny today? '
question = input('Please ask the Magic 8-Ball a yes or no question: ')


answer = ''
random_number = random.randint(1, 9)
#print(random_number)

if random_number == 1:
  answer = 'Yes'
elif random_number == 2:
  answer = 'Maybe'
elif random_number == 3:
  answer = 'No'
elif random_number == 4:
  answer = 'Yes indeed'
elif random_number == 5:
  answer = 'Maybe so'
elif random_number == 6:
  answer = 'No way'
elif random_number == 7:
  answer = 'Of course'
elif random_number == 8:
  answer = 'It is a possibility'
elif random_number == 9:
  answer = 'There is no way that will happen'
else:
  answer = 'Error'

print('')
print('Hello ' + name + ', welcome to the Magic 8-Ball program.')
if question == '':
  print('Please ask Magic 8-Ball a question.')
else:
  print('Your question is: ' + question)

#print('Your question is: ' + question)
print('Your answer is: ' + answer)