# 🧾 QR code generator for Bitcoin addresses

This small Python script allows you to generate a QR code from a Bitcoin address. It works on macOS and Ubuntu.
Using BIP-021 espec https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki#simpler-syntax


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
# Based in https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki#simpler-syntax

import qrcode

# Request Bitcoin address
bitcoin_address = input("Enter your Bitcoin address: ").strip()
amount = input("Enter the amount in Bitcoin: ").strip()
label = input("Enter a label to add: ").strip()
message = input("Enter a message to add: ").strip()

# Build the URI with the standard prefix
# uri = f"bitcoin:{bitcoin_address}"
uri = f"bitcoin:{bitcoin_address}?amount={amount}&label={label}&message={message}"

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
