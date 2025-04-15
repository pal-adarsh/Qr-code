# **QR Code Generator & Reader**  
*A Flask-based web application to generate and decode QR codes.*  

![Demo](https://img.shields.io/badge/Demo-Available-green)  
![Python](https://img.shields.io/badge/Python-3.x-blue)  
![Flask](https://img.shields.io/badge/Framework-Flask-red)  

## **Features**  
✔ **Generate QR Codes** from text or URLs.  
✔ **Decode QR Codes** from uploaded images.  
✔ **Download QR Codes** as PNG files.  
✔ **Open detected URLs** directly from the app.  

---

## **Technologies Used**  
- **Backend**: Python (Flask)  
- **Frontend**: HTML, CSS, JavaScript  
- **Libraries**:  
  - `qrcode` (QR generation)  
  - `OpenCV` + `pyzbar` (QR decoding)  
  - `BytesIO` (in-memory image handling)  

---

## **Setup & Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/qr-code-generator-reader.git
cd qr-code-generator-reader
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Run the Application**  
```bash
python app.py
```
- Open `http://localhost:5000` in your browser.  

---

## **How to Use?**  

### **1. Generate a QR Code**  
1. Enter text/URL in the input box.  
2. Click **"Generate"**.  
3. Download the QR code using the **"Download QR Code"** button.  

### **2. Read a QR Code**  
1. Upload an image containing a QR code.  
2. Click **"Read QR"**.  
3. View the decoded text. If it’s a URL, click **"Open Link"**.  

---

## **Project Structure**  
```
├── app.py                # Flask backend (routes & logic)  
├── templates/  
│   └── index.html        # Frontend HTML  
├── static/  
│   └── styles.css        # CSS styling  
├── requirements.txt      # Python dependencies  
└── README.md  
```

---

## **Future Improvements**  
- [ ] Add user authentication.  
- [ ] Support custom QR colors/logos.  
- [ ] Deploy on cloud (Heroku/Vercel).  
- [ ] Add history of generated QR codes.  

---

## **Contributing**  
Feel free to fork and submit PRs! Open an **issue** for bugs/feature requests.  

## **License**  
[MIT](https://choosealicense.com/licenses/mit/)  

---

### **Demo Screenshot**  
![image](https://github.com/user-attachments/assets/bc20d973-af04-4fd5-aa64-d8b36db35c2c)

---
