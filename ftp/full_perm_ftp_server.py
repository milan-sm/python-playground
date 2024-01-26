# Quick FTP server with username/s for local machine/intranet download
# Cancel after quick usage ! - Do not use on open Internet !

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():    
    authorizer = DummyAuthorizer()

    # Full perm user !
    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    handler.banner = "Cancel after usage !!!!!!"
    
    address = ('', 21)
    server = FTPServer(address, handler)
    
    server.max_cons = 2 #max256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
