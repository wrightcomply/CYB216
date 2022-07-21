# from: https://mohamedaezzat.github.io/posts/portscanner/
# Python code snippet
import socket
from IPy import IP


def scan(target, port_num):
    converted_ip = check_ip(target)
    print('\n' + '[Scanning target...] ' + str(target))
    for port in range(1, port_num):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n').strip('\r')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass


# Python code snippet
if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan (split multiple targets with ,): ')
    port_number = int(input('[+] Enter number of ports you want to scan: '))
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '), port_number)
    else:
        scan(targets, port_number)
