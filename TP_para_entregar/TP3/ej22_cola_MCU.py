# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
from cola import Cola;

MCU = [
    {'nombre':'Tony Stark', 'superheroe':'Iron Man', 'genero':'Masc'},
    {'nombre':'Steve Rogers', 'superheroe':'Capitan América', 'genero':'Masc'},
    {'nombre':'Natasha Romanoff', 'superheroe':'Black Widow', 'genero':'Fem'},
    {'nombre':'Peter Parker', 'superheroe':'Spiderman', 'genero':'Masc'},
    {'nombre':'Profesor Hulk', 'superheroe':'Hulk', 'genero':'Masc'},
    {'nombre':'Carol Danvers', 'superheroe':'Capitana Marvel', 'genero':'Fem'},
    {'nombre':'Scott Lang', 'superheroe':'AntMan', 'genero':'Masc'},
]

cola = Cola()

for i in range(len(MCU)):
    value = MCU[i]
    cola.arrive(value)

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
print ('a. determinar el nombre del personaje de la superhéroe Capitana Marvel;')
def nombre_capitana(datos):
    cont = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['superheroe'] == 'Capitana Marvel':
            print('el nombre de la capitana marvel es: ', value['nombre'])
        cont +=1
nombre_capitana(cola)
print()
# b. mostrar los nombre de los superhéroes femeninos;
print('b. mostrar los nombre de los superhéroes femeninos;')
def superfem(datos):
    cont = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['genero'] == 'Fem':
            print('Nombre: ',value['nombre'], 'Superheroina: ',value['superheroe'])
        cont += 1
superfem(cola)
print()
# c. mostrar los nombres de los personajes masculinos;  
print ('c. mostrar los nombres de los personajes masculinos; ')      
def supermasc(datos):
    cont = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['genero'] == 'Masc':
            print('Nombre: ',value['nombre'])
        cont += 1
supermasc(cola)
print()
# d. determinar el nombre del superhéroe del personaje Scott Lang;
print ('d. determinar el nombre del superhéroe del personaje Scott Lang;')
def nombre_scott(datos):
    cont = 0
    cont2 = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['nombre'] == 'Scott Lang':
            cont2 +=1
            print('el nombre del superheroe es: ', value['superheroe'])       
        cont +=1   
    if cont2 == 0:
        print('no se encontro el personaje')
nombre_scott(cola)
print()
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
print ('e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;')
def superS(datos):
    cont = 0
    total = cola.size()
    print('Personajes o Superheroes que su nombre comienza con S')
    while cont < total:
        value = datos.move_to_end()
        nombre = value['nombre']
        personaje = value['superheroe']
        genero = value['genero']
        if (nombre[0] == 'S') or (personaje[0] == 'S'):
            print(f'Nombre: {nombre}, Personaje: {personaje}, Genero: {genero}') 
        cont +=1
superS (cola)
print()
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
print ('f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.')
def existe_Carol(datos):
    cont = 0
    total = cola.size()
    while cont < total:
        value = datos.move_to_end()
        if value['nombre'] == 'Carol Danvers':
            print('se encontro Carol Danvers, es: ', value['superheroe'])
        cont +=1

existe_Carol(cola)

