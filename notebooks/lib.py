def help():
	print("helloworld() -> Escribe \"hello\"")
	print("basesDeDatos() -> Devuelve listado de bases de datos disponibles")
	print("query(db consulta) -> Recibe numero de base de datos y consulta SELECT y escribe resultado de query a la base de datos")

def helloworld():
	print ("hello")

def basesDeDatos():
	print ("1- Base de datos de Cesce")
	print ("2- Base de datos de Ejemplo1")
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