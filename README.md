# Simple Port Scanner

A basic TCP port scanner written in Python for educational purposes and authorized security testing.

---

## 📄 Description

This project implements a simple TCP port scanner using Python sockets.  
It attempts to establish a TCP connection to a predefined list of ports on a target host and reports which ports are open.

The goal of this project is to demonstrate:

- How TCP connections work at a low level
- Basic port scanning logic
- Use of Python sockets for network reconnaissance
- Interpretation of connection responses

---

## ⚙️ Features

- TCP port scanning
- Customizable target host
- Customizable port list
- Lightweight and fast execution
- Simple and readable implementation

---

## 📦 Requirements

- Python 3.x  
- Network access to the target host  

---

## 🚀 Usage

### 1️⃣ Edit the target host and ports inside the script:

```python
host = "www.google.com"
ports = [80, 443, 21, 22]
```

### 2️⃣ Run the scanner:

```python
python port_scanner.py
```

## 📁 Project Structure

```bash
simple_port_scanner/
├── port_scanner.py
└── README.md
```

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only.

⚠️ Do not scan systems without explicit permission.
Unauthorized port scanning may be illegal depending on your jurisdiction.

## 🧠 Author Notes

This project was created as a foundational exercise to understand network reconnaissance concepts and the behavior of TCP services during connection attempts.