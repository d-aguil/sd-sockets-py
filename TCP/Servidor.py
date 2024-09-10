import socket
import argparse
import threading

class Servidor:
    def __init__(self, id, puerto):
        self.id = id
        self.puerto = puerto
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', self.puerto))
        self.socket.listen(5)  # Escuchar hasta 5 conexiones simultáneas

    def manejar_cliente(self, conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break  # Cliente cerró la conexión
                mensaje = data.decode()
                print(f"{self.id} recibí de {addr} --> {mensaje}")
            except Exception as e:
                print(f"{self.id}: Error al recibir mensaje: {e}")
        conn.close()

    def iniciar(self):
        print(f"{self.id} escuchando en el puerto {self.puerto}")
        while True:
            conn, addr = self.socket.accept()
            print(f"{self.id}: Conexión establecida desde {addr}")
            hilo_cliente = threading.Thread(target=self.manejar_cliente, args=(conn, addr))
            hilo_cliente.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Configuración del servidor')
    parser.add_argument('--id', required=True, help='Identificador único del servidor')
    parser.add_argument('--puerto', type=int, required=True, help='Puerto en el que escuchará el servidor')

    args = parser.parse_args()

    servidor = Servidor(args.id, args.puerto)
    servidor.iniciar()