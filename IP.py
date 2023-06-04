import socket 
import whois
import time
import geocoder
import os
#import nmap
#from ipwhois import IPWhois

#Socket site: https://docs.python.org/3/library/socket.html

#The script is in development very likely not to be 100% sure in searches.
#I used Nmap to be more sure, in the searches of the open doors.

print(" ▄█▀▀▀█▄█ ▄▄█▀▀██▄   ▄▄█▀▀▀█▄█████▀ ▀███▀▀███▀▀▀██████▀▀██▀▀███")
print("▄██    ▀███▀    ▀██▄██▀     ▀█ ██   ▄█▀    ██    ▀██▀   ██   ▀█")
print("▀███▄   ██▀      ▀███▀       ▀ ██ ▄█▀      ██   █       ██     ")
print("  ▀█████▄█        ███          █████▄      ██████       ██     ")
print("▄     ▀███▄      ▄███▄         ██  ███     ██   █  ▄    ██     ")
print("██     ████▄    ▄██▀██▄     ▄▀ ██   ▀██▄   ██     ▄█    ██     ")
print("█▀█████▀  ▀▀████▀▀   ▀▀█████▀▄████▄   ███▄██████████  ▄████▄   ")
print('\n')
print('#############')
print('BY: ~#M?x')
print('GitHub:','https://github.com/suchsoak')
print('#############.\n')

print("Make sure you are an Administrator!!!\n")

print('Exemple: URL www.google.com or IP 127.154.25.6\t\n',)

Host = input(f'put the addres Host (IP ou URL): ')  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class ping_ns_():
    time.sleep(5.0)
    print("\n")
    print("*****************************\n")
    print("---------------------------\n")
    print('[!] Ping -n 4', Host)
    time.sleep(5.0)
    print('---------------------------\n')
    command = f"ping -n 4 {Host}"
    os.system(command)
    print("\n")
    print("*****************************\n")
    print('---------------------------\n')
    print('[!] Nslookup -type=mx', Host)
    print('---------------------------')
    time.sleep(5.0)
    command_2 = f"nslookup -type=mx {Host}"
    os.system(command_2)
    print("\n")
    print("*****************************\n")
    print('---------------------------\n')
    print('[!] Tracert -h 8', Host)
    print('---------------------------\n')
    time.sleep(5.0)
    command_2 = f"tracert -h 8 {Host}"
    os.system(command_2)
    print("\n")
    print("*************************\n")
    print('---------------------------\n')
    print('[!] pathping -h 4', Host)
    print('---------------------------\n')
    time.sleep(5.0)
    command_2 = f"pathping -p 5.0 -h 4 {Host}"
    os.system(command_2)
    print("\n")

g = geocoder.ip (Host)
go = geocoder.google (Host)

class quem_e():
    try:
        print('----------------------------------')
        print("Getting additional information...")
        time.sleep(5.0)
        whois_resultado = whois.whois(Host)
        ip = socket.gethostbyname(Host)
        sem_informacao = False

        print('--------------------------')
        print("[!] IP:", ip)
        print('--------------------------')
        print("[!] Postcode street:", go.postal)
        print('--------------------------')
        print("[!] Street:", go.street)
        print('--------------------------')
        print("[!] More information:", go.street_long)
        print('--------------------------')
        print('[!] house number:', go.housenumber)
        print('--------------------------')
        print('[!] city:', g.city)
        print('--------------------------')
        print("[!] Admin contact: ", whois_resultado.admin_contact)
        print('--------------------------')
        print("[!] tech contact: ", whois_resultado.tech_contact)
        print('--------------------------')
        print('[!] country: ', g.country)
        print('--------------------------')
        print("[!] lat: ", g.lat)
        print('--------------------------')
        print("[!] lng: ", g.lng)
        print('--------------------------')
        print("[!] Domain name:", whois_resultado.domain_name)
        print('--------------------------')
        print("[!] Creation date:", whois_resultado.creation_date)
        print('--------------------------')
        print("[!] Experation date:", whois_resultado.expiration_date)
        print('--------------------------')
        print("[!] Updated date:", whois_resultado.updated_date)
        print('--------------------------')
        print("[!] Status:", whois_resultado.status)
        print('--------------------------')
        print("[!] Name servers:", whois_resultado.name_servers)
        print('--------------------------')
        print("[!] Registrant:", whois_resultado.registrant)
        print('---------------------------------------------------------')
    except KeyboardInterrupt:
        print('program stopped')
    except Exception as erro:
        print('An error has occurred')
s.settimeout(15.0)
print('\n')
print("Getting ports...\n")
print('------------------\n')
service = socket.getservbyport

s.settimeout(15.0) 
nenhuma = True
 
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995]
class Portas:    
    time.sleep(6.0) 
    for port in ports:   
        resultado = s.connect_ex((Host, port))
        if resultado == 0:
            print('**************')
            print('[*] Scanning: ', Host)
            print('[*] Open: ', (port), (service(port)))
            print('**************')
            print('\t\n')  
            nenhuma = False #Se for encontrada não será exibido
    else:
        pass
        if nenhuma:
            print("Nenhuma Porta Encontrada Pelo Scanner Socket.")

class nmap():
    try:
        print('-----------------\t\n')
        print('For a scnner, more accurate...')
        print('-----------------')
        print('[!] Nmap -v -sV', Host)
        time.sleep(5.0)
        nmapscanner = f'nmap -v -sV {Host}'
        os.system(nmapscanner)  
        print('------------------\t\n')
        print('[!] Nmap -Pn', Host)
        print('\t\n')
        print('------------------')
        nmapscanner2 = f'nmap -Pn {Host}'
        os.system(nmapscanner2)
    except KeyboardInterrupt:
        print('program stopped')
    except Exception as erro:
        print('An error has occurred', erro)
