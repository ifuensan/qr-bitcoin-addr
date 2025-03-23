# 🧾 Generador de Código QR para Direcciones Bitcoin en Python

Este pequeño script de Python permite generar un código QR a partir de una dirección de Bitcoin. Funciona en macOS y Ubuntu.

## 🛠️ Requisitos

- Python 3
- Pip
- Librería `qrcode` y `Pillow`

## Instalación (Mac & Ubuntu)

```bash
# Verifica si tienes Python 3
python3 --version

# Instala pip si no lo tienes
# En Mac:
sudo easy_install pip

# En Ubuntu:
sudo apt update
sudo apt install python3-pip

# Instala la librería necesaria
pip3 install qrcode[pil]
```

## 🚀 Cómo usar
Guarda el siguiente código como qr_btc.py:

```
import qrcode

# Solicita dirección de Bitcoin
bitcoin_address = input("Introduce tu dirección de Bitcoin: ").strip()

# Construye el URI con prefijo estándar
uri = f"bitcoin:{bitcoin_address}"

# Genera el código QR
qr = qrcode.make(uri)

# Guarda el código QR como imagen PNG
filename = "bitcoin_qr.png"
qr.save(filename)

print(f"✅ Código QR generado: {filename}")
```

## ▶️ Ejecución

```
python3 qr_btc.py
```

Introduce tu dirección de Bitcoin cuando se te solicite. El archivo bitcoin_qr.png se generará en el mismo directorio.

## 🖼️ Abrir la imagen
En Mac:
```
open bitcoin_qr.png
```

En Ubuntu:
```
xdg-open bitcoin_qr.png
```
