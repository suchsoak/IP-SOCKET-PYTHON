import socket #Discover TCP/UDP
import argparse
import whois #Discover information on the internet
import time #Put the time in the script
import requests 
import sys #Stop Script
import geocoder #Discover geolocation
import os 
import colorama #Color in the script
from colorama import Fore, Style
from urllib.request import urlparse

clear = os.system("clear")

if clear == True:
    os.system("cls")
else:
    print("")

colorama.init() 
print(Fore.RED)

s1 = '''

  ██████     |
▒██    ▒     | BY: suchsoak
░ ▓██▄       | GitHub: https://github.com/suchsoak
  ▒   ██▒    | v:1.0.1
▒██████▒▒    |
▒ ▒▓▒ ▒ ░    |
░ ░▒  ░      |
░  ░  ░      |
      ░      |

'''

print(s1)
print("\n")

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url', help='url', dest='target')
parser.add_argument('-i', '--ip', help='ip', dest='target2')

args = parser.parse_args()

try: #IP information
    if args.target2:
        ip_info1 = args.target2
        info_ip1 = os.system(f'curl ipinfo.io/{args.target2}')
        if info_ip1 != 0:
            print("Error getting IP information.")
            sys.exit(1)
        else:
            sys.exit(0)

except KeyboardInterrupt:
    print("KeyboardInterrup")

try:
    if args.target:
        Host = args.target
    else:
        os.system("python3 ip.py -h") 
        sys.exit()

except KeyboardInterrupt:
     print("KeyboardInterrup")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(Style.RESET_ALL)

try:
    socket.inet_aton(Host)
    url = f'http://{Host}'
except socket.error:
    url = f'https://{Host}'
except Exception as b:
    print(b)

response = requests.get(url)

if response.status_code != '200':
    print('')
else:
    print('')
    
try:
    g = geocoder.ip (f'{Host}')
    if geocoder.google is not None:
        go = geocoder.google (f'{Host}')
except Exception as a:
    print(a)

class who():
    try:
        whois_resul = whois.whois(Host)
        ur = urlparse(url)
        if socket.gethostname is not None:
            ip = socket.gethostbyname(Host)
        print('-----------------------------------------------------------------------------------------------------------------------------------')

        if ip is not None:
            print(Fore.RED)
            print("[*] IP:", ip.rjust(70))
            print(Style.RESET_ALL)
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if response.status_code is not None:
            print("[*] Status Code:", str(response.status_code).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if response.encoding is not None:
            print("[*] Encoding:", str(response.encoding).rjust(75))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')
        
        if ur.scheme is not None:
            print("[*] Scheme:", str(ur.scheme).rjust(75))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')
                    
        if response.cookies is not None:
            print("[*] Cookies:", str(response.cookies).rjust(75))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.query is not None:
             print("[*] query:", str(whois_resul.query).rjust(75))
             print("")
             print('-----------------------------------------------------------------------------------------------------------------------------------')


        if go.postal is not None:
            print("[*] Postcode street:", str(go.postal).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if go.street is not None:
            print("[*] Street:", str(go.street).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if go.street_long is not None:
            print("[*] Stree Long:", str(go.street_long).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if go.housenumber is not None:
            print('[*] house number:', str(go.housenumber).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if g.city is not None:
            print('[*] city:', str(g.city).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if g.reverse is not None:
            print('[*] Reverse:', str(g.reverse).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')
            
        if whois_resul.admin_contact is not None:
            print("[*] Admin contact:", str(whois_resul.admin_contact).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.tech_contact is not None:
            print("[*] tech contact:", str(whois_resul.tech_contact).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if g.country is not None:
            print('[*] country:', str(g.country).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if g.lat is not None:
            print("[*] lat:", str(g.lat).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if g.lng is not None:
            print("[*] lng:", str(g.lng).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.domain_name is not None:
            print("[*] Domain name:", str(whois_resul.domain_name).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.updated_date is not None:
            print("[*] Updated date:", str(whois_resul.updated_date).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.registrant is not None:
            print("[*] Registrant:", str(whois_resul.registrant).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.creation_date is not None:
            print("[*] Creation date:", str(whois_resul.creation_date).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.name_servers is not None:
            print("[*] Name servers:", str(whois_resul.name_servers).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.expiration_date is not None:
            print("[*] Expiration date:", str(whois_resul.expiration_date).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if response.headers is not None:
            print("[*] Headers:", str(response.headers).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.date is not None:
            print("[*] Date:", str(whois_resul.date).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

        if whois_resul.status is not None:
            print("[*] Status:", str(whois_resul.status).rjust(70))
            print("")
            print('-----------------------------------------------------------------------------------------------------------------------------------')

    except KeyboardInterrupt:
        print('program stopped')
    except Exception as erro:
        print('An error has occurred')

s.settimeout(1)

print('\n')
print("Getting ports...\n")

service = socket.getservbyport

s.settimeout(1) 

no = True
 
#ports = [21, 22, 23, 25, 53, 80, 8080, 53, 110, 135, 139, 143, 70,  443, 445, 993, 995]

ports = range(1, 65535)

sleep = time.sleep
sleep(2)

class Ports: 
    try:
        for port in ports:   
            resultado = s.connect_ex((Host, port))
            sleep(2)
            if resultado == 0:
                    print('\t\n') 
                    print('[*] Open: ',(port), (service(port)).rjust(70))
                    print('\t\n') 
                    no = False
        else:
                pass
                if no:
                    print("No ports found.")

    except KeyboardInterrupt:
         print('program stopped')
    except Exception as err:
         print(err)   

