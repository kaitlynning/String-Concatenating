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
insert:40
larger
insert:60
larger
insert:80
larger
insert:90
larger
insert:95
larger
insert:99
smaller
insert:97
Congrats, you got the right number
Total guesses 7 times

#Change to f-string
print (f"Total guesses {counter} times")
print('Total guesses %d times' % counter)
'''