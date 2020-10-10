class Socket:
    buffer_input: string = 'line1'

    def read_line(self, timeout):
        timeout_remaining = timeout
        index = buffer_input.index_of('\n')

        while index == -1:
            if (timeout_remaining <= 0 and timeout != -1) or (timeout_remaining < 0 and timeout == 0):
                return ('', 'timeout')

            self.settimeout(timeout_remaining)
            before_receive = time.now()

            result, error = client.receive()

            timeout_remaining = timeout_remaining - \
                (time.now() - before_receive)

            return ('', error) if error == 'timeout'

            return (nil, error) if error

            buffer_input += result

            index = buffer_input.index_of('\n')

        line = buffer_input[0...index]
        buffer_input = buffer_input[index+1...]

        return line
