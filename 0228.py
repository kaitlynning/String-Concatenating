import random

answer = random.randint(1, 100)
counter = 0
while True:
	counter += 1
	number = int(input('insert:'))
	if number < answer:
		print('larger')
	elif number > answer:
		print('smaller')
	else:
		print('Congrats, you got the right number')
		break
#use f-string
print (f"Total guesses {counter} times")
'''
insert:70
smaller
insert:65
smaller
insert:50
smaller
insert:20
larger
insert:30
larger
insert:40
Congrats, you got the right number
Total guesses 6 times

#Change to f-string
print (f"Total guesses {counter} times")
print('Total guesses %d times' % counter)
'''
