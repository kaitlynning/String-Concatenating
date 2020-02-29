row =int(input('Insert num: '))

for i in range(row):
	for _ in range(i + 1):
		#end=add space no newline
		print('*', end = '')
	#wrap text
	print()

for i in range(row):
	for j in range(row):
		if j < row -i - 1:
			print(' ', end = '')
		else:
			print('*', end = '')
	print()

for i in range(row):
	for j in range(row):
		if j < row -i - 1:
			print('', end = ' ')
		else:
			print('*', end = ' ')
	print()
for i in range(row):
	for j in range(row):
		if j <= i - 1:
			print('', end = ' ')
		else:
			print('*', end = ' ')
	print()

for i in range(row):
	for _ in range(row - i - 1):
		print(' ', end = '')
	for _ in range(i*2 + 1):
		print('*', end = '')
	print() 

'''
Insert num: 8
*
**
***
****
*****
******
*******
********
       *
      **
     ***
    ****
   *****
  ******
 *******
********
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
* * * * * * * * 
* * * * * * * * 
 * * * * * * * 
  * * * * * * 
   * * * * * 
    * * * * 
     * * * 
      * * 
       * 
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
'''