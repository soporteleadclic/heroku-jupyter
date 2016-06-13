def helloworld():
	print ("hello")
   
def query(consulta):
	os.system("pip install pygresql")
	import pg
	#Base de datos de Cesce
	hostname = 'ec2-54-247-190-226.eu-west-1.compute.amazonaws.com'
	username = 'u3jk39shtaohhp'
	password = 'p5gvn36g2q076783i6s3j6hqqfq'
	database = 'dabdmj8rgg0lfa'
	conn = pg.DB(host=hostname, user=username, passwd=password, dbname=database)

	result = conn.query(consulta)
	print (result)
	
	#print ("Nombre de la tabla")
	#for i in result.getresult() :
	#	print (i[1])#+"\t****\t"+i[2])
	conn.close()