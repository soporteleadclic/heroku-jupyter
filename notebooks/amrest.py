import pg
import pandas

def sql( query ):
    hostname = 'ec2-79-125-113-131.eu-west-1.compute.amazonaws.com'
    database = 'dbn84cdh4hn9i3'
    username = 'uaan3afjlla7qq'
    password = 'p3ko2sredkqvnpcennou713esuh'
    cnn = pg.DB( host=hostname, user=username, passwd=password, dbname=database )
    result = cnn.query( query )
    cnn.close()
    return( result )

def tables( ):
    result = sql( "SELECT schemaName AS schema, tableName AS table FROM pg_catalog.pg_tables WHERE tableOwner = 'uaan3afjlla7qq' ORDER BY schemaName, tableName" )
    return( result )

