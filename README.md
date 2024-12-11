
# QR Code Generator

A Python-based QR code generator that creates shopping bill QR codes with customer details, itemized billing, and total cost. This project demonstrates how to work with libraries like `qrcode` and `PIL` to generate and save QR codes dynamically.

## Features
- Accepts customer details, bill ID, and itemized shopping details.
- Calculates the total bill amount automatically.
- Generates a QR code containing all bill details.
- Saves the QR code as an image file (`shopping_qr_code.png`).

## Requirements
- Python 3.6 or higher
- Libraries:
  - `qrcode`
  - `Pillow` (PIL)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/masimkhan-dev/qr-code-generator.git
   cd qr-code-generator
   ```
2. Install the required libraries:
   ```bash
   pip install qrcode pillow
   ```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter customer details, bill ID, and itemized shopping information.
3. The script will calculate the total bill and generate a QR code.
4. The QR code will be saved in the current directory as `shopping_qr_code.png`.

## Example
### Input:
```
Enter customer name: John Doe
Enter bill ID: 12345
Enter item name (or type 'done' to finish): Apple
Enter price for Apple: 2.5
Enter quantity for Apple: 4
Enter item name (or type 'done' to finish): Milk
Enter price for Milk: 1.8
Enter quantity for Milk: 2
Enter item name (or type 'done' to finish): done
```

### Output:
- A QR code file `shopping_qr_code.png` containing:
  ```
  Customer Name: John Doe
  Bill ID: 12345
  Shopping Bill:
  Apple (x4): $10.00
  Milk (x2): $3.60

  Total: $13.60
  ```

## Future Enhancements
- Add an option to display the QR code directly after generation.
- Integrate the feature to email or share the QR code.
- Implement a GUI for better user interaction.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

