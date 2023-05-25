import socket 
import whois
import time
import geocoder
import os
#import nmap
#from ipwhois import IPWhois

#Site do socket: https://docs.python.org/3/library/socket.html

#O Script Está Em Desenvolvimento Muito Provavel Que Não Seja 100% Certeza Nas Buscas.
#Utilizei O Nmap Para Ter Mais Certeza, Nas Buscas Das Portas Abertas.



print('▌║█║▌│║▌│║▌║▌█║SOCKET▌│║▌║▌│║║▌█║▌║█\n')
print('#############')
print('BY: ~#M?x')
print('GitHub:','https://github.com/suchsoak')
print('#############.\n')


#	whois     sibilo     traceroute     mtr     dns   

# ports = range(1, 8080) #Portas De 1 A 65536, caso queria mudar os numeros pode.

#caso queria colocar em formato de lista, utilize [] ao invés de range (). Nesse conceito coloque ports = [20,30,80,8080]


if KeyboardInterrupt == True:
    print('Programa Interrompido')

print("Certifique-se que está como Administrador!!!\n")

print('Exemplo: URL www.google.com or IP 127.154.25.6\t\n',)

Host = input(f'Coloqueo o Endereço Host (IP ou URL): ') #Colocar o Endereço de IP ou URL 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

#Colocar Vpn Para Um Melhor Anonimato
# try:
#         print('')
# except Exception as erro:
#     print(erro)
#     if KeyError == True:
#         print('[*] Erro de sintase', KeyError())
#     print(TypeError())

# class vpn():
#     print('\n')
#     print("****************************\n")
#     print("--------------------------")
#     print('[*] ')

class ping_ns_():
    time.sleep(5.0)
    print("\n")
    print("*****************************\n")
    print("---------------------------\n")
    print('[*] Ping -n 4', Host)
    time.sleep(5.0)
    print('---------------------------\n')
    command = f"ping -n 4 {Host}"
    os.system(command)
    print("\n")
    print("*****************************\n")
    print('---------------------------\n')
    print('[*] Nslookup -type=mx', Host)
    print('---------------------------')
    time.sleep(5.0)
    command_2 = f"nslookup -type=mx {Host}"
    os.system(command_2)
    print("\n")
    print("*****************************\n")
    print('---------------------------\n')
    print('[*] Tracert -h 8', Host)
    print('---------------------------\n')
    time.sleep(5.0)
    command_2 = f"tracert -h 8 {Host}"
    os.system(command_2)
    print("\n")
    print("*************************\n")
    print('---------------------------\n')
    print('[*] pathping -h 4', Host)
    print('---------------------------\n')
    time.sleep(5.0)
    command_2 = f"pathping -p 5.0 -h 4 {Host}"
    os.system(command_2)
    print("\n")

# host = input('Coloque o IP ou URL: ')
# command = f"ping -c 4 {host}"
# os.system(command)


# ip  177.137.4.253


g = geocoder.ip (Host)
go = geocoder.google (Host)


#ip_whois = IPWhois(Host)
#result = ip_whois.lookup_rdap()
#Obtendo informacoes com o whois sobre o ip ou site.
class quem_e():
    print('----------------------------------')
    print("Obtendo informações adicionais...")
    time.sleep(5.0)
    whois_resultado = whois.whois(Host)
    ip = socket.gethostbyname(Host)
    sem_informacao = False

    print('--------------------------')
    print("[*] IP:", ip)
    print('--------------------------')
    print("[*] Codigo Postal:", go.postal)
    print('--------------------------')
    print("[*] Rua:", go.street)
    print('--------------------------')
    print("[*] Rua mais informação:", go.street_long)
    print('--------------------------')
    print('[*] Numero da casa:', go.housenumber)
    print('--------------------------')
    print('[*] Cidade:', g.city)
    print('--------------------------')
    print("[*] Contato administrativo: ", whois_resultado.admin_contact)
    print('--------------------------')
    print("[*] Contato técnico: ", whois_resultado.tech_contact)
    print('--------------------------')
    print('[*] País: ', g.country)
    print('--------------------------')
    print("[*] Longitude: ", g.lat)
    print('--------------------------')
    print("[*] Latitude: ", g.lng)
    print('--------------------------')
    print("[*] Nome do Dominio:", whois_resultado.domain_name)
    print('--------------------------')
    print("[*] Data de Criação:", whois_resultado.creation_date)
    print('--------------------------')
    print("[*] Data de Expiração:", whois_resultado.expiration_date)
    print('--------------------------')
    print("[*] Data Atulizada:", whois_resultado.updated_date)
    print('--------------------------')
    print("[*] Status do Dominio:", whois_resultado.status)
    print('--------------------------')
    print("[*] Servidor de Nomes:", whois_resultado.name_servers)
    print('--------------------------')
    print("[*] Registro:", whois_resultado.registrant)
    print('---------------------------------------------------------')
    
s.settimeout(15.0)
print('\n')
print("Obtendo Portas...\n")
print('------------------\n')
service = socket.getservbyport

s.settimeout(15.0) #Esperar 15 segundos, para analisar as portas uma de cada
nenhuma = True
 #caso nenhuma porta seja encontrada


ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995]
class Portas:    #Usei o class para deixar o codigo mais organizado
    time.sleep(6.0) 
    for port in ports:   #Loop, podendo também utilizar o while. Porém, em meu caso utilizei for.
        resultado = s.connect_ex((Host, port))
        if resultado == 0:
            print('**************')
            print('[*] Scaneado: ', Host)
            print('[*] Abertas: ', (port), (service(port)))
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
        print('Para um scanner, Mais preciso...')
        print('-----------------')
        print('[*] Nmap -v -sV', Host)
        time.sleep(5.0)
        print('-----------------')
        print('Comando sV é para obter informações sobre provaveis portas abertas.')
        print('-----------------')
        nmapscanner = f'nmap -v -sV {Host}'
        os.system(nmapscanner)  
        print('------------------\t\n')
        print('[*] Nmap -Pn', Host)
        print('\t\n')
        print('------------------')
        nmapscanner2 = f'nmap -Pn {Host}'
        os.system(nmapscanner2)
    except Exception as erro:
        print('Ocorreu um erro', erro)
    finally:
        print('\t\n')
        print('[-_-] Obrigado Por Usar O Meu PortScan/Loucura!')
            
            





















                 #Se nenhuma porta for encontrada, será exibido.
                                                    #As portas fechadas não irão aparecer     


#----------------------------Outro Script Que Estava Em Desenvolvimento--------------------------------------------#                
    #scaneado com nmap.
    
# class nmap():   
#     nmap = nmap.PortScanner
#     nmap.scan(Host,range)
#     print("Scaneado as portas.")
#     print(nmap.scan())
#     print(nmap[Host].all_protocols())
#     print(nmap[Host]['tcp'].keys())



#Portas_Abertas = input('Mostrar portas abertas?\t' '(Y/N):')


#----------------------------Outro Script Que Estava Em Desenvolvimento---------------------------------------------#


# import socket

# for client in range(1,500 ):
#     client = client.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
#     client.connect('192.168.0.10', 8080)
#     client.send('Eu sou o client\t')
#     if client == True:
#         print('Connect')
#     else:
#         print('Porta fechada')

# except Exception as error:
#      print('Erro: ', error)

