# protocolo ceroconf
# broadcast udp puerto 1234 'nombre_de_servicio\n numbero_de_puerto\n'

class Service:
    name: string
    ip: number
    port: number


services: [Service] = []


def video_capture():
    skt = socket.udp()
    skt.bind(*, 1234)

    while True:
        datagram = ""
        ip = ""
        while True:
            recieived, ip, port = skt.receive(-1)

            datagram += recieived
            length = datagram.count('\n')
            if length >= 2:
                break

        index = datagram.find('\n', 2)
        service = Service(datagram[:index], ip)

        datagram = datagram[index:]

        if not services.contains(service):
            if service.name == "tcp_cam":
                threading.Thread(target=read_stream, args=(service))
                services.append(service)


def read_stream(service):
    master = socket.tcp()
    client, err = master.connect(service.ip, service.port)

    if err != None:
        return

    stream_file = open("{}_{}.video".format(service.ip, service.port))

    while True:
        data, err = client.receive()

        if err != None:
            client.close()
            stream_file.close()
            services.remove(service)
            return

        stream_file.write(data)


def tcp_cam():
    threading.Thread(announcements)
    threading.Thread(listen_tcp)


def announcements():
    skt = skt.udp()

    while True:
        skt.send(("255.255.255.255", 1234),
                 "{}\n{}\n".format("tcp_cam", my_port))
        time.sleep(30)


def listen_tcp():
    master = skt.tcp()
    master.bind(*, my_port)

    server = master.listen()

    while True:
        client, err = server.accept()

        if err == None:
            threading.Thread(tcp_share, args=(client))


def tcp_share(client):
    video_feed = open("/dev/video0")

    while True:
        remaining = video_feed.read()

        while remaining != "":
            remaining, err = client.send(remaining)

            if err != None:
                client.close()
                return
