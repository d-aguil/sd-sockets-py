import socket
import argparse
import threading

class Servidor:
    def __init__(self, id, puerto):
        self.id = id
        self.puerto = puerto
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', self.puerto))

    def escuchar_mensajes(self):
        while True:
            try:
                data, addr = self.socket.recvfrom(1024)
                mensaje = data.decode()
                print(f"{self.id} recibí de {addr} --> {mensaje}")
            except Exception as e:
                print(f"{self.id}: Error al recibir mensaje: {e}")

    def iniciar(self):
        hilo_escucha = threading.Thread(target=self.escuchar_mensajes)
        hilo_escucha.daemon = True
        hilo_escucha.start()

        print(f"{self.id} escuchando en el puerto {self.puerto}")
        hilo_escucha.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Configuración del servidor')
    parser.add_argument('--id', required=True, help='Identificador único del servidor')
    parser.add_argument('--puerto', type=int, required=True, help='Puerto en el que escuchará el servidor')

    args = parser.parse_args()

    servidor = Servidor(args.id, args.puerto)
    servidor.iniciar()