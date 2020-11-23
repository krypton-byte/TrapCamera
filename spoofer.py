import smtplib
from base64 import b64decode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
def send_email(TO: str, SUBJECT: str, TEXT: str, ImageData):
    FROM = ""
    Passw=""
    Message=MIMEMultipart()
    Message["Subject"] = SUBJECT
    Message["From"]    = FROM
    Message["To"]      = TO
    Text               = MIMEText(TEXT)
    Image              = MIMEImage(b64decode(ImageData[31:]))
    Message.attach(Text)
    Message.attach(Image)
    # Prepare actual message
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, Passw)
        server.sendmail(FROM, TO, Message.as_string())
        server.close()
        print("terkirim")
        return 'Terkirim'
    except Exception as e:
        print(e)
        print("gagal")
        return "Gagal Terkirim"