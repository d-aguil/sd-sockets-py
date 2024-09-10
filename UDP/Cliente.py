import socket
import argparse

class Cliente:
    def __init__(self, id, mensaje, host, destinos):
        self.id = id
        self.mensaje = mensaje
        self.destinos = destinos
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def enviar_mensaje(self, mensaje,host, puerto_destino):
        try:
            self.socket.sendto(mensaje.encode(), (host, puerto_destino))
            print(f"{self.id}: Mensaje enviado a puerto {puerto_destino}")
        except Exception as e:
            print(f"{self.id}: Error al enviar mensaje a puerto {puerto_destino}: {e}")

    def iniciar(self):
        for puerto_destino in self.destinos:
            self.enviar_mensaje(self.mensaje, self.host, puerto_destino)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Configuración del cliente')
    parser.add_argument('--id', required=True, help='Identificador único del cliente')
    parser.add_argument('--mensaje', required=True, help='Mensaje a enviar')
    parser.add_argument('--host', type=str, default='localhost', help='Host destino')
    parser.add_argument('--destinos', type=int, nargs='+', required=True, help='Lista de puertos a los que enviar mensajes')

    args = parser.parse_args()

    cliente = Cliente(args.id, args.mensaje, args.host, args.destinos)
    cliente.iniciar()