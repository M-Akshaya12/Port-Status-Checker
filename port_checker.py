import socket

def check_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout after 2 seconds

        # Try connecting to the host and port
        result = sock.connect_ex((host, port))

        if result == 0:
            return f"Port {port} is OPEN on {host}"
        else:
            return f"Port {port} is CLOSED on {host}"

    except socket.gaierror:
        return "Hostname could not be resolved."
    except Exception as e:
        return f"Error: {e}"
    finally:
        sock.close()


# Main program
host = input("Enter hostname or IP address: ")
port = int(input("Enter port number to check: "))

status = check_port(host, port)
print(status)