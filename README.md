# 🖼️ Image Steganography using OpenCV

This project implements **Steganography** using **Least Significant Bit (LSB) Encoding** to hide secret messages inside images securely.

## 📌 Features
✅ Hide a **secret message** inside an image  
✅ **Password protected** decryption  
✅ Works with **JPG & PNG images**  
✅ Uses **OpenCV & NumPy** for image processing  
✅ **Error handling** for invalid inputs  

---

## 🚀 Installation

1️⃣ **Clone the repository**

git clone https://github.com/GuruVishnuKumar/Cybersecurity-Intern-Project.git
cd Cybersecurity-Intern-Project

2️⃣ Install required dependencies

pip install opencv-python numpy

🎯 Usage
🔹 Encryption (Hiding the Message)

python encrypt.py
Enter the message and password
It creates a new encryptedImage.png with the hidden message.

🔹 Decryption (Extracting the Message)

python decrypt.py
Enter the password to reveal the secret message.

📜 Code Explanation
🔹 encrypt.py (Hides the message)
Reads the image using OpenCV (cv2.imread()).
Converts the message + password into binary.
Hides the binary bits in the Least Significant Bits (LSB) of the image pixels.
Saves the modified image as encryptedImage.png.

🔹 decrypt.py (Extracts the message)
Reads encryptedImage.png using OpenCV.
Extracts the hidden bits from the LSB of pixels.
Converts the binary data back to text.
Checks the password before revealing the secret message.

🛠️ Example
Step 1: Encrypt

$ python encrypt.py
Enter secret message: Hello World!
Enter a passcode: secret123
Message encrypted successfully! Saved as encryptedImage.png

Step 2: Decrypt

$ python decrypt.py
Enter passcode for decryption: secret123
Decryption Successful! Secret Message: Hello World!

🛡️ Security Note
This method provides basic security by hiding data inside an image.
For better security, you can encrypt the message (e.g., AES Encryption) before hiding it.




