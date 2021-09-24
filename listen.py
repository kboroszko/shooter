import socket



def recv(c):
    buf = ''
    while '\n' not in buf:
        buf += c.recv(8).decode()
    return int(float(buf.split('\n')[0]))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 12345))

print("listening on port", 12345)

s.listen(10)

(c, addr) = s.accept()

print("connection from:", addr)

x = recv(c)
while x > 0:
    print(x)
    x = recv(c)


