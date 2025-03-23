# 🧾 QR Code Generator for Bitcoin addresses

This small Python script allows you to generate a QR code from a Bitcoin address. It works on macOS and Ubuntu.

## 🛠️ Requirements

- Python 3
- Pip
- `qrcode` and `Pillow` libraries

## Installation (Mac & Ubuntu)

```bash
# Check if you have Python 3
python3 --version

# Install pip if you don't have it
# On Mac:
sudo easy_install pip

# On Ubuntu:
sudo apt update
sudo apt install python3-pip

# Install the required library
# On Ubuntu:
pip3 install qrcode[pil]

# On Mac:
pip install "qrcode[pil]"
```

## 🚀 How to use
Save the following code as qr_btc.py:

```python
import qrcode

# Request Bitcoin address
bitcoin_address = input("Enter your Bitcoin address: ").strip()

# Construct the URI with standard prefix
uri = f"bitcoin:{bitcoin_address}"

# Generate the QR code
qr = qrcode.make(uri)

# Save the QR code as a PNG image
filename = "bitcoin_qr.png"
qr.save(filename)

print(f"✅ QR code generated: {filename}")
```

## ▶️ Execution

```bash
python3 qr_btc.py
```

Enter your Bitcoin address when prompted. The file bitcoin_qr.png will be generated in the same directory.

## 🖼️ Open the image
On Mac:
```bash
open bitcoin_qr.png
```

On Ubuntu:
```bash
xdg-open bitcoin_qr.png
```
