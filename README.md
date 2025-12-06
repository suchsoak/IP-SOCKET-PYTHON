# 🌐 IP-SOCKET-PYTHON

A powerful socket scanner to gather information about any `IP` address or website `URL`.

```
  ██████     |
▒██    ▒     | BY: suchsoak
░ ▓██▄       | GitHub: https://github.com/suchsoak
  ▒   ██▒    | v:1.0.1
▒██████▒▒    |
▒ ▒▓▒ ▒ ░    |
░ ░▒  ░      |
░  ░  ░      |
      ░      |
```

## 📦 Installation

**Run these commands in your terminal:**

```sh
git clone https://github.com/suchsoak/IP-SOCKET-PYTHON.git
chmod +x requirements.txt
pip install -r requirements.txt
python3 ip.py
```

## 🚀 Usage

```sh
usage: ip.py [-h] [-u TARGET] [-i TARGET]

options:
    -h, --help            show this help message and exit
    -u TARGET, --url TARGET
                                                scan a URL
    -i TARGET, --ip TARGET
                                                scan an IP address
```

**Scan an IP:**
```sh
python3 ip.py -i <ip_target>
```

**Scan a URL:**
```sh
python3 ip.py -u <url_target>
```

## 📚 Libraries & Documentation

| Library | Link |
|---------|------|
| 🔌 socket | https://docs.python.org/3/library/socket.html |
| 🗺️ geocoder | https://geocoder.pbh.gov.br/geocoder/ |
| 🔍 python-whois | https://pypi.org/project/python-whois/ |
| 🎨 colorama | https://pypi.org/project/colorama/ |
| 📡 requests | https://pypi.org/project/requests/ |
| 🌐 urllib | https://docs.python.org/3/library/urllib.html |
| ⚙️ argparse | https://docs.python.org/3/library/argparse.html |
| 💾 os | https://docs.python.org/3/library/os.html |
| 🔄 sys | https://docs.python.org/3/library/sys.html |

## 📄 License

Licensed under the `MIT License`.
