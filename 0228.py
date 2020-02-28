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
print('Total guesses %d times' % counter)

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
'''