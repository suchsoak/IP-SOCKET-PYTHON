import socket 
import whois
import time
import geocoder
import platform
import os
import colorama
from colorama import Fore, Style
#Socket site: https://docs.python.org/3/library/socket.html
#The script is in development very likely not to be 100% sure in searches.
colorama.init()
print(Fore.RED)
print("  ██████     |")
print("▒██    ▒     | BY: ~#M?x ")
print("░ ▓██▄       | GitHub: https://github.com/suchsoak")
print("  ▒   ██▒    | ")
print("▒██████▒▒    |")
print("▒ ▒▓▒ ▒ ░    |")
print("░ ░▒  ░      |")
print("░  ░  ░      |")
print("      ░      |")
print("\n")
Host = input(f'IP ou URL: ') 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(Style.RESET_ALL)

if platform.system() == 'Windows': 
        # time.sleep(5.0)
         print("\n")
         print("---------------------------\n")
         print('[!] Ping -n 4', Host)
         time.sleep(5.0)
         print('---------------------------\n')
         command = f"ping -n 4 {Host}"
         os.system(command)
elif platform.system() == 'Linux': 
        time.sleep(5.0)
        print("\n")
        print("*****************************\n")
        print("---------------------------\n")
        print('[!] Ping -c 4', Host)
        time.sleep(5.0)
        print('---------------------------\n')
        command = f"ping -c 4 {Host}"
        os.system(command)
elif platform.system() == 'Darwin':
        time.sleep(5.0)
        print("\n")
        print("*****************************\n")
        print("---------------------------\n")
        print('[!] Ping -c 4', Host)
        time.sleep(5.0)
        print('---------------------------\n')
        command = f"ping -c 4 {Host}"
        os.system(command)

else :
    print("operating system not supported.")
    
g = geocoder.ip (f'{Host}')
go = geocoder.google (f'{Host}')

class quem_e():
    try:
        print('----------------------------------')
        print("Getting additional information...")
        time.sleep(5.0)
        whois_resultado = whois.whois(Host)
        ip = socket.gethostbyname(Host)
        sem_informacao = False
        if ip is not None:
            colorama.init()
            print(Fore.RED)
            print('----------------------------------')
            print("[*] IP:", ip)
            print('----------------------------------')  
            print(Style.RESET_ALL)  
        if go.posta is not None:
            print("[*] Postcode street:", go.postal)
            print('----------------------------------')
        if go.street is not None:    
            print("[*] Street:", go.street)
            print('----------------------------------')
        if go.street_long is not None:
            print("[*] More information:", go.street_long)
            print('----------------------------------')
        if go.housenumber is not None:
            print('[*] house number:', go.housenumber)
            print('----------------------------------')
        if g.city is not None:
            print('[*] city:', g.city)
            print('----------------------------------')
        if whois_resultado.admin_contact is not None:
            print("[*] Admin contact: ", whois_resultado.admin_contact)
            print('----------------------------------')
        if whois_resultado.tech_contact is not None:
            print("[*] tech contact: ", whois_resultado.tech_contact)
            print('----------------------------------')
        if g.country is not None:
            print('[*] country: ', g.country)
            print('----------------------------------')
        if g.lat is not None:
            print("[*] lat: ", g.lat)
            print('----------------------------------')
        if g.lng is not None:
            print("[*] lng: ", g.lng)
            print('----------------------------------')
        if whois_resultado.domain_name is not None:
            print("[*] Domain name:", whois_resultado.domain_name)
            print('----------------------------------')
        if whois_resultado.creation_date is not None:
            print("[*] Creation date:", whois_resultado.creation_date)
            print('----------------------------------')
        if whois_resultado.expiration_date is not None:
            print("[*] Experation date:", whois_resultado.expiration_date)
            print('----------------------------------')
        if whois_resultado.updated_date is not None:
            print("[*] Updated date:", whois_resultado.updated_date)
            print('----------------------------------')
        if whois_resultado.status is not None:
            print("[*] Status:", whois_resultado.status)
            print('----------------------------------')
        if whois_resultado.name_servers is not None:
            print("[*] Name servers:", whois_resultado.name_servers)
            print('----------------------------------')
        if whois_resultado.registrant is not None:
            print("[*] Registrant:", whois_resultado.registrant)
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
no = True
 
#ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995]
ports = range(1, 65535)
class Portas: 
    try:
        time.sleep(6.0) 
        for port in ports:   
            resultado = s.connect_ex((Host, port))
            if resultado == 0:
                    print('||')
                    print('[*] Open: ', (port), (service(port)))
                    print('||')
                    print('\t\n') 
                    no = False
        else:
                pass
                if no:
                    print("No ports found.")
    except KeyboardInterrupt:
         print('program stopped')
    except Exception as erro:
         print(erro)              
