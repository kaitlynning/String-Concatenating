print('Celsius to Fahrenheit conversion')

def FahrenheitConverter(c):
   return c *9/5 +32

c = int(input("Plz enter ℃: ").strip())
output = FahrenheitConverter(c)
print("{} ℉".format(output))

'''
Celsius to Fahrenheit conversion
Plz enter ℃: 30
86.0 ℉
'''