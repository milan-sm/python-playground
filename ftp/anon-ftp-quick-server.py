# Quick FTP Server for local machine/intranet
# Cancel after quick usage !!!!!!

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():    
    authorizer = DummyAuthorizer()    
    authorizer.add_anonymous(os.getcwd())
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    handler.banner = "Anon/Temp FTP Local Server"
    
    address = ('', 21)
    server = FTPServer(address, handler)

    server.max_cons = 2 #up to 256
    server.max_cons_per_ip = 5
    
    server.serve_forever()

if __name__ == '__main__':
    main()
