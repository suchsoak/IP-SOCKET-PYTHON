# IP-SOCKET-PYTHON

A scanner with socket, with information about a particular ip or url of a website.

>[!NOTE]
> The script is in development, any errors can be fixed in the future.

# How to install

**Place in the terminal:**

```sh
   git clone https://github.com/suchsoak/IP-SOCKET-PYTHON.git
```
**After enter in the files, and put:**

```sh
   chmod +X requirements.txt
```

```sh
    pip install -r requirements.txt
```

**Now start the script:**

```sh
    python3 ip.py
```

# Usage

>[!TIP]
>I recommended use IP

```sh

usage: ip.py [-h] [-u TARGET] [-i TARGET]

options:
  -h, --help            show this help message and exit
  -u TARGET, --url TARGET
                        url
  -i TARGET, --ip TARGET
                        ip

```

```sh
python3 ip.py -i <ip_target>
```
or

```sh
 python3 ip.py -u <url_target>
```

## For ports, you can use a list or 1 by then, 65535

```sh
 
#ports = [21, 22, 23, 25, 53, 80, 8080, 53, 110, 135, 139, 143, 70,  443, 445, 993, 995]

ports = range(1, 65535)

```

| Libraries |  Links |
| ------ | ------ |
| socket | https://docs.python.org/3/library/socket.html
| geocoder |  https://geocoder.pbh.gov.br/geocoder/
| python-whois | https://pypi.org/project/python-whois/
| colorama | https://pypi.org/project/colorama/
| requests | https://pypi.org/project/requests/
|  urlib   | https://docs.python.org/3/library/urllib.html
|  argparse | https://docs.python.org/3/library/argparse.html

