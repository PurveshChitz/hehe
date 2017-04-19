import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP) #create tcp/ip socket Address family types.,Socket types.
host = socket.gethostname()
port = 12348
s.bind(('',port))
s.listen(5)
while (True) :
        new_s, addr=s.accept() #connection and address
        print 'Got connection from proxy....sending data...'
        user = new_s.recv(200)
        print 'User : ',user
        new_s.send('CONNECTION WAS SUCCESSFULL....')
s.close()
new_s.close()

