class IStdin:
    '''
    An interface that fits both a socket and a regular stdin.
    You should only use methods that are typed on this class.
    '''
    def readline(self) -> str:
        '''
        Reads a line of the input and returns it as a string.
        To avoid inconsistencies with whitespace, you should
        always strip newlines from the result as so:
        line = stdin.readline().strip('\n')
        '''
        pass

class IStdout:
    '''
    An interface that fits both a socket and a regular stdout.
    You should only use methods that are typed on this class.
    '''
    def write(self, message: str) -> None:
        '''
        Writes a message to the output as-is. if you want
        to write a newline after the string, include it in
        the message.
        '''
        pass

    def flush(self) -> None:
        '''
        Flushes the stdout -- for occasions where you want
        to force-send an output without sending a newline.
        '''
        pass
