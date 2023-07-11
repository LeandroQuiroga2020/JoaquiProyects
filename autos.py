def calcular_precio(marca, puerta, color):  #entran los valores metidos a mano por el input
    marcas= {'Ford':100000, 'Chervrolet':120000,'Fiat':50000}
    puertas= {2:5000,4:7000,5:8000}
    colores= {'Blanco':10000, 'Azul':20000, 'Negro':3000}
    precio=marcas[marca]+puertas[puerta]+colores[color]
    return precio


mas_clientes= "si"
ventas=[]  #meto aca todas las ventas que tuve, array vacio

marcas = ["Ford","Chevrolet","Fiat"]
puertas = [2,4,5]
colores = ["Blanco","Azul","Negro"]

while mas_clientes == "si":
    nombre = input("Ingrese nombre : ")
    apellido = input("Ingrese apellido : ")
    marca = ""
    puerta =0
    color = ""

    while marca not in marcas:
        marca = input("Ingrese Marca : ")

    while puerta not in puertas:
        puerta = int(input('Ingrese Puerta :'))

    while color not in colores:
        color = input("Ingrese Color: ")

    precio= calcular_precio(marca,puerta,color)

    venta= {"nombre":nombre, "apellido":apellido, "marca":marca , "puertas":puerta, "color":color, "precio":precio} #diccionario
    ventas.append(venta) #lo agrego al array vacio

    mas_clientes = input("Hay mas cliente : ")

print(ventas)   #para ver lo que se va guardando en el diccionario

for i in ventas:
    print("La persona "+ i['nombre']+ i['apellido' ]+" compro un auto marca " + i['marca'] + 
          " con " + str(i['puertas'])+ " color "+ i['color'] + " a " + str(i['precio']) +"pesos")