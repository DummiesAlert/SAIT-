import socket

port = 35685
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (socket.gethostbyname('localhost'))
s.bind((addr, port))
s.listen(5)
print("[+] Server Listening . . .")

while True: 
    
    conn, addr = s.accept()
    print(f"Connection to {addr[0]} on {addr[1]}")
    conn.send(bytes("Socket Programming in Python", "utf-8 "))