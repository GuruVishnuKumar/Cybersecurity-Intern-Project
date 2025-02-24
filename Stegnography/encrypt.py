import cv2
import numpy as np

def text_to_binary(text):
    """Convert text to binary string."""
    return ''.join(format(ord(char), '08b') for char in text)

def encode_image(image_path, output_path, message, password):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image '{image_path}'. Check if the file exists.")
        return

    h, w, _ = img.shape

    # Prepare the message with a separator
    secret_data = password + ":" + message
    binary_secret = text_to_binary(secret_data) + '1111111111111110'  # End marker

    # Check if image can store the message
    max_bytes = h * w * 3 // 8
    if len(binary_secret) > max_bytes * 8:
        print("Error: Message is too long for this image. Try a larger image.")
        return

    data_index = 0
    for row in range(h):
        for col in range(w):
            pixel = list(img[row, col])  # Convert pixel to list
            for i in range(3):  # Modify RGB channels
                if data_index < len(binary_secret):
                    bit_value = int(binary_secret[data_index])
                    pixel[i] = (pixel[i] & ~1) | bit_value  # Ensure pixel remains in uint8 range
                    pixel[i] = max(0, min(255, pixel[i]))  #  Prevent OverflowError
                    data_index += 1
            img[row, col] = np.array(pixel, dtype=np.uint8)  # Convert back to array
            if data_index >= len(binary_secret):
                cv2.imwrite(output_path, img)
                print(f"Message encrypted successfully! Saved as {output_path}")
                return

# Input
image_path = "pic.jpg"
output_path = "encryptedImage.png"
message = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encrypt
encode_image(image_path, output_path, message, password)