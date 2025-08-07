import qrcode

def generate_qr(data, filename='qr_code.png'):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

def main():
    print("Choose QR Code Type:")
    print("1: Website URL")
    print("2: UPI Payment")
    print("3: WhatsApp Message")
    print("4: Custom Text")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        url = input("Enter website URL: ")
        generate_qr(url, "website_qr.png")

    elif choice == '2':
        upi_id = input("Enter UPI ID (e.g. name@bank): ")
        name = input("Enter name: ")
        amount = input("Enter amount: ")
        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"
        generate_qr(upi_link, "upi_qr.png")

    elif choice == '3':
        phone = input("Enter phone number with country code (e.g. 919876543210): ")
        message = input("Enter message: ")
        whatsapp_link = f"https://wa.me/{phone}?text={message.replace(' ', '%20')}"
        generate_qr(whatsapp_link, "whatsapp_qr.png")

    elif choice == '4':
        text = input("Enter any text: ")
        generate_qr(text, "custom_text_qr.png")

    else:
        print("Invalid choice!")

# ✅ Correct entry point
if __name__ == "__main__":
    main()
