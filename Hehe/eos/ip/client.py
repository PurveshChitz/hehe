import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
host = socket.gethostname()
port = 12348
print "CONNECTING ......"
s.connect(('192.168.1.3', port))
me = raw_input('ROHAN : ')
s.sendall(me)
server = s.recv(200)
print 'SERVER :',server
s.close()



dil ayya gadhi pe to pari kya cheez ayya...
