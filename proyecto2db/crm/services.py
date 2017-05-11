import psycopg2


def _get_session():
    try:
        conn = psycopg2.connect("host='localhost' dbname='Medicos' user='postgres' password='Manzanar0j4'")
    except:
        print "I am unable to connect to the database"
        return 'error'

    return conn.cursor()

def insert_client(nombre, tipo, phone, url, email, addr, city, netvalue, clientsince, twitteracct, pic):
    cur = _get_session()
    query= 'INSERT INTO Clientes (id_cliente, nombre, cliente_type, telefono, sitio_web, correo_electronico, direccion, ciudad, valor_net, cliente_desde, twitter_acct, foto) VALUES (nextval(val_id_cliente),"%s","%d","%s","%s","%s","%s","%s","%d","%s","%s","%s");'%(name,tipo,phone,url,email,addr,city,netvalue,clientsince,twitteracct,pic)
    cur.execute(query)


def update_client(campos[], oldVals[], newVals[]):
    cur = _get_session()
    for i in campos[]:
        query= 'UPDATE Clientes SET %s = "%s" WHERE %s = "%s";'%(campos[i], newVals[i],campos[i],oldVals[i])
        cur.execute(query)

def delete_client(id):
    cur = _get_session()
    query = 'DELETE FROM Clientes WHERE id_cliente="%s";'%(id)
    cur.execute(query)

def triggerE1():
	cur = _get_session()
	query1 = 'CREATE TRIGGER E1 AFTER DELETE ON aseguradora FOR EACH ROW BEGIN UPDATE cliente SET id_aseguradora = 0 WHERE id_aseguradora = null END;' 
	query2 = 'CREATE TRIGGER E2 AFTER UPDATE OF ID_aseguradora ON aseguradora FOR EACH ROW BEGIN UPDATE cliente SET ID_aseguradora = NEW.id WHERE ID_aseguradora = OLD.id;'
	cur.execute(query1)
	cur.execute(query2)
	