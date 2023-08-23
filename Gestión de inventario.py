import json

products= []
sales = []
with open('data_inventary.json') as data_inv:
	products = json.load(data_inv)
with open('data_sales.json') as data_sales:
	sales = json.load(data_sales)

def add_product ():
	name = input('Escribe el nombre del producto: ')
	price = int(input('Escribe el precio del producto: '))
	quantity = int(input('Escribe la cantidad a añadir de este producto: '))
	description = input('Escribe una breve descripcion del producto: ')
	product = {'name':name,'price':price,'quantity':quantity, 'description': description}
	products.append(product)

def show_products() :
	if len(products) != 0:
		for e in products:
			name = e['name']
			price = e['price']
			quantity = e['quantity']
			description = e['description']
			print('')
			print(f'Nombre del producto: {name} ')
			print(f'Precio del producto: {price} ')
			print(f'Cantidad del producto: {quantity} ')
			print(f'Descripcion del producto: {description} ')
			print('')
	else:
		print('Todavia no hay productos en stock')
		
def update_product():
	# codigo para mostrar los nombres de los productos en inventario
	print('Los productos en inventario son:')
	products_name = []
	for e in products:
		name = e['name']
		products_name.append(name)
	show_names = ', '.join(products_name)
	print(show_names)
	print('')
	#codigo para actualizar el producto
	product_update = input('Introduce el nombre del producto que quieres actualizar (debe ser el nombre exacto): ')
	update = int(input('Escribe el numero correspondiente a la actualizacion que quieres hacer: 1- nombre, 2- precio, 3- cantidad, 4- descripcion ::'))
	if update == 1:
		try:
			index = products_name.index(product_update)
			new_name = input('Introduce el nuevo nombre: ')
			products[index]['name'] = new_name
			print('Actualizado correctamente')
		except:
			print('ese producto no existe')
	elif update == 2:
		try:
			index = products_name.index(product_update)
			new_price = int(input('Introduce el nuevo precio: '))
			products[index]['price'] = new_price
			print('Actualizado correctamente')
		except:
			print('ese producto no existe')
	elif update == 3:
		try:
			index = products_name.index(product_update)
			new_quatity = int(input('Introduce la nueva cantidad: '))
			products[index]['quatity'] = new_quatity
			print('Actualizado correctamente')
		except:
			print('ese producto no existe')
	elif update == 4:
		try:
			index = products_name.index(product_update)
			new_description = input('Introduce la nueva descripcion: ')
			products[index]['description'] = new_description
			print('Actualizado correctamente')
		except:
			print('ese producto no existe')

def search_product ():
	product_search = input('Escribe el nombre del producto que quieres buscar: ')
	res = False
	for e in products:
		if e['name'] == product_search:
			name = e['name']
			price = e['price']
			quantity = e['quantity']
			description = e['description']
			res = True #found
			print('')
			print(f'Nombre del producto: {name} ')
			print(f'Precio del producto: {price} ')
			print(f'Cantidad del producto: {quantity} ')
			print(f'Descripcion del producto: {description} ')
			print('')
	if res == False:
		print('Producto no encontrado')

def register_sale ():
	name = input('Nombre del producto vendido: ')
	res = False
	i = 0
	for e in products:
		if e['name'] == name:
			res = True
			quantity = int(input('Cantidad vendida: '))
			date = input('Fecha de venta: ')
			income = products[i]['price'] *quantity
			products[i]['quantity'] = products[i]['quantity'] - quantity
			sale = {'name': name, 'quantity': quantity, 'date': date, 'income': income}
			sales.append(sale)
		i += 1
	if res == False:
		print('Producto inexistente')
	
def sumary_sales ():
	for e in sales:
		name = e['name']
		income = e['income']
		quantity = e['quantity']
		date= e['date']
		print('')
		print(f'Nombre del producto: {name} ')
		print(f'Ingreso de venta: {income} ')
		print(f'Cantidad del producto vendida: {quantity} ')
		print(f'Fecha de venta: {date} ')
		print('')
	sumary_sale = len(sales)
	sumary_income = 0
	for e in sales:
		income_this = e['income']
		sumary_income += income_this
	print('')
	print(f'Cantidad de productos vendidos: {sumary_sale}')
	print(f'Ingreso total: {sumary_income}')

def save_data ():
	with open('data_inventary.json','w') as file_inv:
		data = json.dumps(products)
		file_inv.write(data)
	with open('data_sales.json','w') as file_sales:
		data = json.dumps(sales)
		file_sales.write(data)
	print('Datos guardados con exito')

def delete_product ():
	product_name = input('Ingresa el nombre del producto que quieres eliminar por completo: ')
	products_name = []
	for e in products:
		name = e['name']
		products_name.append(name)
	try:
		index = products_name.index(product_name)
		products.pop(index)
		print('Producto eliminado con exito')
	except:
		print('Ingresa un nombre de producto valido')

def menu ():
	print('BIENVENIDO AL GESTOR DE INVENTARIO')
	while True:
		print('Escibe el numero correspondiente a la accion que quieras realizar.')
		print('1- Añadir producto nuevo')
		print('2- Registrar una venta')
		print('3- Buscar informacion de un producto')
		print('4- Actualizar los detalles de un producto')
		print('5- Mostrar todos los productos en stock')
		print('6- Mostrar el resumen de las ventaz e ingreso')
		print('7- Eliminar un producto')
		print('8- Guardar y salir')
		res = int(input('----->  '))
		if res == 1:
			add_product()
		elif res == 2:
			register_sale()
		elif res == 3:
			search_product()
		elif res == 4:
			update_product()
		elif res == 5:
			show_products()
		elif res == 6:
			sumary_sales()
		elif res == 7:
			delete_product()
		elif res == 8:
			save_data()
			print('HASTA LUEGO')
			break
		else:
			print('Introduce una opcion correcta')
		
		
menu()