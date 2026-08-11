# With the help of Flask,write a qr code generator that asks for the user their data and display the result on the browser
import qrcode
import os
from flask import Flask,render_template,request,url_for

app = Flask(__name__,static_folder='static',template_folder='templates')
QR_FOLDER=('static/qrcodes')
os.makedirs(QR_FOLDER,exist_ok=True)

@app.route('/')
def home():
    return render_template('form.html',title="personal information")

@app.route('/generator',methods=['POST'])
def generate():
    #1) Get the data from form;

    name=request.form["name"].upper()
    surname=request.form["surname"].upper()
    date_of_birth=request.form["age"].upper()
    email=request.form["email"]

    #2) Put all the data into one string for QR
    qr_data = f"Name: {name} {surname}\n, Date of Birth: {date_of_birth}\n Email: {email}"
    qr_filename=f"{name}_{surname}_qr.png"

    #3) Generator QR
    qr_path=os.path.join(QR_FOLDER,qr_filename)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="white")
    img.save(qr_path)

    return render_template("result.html",name=name,qr_file=qr_filename)

if __name__ == '__main__':
    app.run(debug=True)


