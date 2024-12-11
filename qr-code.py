import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_shopping_qr(customer_name, bill_id, items, logo_path=None, output_path="shopping_qr_code.png"):
    # Calculate the total bill
    total_bill = sum(item['price'] * item['quantity'] for item in items)
    
    # Create the bill details string
    bill_details = f"Customer Name: {customer_name}\n"
    bill_details += f"Bill ID: {bill_id}\n"
    bill_details += "Shopping Bill:\n"
    for item in items:
        bill_details += f"{item['name']} (x{item['quantity']}): ${item['price'] * item['quantity']:.2f}\n"
    bill_details += f"\nTotal: ${total_bill:.2f}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(bill_details)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Add logo to the QR code if provided
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        logo_size = min(img.size) // 4
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)
        logo_position = (
            (img.size[0] - logo_size) // 2,
            (img.size[1] - logo_size) // 2
        )
        img.paste(logo, logo_position, mask=logo if logo.mode == 'RGBA' else None)
    
    # Save the image
    img.save(output_path)
    print(f"QR code generated and saved as '{output_path}'.")

def get_shopping_details():
    customer_name = input("Enter customer name: ").strip()
    bill_id = input("Enter bill ID: ").strip()
    
    items = []
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        
        try:
            item_price = float(input(f"Enter price for {item_name}: "))
            item_quantity = int(input(f"Enter quantity for {item_name}: "))
            items.append({'name': item_name, 'price': item_price, 'quantity': item_quantity})
        except ValueError:
            print("Invalid input! Please enter numeric values for price and integer values for quantity.")
    
    return customer_name, bill_id, items

if __name__ == "__main__":
    print("Welcome to the Advanced Shopping QR Code Generator!")
    customer_name, bill_id, items = get_shopping_details()
    
    # Optional logo integration
    use_logo = input("Do you want to add a logo to the QR code? (yes/no): ").strip().lower()
    logo_path = None
    if use_logo == "yes":
        logo_path = input("Enter the path to the logo image: ").strip()
        if not os.path.exists(logo_path):
            print("Logo file not found. Proceeding without a logo.")
            logo_path = None
    
    output_path = input("Enter the output filename (or press Enter for default 'shopping_qr_code.png'): ").strip()
    if not output_path:
        output_path = "shopping_qr_code.png"
    
    generate_shopping_qr(customer_name, bill_id, items, logo_path, output_path)
