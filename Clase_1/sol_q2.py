# Aquí hay de dos sopas, vamos primero con la primer solución.
# Para esto vamos a necesitar una nueva variable que se llame
# tmp (temporal) y ahí vamos a guardar un valor para poder hacer
# el swap sin perder información 

a = [1,2,3]
b = [-1,-2,-3]

print('a = {}'.format(a))
print('b = {}'.format(b))

print('')
print('Aquí vamos a hacer el swap')

tmp = a 
a = b
b = tmp

print('a = {}'.format(a))
print('b = {}'.format(b))

print('')
print('Aquí iniciamos la versión 2')

# Ahora vamos a la segunda solución, igual de válida que la primera.
# Esta solución es llamada la solución pythonista y es que nos vamos
# a aprovechar de una habilidad de python que se llama descompresion
# de tuplas. 

a = [1,2,3]
b = [-1,-2,-3]

print('a = {}'.format(a))
print('b = {}'.format(b))

print('')
print('Aquí vamos a hacer el swap versión Pythonista')

a,b = b,a

print('a = {}'.format(a))
print('b = {}'.format(b))

# ¿Cómo te quedó el ojo? Más fácil de esta forma ¿No lo crees?