import psycopg2


def _get_session():
    try:
        conn = psycopg2.connect("dbname='CRM' user='postgres' host='localhost' password='root'")
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
