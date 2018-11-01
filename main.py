import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 
				'age', 
				'company', 
				'job']

clients = []


""" Cargar la informacion a memoria un 
desde el archivo formato CSV """
def _initialize_clients_from_storage():
	with open(CLIENT_TABLE, mode='r') as f:
		reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)


""" Guarda la informacion en un archivo
de formato CSV """
def _save_clients_to_storage():
	tmp_table = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table, mode='w') as f:
		write = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
		write.writerows(clients)

		os.remove(CLIENT_TABLE)
		os.rename(tmp_table, CLIENT_TABLE)


""" Guarda al cliente en la estructura de datos"""
def create_client(client):
	global clients
	if get_client_by_name(client.get('name')) == None:
		clients.append(client)
	else:
		print("Client already in the client's list")
	return clients


""" Actualiza la informacion de un cliente,
revice el id del cliente y los nuevos datos"""
def update_client(client_id, new_client):
	global clients
	
	if client_id != None:
		clients[client_id] =  new_client
		return clients
	else:
		print('Client not exist')


""" Lista todos los clientes"""
def list_client():
	global clients
	print('uuid | name | age | company | job')
	print("*"*40)
	for idx, client in enumerate(clients):		
		print('{uuid} | {name} | {age} | {company} | {job}'.format(
			uuid=idx,
			name=client['name'],
			age=client['age'],
			company=client['company'],
			job=client['job']
			)
		)


""" Elimina un cliente buscando por id"""
def delete_client(client_id):
	global clients
	if client_id != None:
		del clients[client_id]
	else:
		print('Client not exist')


""" Pregunta el nombre de un cliente y retorna
el id si lo encuentra o termia la ejecucion"""
def _get_client_index():
	global clients
	client_name =  None

	while not client_name:
		client_name = input('What is the name of the client? ')
		if client_name == 'exit':
			client_name = None
			break

	if not client_name:
		sys.exit()
	else:
		return get_client_by_name(client_name)
		

""" Recibe el nombre del cliente y obtiene el 
id """
def get_client_by_name(client_name):
	global clients
	for idx, client in enumerate(clients):
		if client.get('name') == client_name:
	 		return idx
	return None


""" Llena la estructura de datos del cliente"""
def get_client_field(field_name):
	client_data =  None

	while not client_data:
		client_data = input('What is the client {}? '.format(field_name))
		
	return client_data


""" Define y llena los datos del cliente"""
def get_client():
	client = {
		'name': get_client_field('name'),
		'age': get_client_field('age'),
		'company': get_client_field('company'),
		'job': get_client_field('job'),
	}
	return client


""" Imprime el mensaje de bienvenidos y las acciones
que se pueden realizar"""
def _print_welcom():
	print('Welcom to Vic vents')
	print('*'*50)
	print('What would you like to do today?')
	print('[C] Create a client')
	print('[D] Delete a client')
	print('[U] Update a client')
	print('[S] Search a client')
	print('[L] List  clients')



""" Funcion para inicalizar el programa"""
if __name__ == '__main__':
	_initialize_clients_from_storage()
	_print_welcom()

	acction = input()
	acction = acction.upper()

	if acction == 'C':
		client = get_client()
		create_client(client)
	elif acction == 'D':
		client_id = _get_client_index()
		delete_client(client_id)
	elif acction == 'U':
		client_id = _get_client_index()
		print('----------New Data----------')
		new_client = get_client()
		update_client(client_id, new_client)
	elif acction == 'S':
		client = _get_client_index()
		if client != None:
			print("Client exist")
		else:
			print("Client not exist")
	elif acction == 'L':
		list_client()
	else:
		print('The acction is unknown')

	_save_clients_to_storage()

