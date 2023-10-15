# Copyright 2023 suchsoak

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import socket 
import whois
import time
import requests
import geocoder
import colorama
from colorama import Fore, Style

colorama.init()

s1 = '''

  ██████     |
▒██    ▒     | BY: ~#M?x 
░ ▓██▄       | GitHub: https://github.com/suchsoak
  ▒   ██▒    | v:1.0.2
▒██████▒▒    |
▒ ▒▓▒ ▒ ░    |
░ ░▒  ░      |
░  ░  ░      |
      ░      |

'''

print(s1)
print("\n")
Host = input(f'IP or URL: ') 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(Style.RESET_ALL)

try:
    socket.inet_aton(Host)
    url = f'http://{Host}'
except socket.error:
    url = f'https://{Host}'

response = requests.get(url)

g = geocoder.ip (f'{Host}')
go = geocoder.google (f'{Host}')

class who():
    try:
        print('-----------------------------------------------------------------------------------------------------------------------------------')
        time.sleep(3.0)
        whois_resul = whois.whois(Host)
        ip = socket.gethostbyname(Host)
        sem_informacao = False
        if ip is not None:
            print(Fore.RED)
            print("[*] IP:", ip.rjust(80))
            print(Style.RESET_ALL)
            print("")

        if response.status_code is not None:
            print("[*] Status Code:", str(response.status_code).rjust(70))
            print("")

        if response.encoding is not None:
            print("[*] Encoding:", str(response.encoding).rjust(75))
            print("")

        if go.postal is not None:
            print("[*] Postcode street:", str(go.postal).rjust(70))
            print("")

        if go.street is not None:
            print("[*] Street:", str(go.street).rjust(70))
            print("")

        if go.street_long is not None:
            print("[*] Stree Long:", str(go.street_long).rjust(70))
            print("")

        if go.housenumber is not None:
            print('[*] house number:', str(go.housenumber).rjust(70))
            print("")

        if g.city is not None:
            print('[*] city:', str(g.city).rjust(70))
            print("")

        if whois_resul.admin_contact is not None:
            print("[*] Admin contact:", str(whois_resul.admin_contact).rjust(70))
            print("")

        if whois_resul.tech_contact is not None:
            print("[*] tech contact:", str(whois_resul.tech_contact).rjust(70))
            print("")

        if g.country is not None:
            print('[*] country:', str(g.country).rjust(70))
            print("")

        if g.lat is not None:
            print("[*] lat:", str(g.lat).rjust(70))
            print("")

        if g.lng is not None:
            print("[*] lng:", str(g.lng).rjust(70))
            print("")

        if whois_resul.domain_name is not None:
            print("[*] Domain name:", str(whois_resul.domain_name).rjust(75))
            print("")

        if whois_resul.updated_date is not None:
            print("[*] Updated date:", str(whois_resul.updated_date).rjust(75))
            print("")

        if whois_resul.registrant is not None:
            print("[*] Registrant:", str(whois_resul.registrant).rjust(70))
            print("")

        if whois_resul.creation_date is not None:
            print("[*] Creation date:", str(whois_resul.creation_date).rjust(70))
            print("")

        if whois_resul.name_servers is not None:
            print("[*] Name servers:", str(whois_resul.name_servers).rjust(70))
            print("")

        if whois_resul.expiration_date is not None:
            print("[*] Expiration date:", str(whois_resul.expiration_date).rjust(70))
            print("")

        if response.headers is not None:
            print("[*] Headers:", str(response.headers).rjust(70))
            print("")

        if whois_resul.status is not None:
            print("[*] Status:", str(whois_resul.status).rjust(70))
            print("")
        print('-----------------------------------------------------------------------------------------------------------------------------------')

    except KeyboardInterrupt:
        print('program stopped')
    except Exception as erro:
        print('An error has occurred')

s.settimeout(15.0)
print('\n')
print("Getting ports...\n")
service = socket.getservbyport

s.settimeout(15.0) 

no = True
 
#ports = [21, 22, 23, 25, 53, 80, 8080, 53, 110, 135, 139, 143, 70,  443, 445, 993, 995]

ports = range(1, 65535)

class Portas: 
    try:
        time.sleep(3.0) 
        for port in ports:   
            resultado = s.connect_ex((Host, port))
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
    except Exception as erro:
         print(erro)   
