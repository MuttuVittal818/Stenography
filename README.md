# Secure Data Hiding in Image Using Steganography  

## 📌 Project Overview  
This project implements **image steganography**, a technique for **hiding secret messages inside images** without altering their visual appearance. Using Python and OpenCV, we embed and retrieve messages from an image securely.  

---

## 🛠️ Technologies Used  
- **Python** – Core programming language  
- **OpenCV** – Image processing library  
- **NumPy** – Array manipulations  
- **Cryptography** – Secure encoding techniques  
- **VS Code** – Development environment  
- **GitHub** – Version control  

---

## 🎯 Features  
✅ Hide secret messages inside an image  
✅ Retrieve hidden messages with the correct passcode  
✅ No visible changes to the image after encoding  
✅ Lightweight and efficient algorithm  

---

## 📌 How It Works  
1. **Encoding Phase**:  
   - A secret message is converted into ASCII values.  
   - These values are embedded into the image pixels.  
   - The modified image is saved as an encrypted file.  

2. **Decoding Phase**:  
   - The program extracts hidden data from the image.  
   - The user must enter the correct passcode for decryption.  
   - The original message is displayed if authentication is successful.  

---

## 🚀 Installation & Usage  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/steganography-project.git
cd steganography-project
