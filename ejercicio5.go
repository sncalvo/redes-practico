package main

func main() {
	master := socket.tcp()
	master.bind("12.12.12.128", 80)

	server, err := master.listen()

	if err != nil {
		return
	}

	for {
		client, err := server.accept()

		if err != nil {
			continue
		}

		go serveClient(client)
	}
}

func serveClient(client Socket) {
	defer client.close()

	received: string
	hostHeader: string
	for {
		data, err := client.receive()
		received += data

		if err == "closed" || hostHeader = getHttpHostHeader(received) {
			break
		}
	}

	if err != nil && err != "closed" {
		return
	}

	master := socket.tcp()
	ip: string
	switch hostHeader {
	case "http://www.serviciouno.uy/":
		ip = "192.168.128.1"
	case "http://www.serviciodos.uy/":
		ip = "192.168.128.2"
	default:
		client.send("POW") // client.send(BAD_REQUEST)
		return
	}

	destinationServer, err := master.connect(ip, 80)

	if err != nil {
		return
	}

	defer destinationServer.close()

	for receive != "" {
		remain, err := destinationServer.send(received)
		received = remain

		if err != nil {
			return
		}
	}

	go retransmit(client, destinationServer)
	go retransmit(destinationServer, client)
}


func retransmit(source Socket, destination Socket) {
	defer client.close()
	defer server.close()

	for {
		data, err := source.receive()

		for data != "" {
			remain, err := destination.send(data)
			data = remain

			if err {
				return
			}
		}
	}
}
