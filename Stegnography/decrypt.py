import cv2
import numpy as np

def binary_to_text(binary_string):
    """Convert binary string to text."""
    text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    return text

def decode_image(image_path, input_password):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image '{image_path}'. Check if the file exists.")
        return

    h, w, _ = img.shape
    binary_secret = ""

    for row in range(h):
        for col in range(w):
            pixel = img[row, col]
            for i in range(3):  # Extract from RGB channels
                binary_secret += str(pixel[i] & 1)
                if binary_secret[-16:] == "1111111111111110":  # End marker found
                    binary_secret = binary_secret[:-16]
                    secret_data = binary_to_text(binary_secret)
                    saved_password, message = secret_data.split(":", 1)

                    if saved_password == input_password:
                        print(f"Decryption Successful! Secret Message: {message}")
                    else:
                        print("Error: Incorrect Password! Access Denied.")
                    return

    print("Error: No hidden message found!")

# Input
image_path = "encryptedImage.png"
password = input("Enter passcode for decryption: ")

# Decrypt
decode_image(image_path, password)