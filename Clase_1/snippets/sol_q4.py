# Esta es la solución del problema: 

dulces_alicia = 121
dulces_roberto = 77
dulces_carolina = 109

por_destruir = (dulces_alicia+dulces_roberto+dulces_carolina)- 3*((dulces_carolina+dulces_roberto+dulces_alicia)//3)

print('Se destruirán {} dulces'.format(por_destruir))