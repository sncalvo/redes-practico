#
# El servidor espera conexiones TCP en todas sus interfaces en el puerto 8081.
#
# Los clientes envían dos tipos de mensajes:
# 1. ECHO: texto\n
# 2. EXIT\n
#
# Al recibir un mensaje de tipo ECHO el servidor debe contestar al cliente con texto.
#
# Al recibir un mensaje de tipo EXIT el servidor deberá contestarle “CLOSE ip_cliente” donde
# ip_cliente es la dirección IP del cliente que envió el comando y cerrar la conexión con dicho
# cliente.
#

class server:
    def serve_client(client):
        message_buffer = ""

        while True:
            message, error = client.recieve()

            if not error:
                message_buffer += message
                index = message.index_of('\n')

                # while there are more commands
                while index != -1:
                    command = message_buffer[0...index]
                    message_buffer = message_buffer[index+1...0]

                    if command.starts_with('ECHO'):
                        text = command.where_not('ECHO')  # inventado

                        client.send(text)
                    elif command.starts_with('EXIT'):
                        client.send('CLOSE {}'.format(client.getpeer()[0]))
                        break

                    index = message_buffer.index_of('\n')

        client.close()

    def __new__():
        master = socket.tcp()
        master.bind('*', 8081)

        server = master.listen()

        while True:
            client, error = server.accept()

            thread.new(serve_client, client) if not error


class client:
    def __new__():
        master = socket.tcp()
        master.bind(address, port)
        client, err = master.connect(address, port)
