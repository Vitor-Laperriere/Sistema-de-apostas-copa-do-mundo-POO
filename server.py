import socket
import threading
from servidor.aviao import Aviao

def bool_to_data(poltronas):
    res = ""
    for poltrona in poltronas:
        res += "L" if poltrona else "O"

    return res

def data_2_poltronas(data):
    return [int(x) for x in data.split(' ')]

def list_to_data(retorno):
    res = ""
    for valor in retorno:
        res += "1" if valor else "0"

    return res

def server_thread(conn, address, identificador, aviao):
    data = conn.send(bool_to_data(aviao.livres()).encode())

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        data = str(data)
        print(f"from {identificador}: {data}")
        if data[0] == '0':
            data = bool_to_data(aviao.livres()).encode()
        if data[0] == '1':
            data = list_to_data(aviao.reserva(data_2_poltronas(data[1:]), identificador)).encode()
        if data[0] == '2':
            break
        
        conn.send(data)  # send data to the client
    conn.close()  # close the connection

def server_program():
    aviao = Aviao()
    
    # get the hostname
    host = socket.gethostname()
    port = 5400  # initiate port no above 1024
    
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    
    try:
       # configure how many client the server can listen simultaneously
       server_socket.listen(10)
       identificador = 1
       while True:
           conn, address = server_socket.accept()  # accept new connection
           print("Connection from: " + str(address))
           new_thread = threading.Thread(target = server_thread, args=(conn, address, identificador, aviao))
           new_thread.start()
           identificador += 1
    finally:
        server_socket.shutdown(socket.SHUT_RDWR)

if __name__ == '__main__':
    server_program()
