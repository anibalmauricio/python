# Variables

# Como buena practica en python es utiliza snake case
my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_variable_to_string = str(my_int_variable)
print(type(my_int_variable_to_string))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de cadenas
print(type(print(my_variable, my_int_variable_to_string, my_bool_variable)))
print("Este es el valor de: ", my_variable)
# Algunas funciones del sistema
print(len(my_variable))

# Variables en una sola linea. !Cuidado con abusar de esta sintaxis¡
name, surname, alias, age = "Anibal", "Pacheco", 'Otro', 41
print("Me llamo:", name, surname, ". Mi alias es:", alias, "y tengo:", age, "años")

# Inputs 
"""
first_name = input('What is your name: ')
age = input('How old are you? ')
"""
name = 35
age = "Mauricio"
print(name)
print(age)

# Forzamos el tipo
"""
Aunque en este caso simplemente es para información, sin embargo se puede cambiar
"""
address: str = "Mi dirección"
address = 32
print(type(address))