void sevidor()
{
    int master = socket.tcp();
    master.bind(*, 8081);
    serverSock = master.listen();
    while (true)
    {
        clientSock, err = serverSock.accept(); //espero conexiones
        if (err)
            break;
        thread.create(atenderCliente, clientSock); //hilo de atención para
        el cliente
    }
    serverSock.close();
}

void atenderCliente(clientSock)
{
    exit = false;
    while (!exit)
    {
        command = "";
        do
        {
            data, err = clientSock.receive(); //recibo el stream del cliente
            command += data;
        } while (!((err == "closed") || (find(command, '\n'))) //recibí el

        if (err == "closed" || data = "") {
            clientSock.close();
            return;
        }
        //Armo la respuesta dependiendo del comando
        if (find(command, 'ECHO')) {
            stream = remove(command, "ECHO")
        } else {
            ip, port = clientSock.getPeer();
            stream = "CLOSE " + ip;
            exit = true;
        }

        do
        {
            remain, err = clientSock.send(stream)

                              if (err == "closed")
            {
                clientSock.close();
                return;
            }

            stream = remain;
        } while (!remain == "")
    }

    clientSock.close();
}

void cliente()
{
    int master = socket.tcp();
    client, err = master.connect(IP_SERVER, 8081);
    msg[1] = "ECHO texto a replicar ….\n";
    msg[2] = "EXIT \n";
    if (!(client, err == NULL, failure))
    {
        for (i = 1 to i = 2)
        {
            stream = msg[i];
            remain = "";
            do
            {
                remain, err = client.send(stream);
                if (err == "closed")
                    client.close();
                return;
                stream = remain;
            } while (remain != "");

            do
            {
                data, err = client.receive();
                respuesta += data;
            }
            while (!(err == "closed" || find(respuesta, '\n')) //recibí
        }
    }
    client.close();
}
