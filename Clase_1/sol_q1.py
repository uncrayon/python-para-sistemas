# Calcula el volumen de la célula usando lo siguiente:
d = 9.7 #µm, Diamétro en promedio
pi = 3.1416 #Más o menos es esto

# Paso 1, crea una variable que se llame radio y asignale el valor del radio partiendo del diámetro

radio = d / 2

# Paso 2, crea una variable que se llame volumen y guarda ahí el valor usando la relación que se presentó para el volumen

V = (4/3)*pi*(radio**2)

# No olvides devolver el resultado

print('El volumen son {:.2f} µm^3'.format(V))