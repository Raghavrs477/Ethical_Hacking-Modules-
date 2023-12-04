import socket
import termcolor
def scan(target,ports):
        for ports in range(1,ports):
                scan_port(target,ports)
print('\n'+'start scan for'+ str('target'))

def scan_port(ipaddress,port):
        try:
                sock=socket.socket()
                sock.connect((ipaddress,port))
                print("[+] Port Opened"+str(port))
                sock.close()
        except:
                print("[+]Port Cloosed" +str(port))
target = input("[+] Enter target to scan(split by , ):")

ports=int(input("[+]Enter how many ports "))

if "," in target:
        print("[*]Scanning multiple targets ")




target = input("[+] Enter target to scan(split by , ):")

ports=int(input("[*]Enter how many ports "))

if "," in target:
        print("[*]Scanning multiple targets ")
        for ip_addr in target.split(','):
            scan(ip_addr.split(''),ports)
else:
        scan(target,ports)
