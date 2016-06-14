def help():
	print("helloworld()\n   -> Escribe \"helloworld\"\n")
	print("basesDeDatos()\n   -> Devuelve listado de bases de datos disponibles\n")
	print("query(db, \"consulta\")\n   -> Recibe numero de base de datos y consulta SELECT y escribe resultado de query a la base de datos\n")
	print("query(db, \"consulta\", posicionCampo)\n   -> Recibe numero de base de datos y consulta SELECT y posicion del campo y devuelve una lista con los valores del campo seleccionado (primera posicion es 0)\n")

def helloworld():
	print ("helloworld")

def basesDeDatos():
	print ("1- Base de datos de Cesce\n")
	print ("2- Base de datos de Ejemplo1\n")
	print ("3- Base de datos de Ejemplo2")
	
def query(db, consulta):
	import os
	os.system("pip install pygresql")
	import pg
	#Base de datos de Cesce (debe depender del param db que recibe)
	hostname = 'ec2-54-247-190-226.eu-west-1.compute.amazonaws.com'
	username = 'u3jk39shtaohhp'
	password = 'p5gvn36g2q076783i6s3j6hqqfq'
	database = 'dabdmj8rgg0lfa'
	conn = pg.DB(host=hostname, user=username, passwd=password, dbname=database)
	result = conn.query(consulta)
	print (result)
	conn.close()

def query(db, consulta, posicionCampo):
	import os
	os.system("pip install pygresql")
	import pg
	respuesta = []
	#Base de datos de Cesce (debe depender del param db que recibe)
	hostname = 'ec2-54-247-190-226.eu-west-1.compute.amazonaws.com'
	username = 'u3jk39shtaohhp'
	password = 'p5gvn36g2q076783i6s3j6hqqfq'
	database = 'dabdmj8rgg0lfa'
	conn = pg.DB(host=hostname, user=username, passwd=password, dbname=database)
	result = conn.query(consulta)
	for dato in result.getresult():
		resultado.append(dato[posicionCampo])
	print (result)
	conn.close()	
	return resultado