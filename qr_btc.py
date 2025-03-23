# https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki#simpler-syntax

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

