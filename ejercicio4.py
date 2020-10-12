def redirection(arg):
    origin_port, address, destination_port = args.split(':')
    master = socket.tcp()
    if address.is_domain():
        address = socket.gethostbyname(address)

    server = master.listen(address, origin_port)

    while True:
        client, err = server.accept()

        if err == None:
            threading.Thread(serve_client, args=(
                client, address, destination_port))


def serve_client(client, address, destination_port):
    master = socket.tcp()
    destination_client = master.connect(address, destination_port)

    while True:
        data, err = client.receive()

        if err != None:
            break

        destination_client.send(data)
        data, err = destination_client.receive()

        if err != None:
            break

        client.send(data)

    client.close()
    destination_client.close()
