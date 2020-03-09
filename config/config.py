# CTFNC_PORT is the port that ctf-nc will use when running in production.
CTFNC_PORT = 9001

# CTFNC_BIND is the address that the socket will bind to. By default, it
# binds to 0.0.0.0, accepting all incoming connections. If you want to
# accept connections from only a subnet, you should change this.
CTFNC_BIND = '0.0.0.0'

# CTFNC_MAX_CONN is the maximum amount of simultaneous connections that
# CTFNC will process before putting other connections into a queue.
# This is to avoid the process launching too many threads.
# Change this to 0 to use python's default of min(32, os.cpu_count + 4).
CTFNC_MAX_CONN = 10
