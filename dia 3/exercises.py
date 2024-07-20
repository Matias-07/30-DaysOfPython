age = 17;
height = 1.80;
complex = 4j;

base = input('base of triangle:'); 
height = input('height of triangle:')

area_of_triangle = 0.5 * int(base) * int(height) 

print(int(area_of_triangle)); 

side_a = input('side a lenght:')
side_b = input('side b lenght:')
side_c = input('side c lenght:')

perimeter_triangle = int(side_a) + int(side_b) + int(side_c); 

print(int(perimeter_triangle))

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

lenght = int (input('lenght of the rectangle:'))
width = int(input('width of the rectangle:')) 

area_of_rectangle = lenght * width

perimeter_rectangle = 2 * (lenght + width)

print(int(area_of_rectangle))
print(int(perimeter_rectangle))

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

while True:
    radius = input('Radius of circle: ')
    if radius.isdigit(): 
        radius = int(radius)
        break
    else:
        print("Please enter a valid number.")

new_area_circle = 3.14 * (radius ** 2)
print(int(new_area_circle))

ciercunference = 2 * 3.14 * radius
print(int(ciercunference))

# Define the slope from the equation y = 2x - 2
slope = 2

# Calculate the y-intercept (when x = 0)
y_intercept = 2 * 0 - 2

# Calculate the x-intercept (when y = 0)
# 0 = 2x - 2 --> 2x = 2 --> x = 1

x_intercept = 1

print(slope, x_intercept, y_intercept)

x1 = 2
y1 = 2
x2 = 6
y2 = 10

m_slope = y2-y1/x2-x1

print(int(m_slope))

from math import sqrt

print('the Euclidean distance is:1',sqrt((x2-x1)**2+(y2-y1**2)));

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

a = 1
b = 6
c = 9

D = b**2 - 4*a*c

if D < 0:
    print("There are no real solutions for x that make y = 0.")
else:
    x = int(-b / (2*a))
    print(f'There is one solution for x that makes y = 0: x = {x}')

python = len('python'); 
dragon = len('dragon');

print(not (python == dragon)); 
print('on' in 'python' and 'on' in 'dragon'); 
print('jargon' in 'I hope this course is not full of jargon');
print(not'on' in 'python' and not 'on' in 'dragon'); 
print(float(python))
print(str(python))

num = 6 

if (num % 2 == 0): 
    print('is an even number:',num)
else: 
    print('is not an even number')

print(7//3 == int(2.7))
print(type('10') == type(10)) 
print(int(float('9.8')) == 10)

hours = int(input('hours:'))
rate = int(input('rate per hour:'))

weekly_earning = hours * rate 

print(int(weekly_earning))

user_age = int(input('your actual age: '))

secods_lived = user_age*365*24*60*60

print('you have lived:',secods_lived,'seconds' )

print('1 ','1 ','1 ','1 ','1 ')
print('2 ','1 ','2 ','4 ','8 ')
print('3 ','1 ','3 ','9 ','27 ')
print('4 ','1 ','4 ','16 ','64 ')
print('5 ','1 ','5 ','25 ','125 ')