variable_types = ['camelCase', 'PascalCase', 'snake_case', 'kebab-case']; 

first_name = 'Matias'
last_name = 'Ferrari';
full_name = 'Matias Ferrari';
country = 'Argentina';
city = 'CABA';
age = 17;
year = 2024;
is_married = False;
is_true = False;
is_light_on = True;
num_one = 5;
num_two = 4;

pets_name , mothers_name , fathers_name, sibilings  = 'osito' , 'silvana', 'gabriel', 2; 


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print('my name has', len(first_name), 'letters and my last name has', len(last_name));

variable_total = (num_one + num_two);
print(variable_total);
variable_diff = (num_one - num_two);
print(variable_diff);
variable_product = (num_one * num_two);
print(variable_product); 
variable_division = (num_one / num_two);
print(variable_division); 
variable_remaider = (num_one % num_two);
print(variable_remaider);
variable_exp = (num_one ** num_two);
print(variable_exp);
variable_floor_division = (num_one // num_two);
print(variable_floor_division);

#The radius of a circle is 30 meters

area_of_circle = 3.14*(30**2); 
print(int(area_of_circle))

circunf_of_circle = 3.14*60; 
print(circunf_of_circle)

while True:
    radius = input('Radius of circle: ')
    if radius.isdigit(): 
        radius = int(radius)
        break
    else:
        print("Please enter a valid number.")

new_area_circle = 3.14 * (radius ** 2)
print(int(new_area_circle))

user_name = input('whats your name?:'); 
user_last_name = input('whats your last name?:'); 
user_country = input('where are you from?:');
user_age = input('how old are you?:');
