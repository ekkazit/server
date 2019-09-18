import functools
import xmlrpc.client

HOST = 'localhost'
PORT = 8069
DB = 'demo'
USER = 'admin@mail.com'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print("Logged in as %s (uid:%d)" % (USER, uid))

# call statement
call = functools.partial(xmlrpc.client.ServerProxy(ROOT + 'object').execute, DB, uid, PASS)


# call search read
cars = call('tms.car', 'search_read', [])
for c in cars:
    print("Car ID=%s Name=%s" % (c['id'], c['name']))
