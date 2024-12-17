import hmac
import hashlib
import base64

WEB_ID = "5bf9e635-71c2-4daa-aa2b-d265f810caf6"
WEB_KEY = "y93GFqrpkn5Wy8k8"
SECRET = "7d9YQ69sNtpQeJFdg94bPt2n33gHxCsbNPCqTeXasxzFXYDwPja7FFjKnT7ZYA6j"

def get_signature(timestamp):
    fullsec = timestamp + WEB_ID + WEB_KEY
    
    msg = fullsec.encode('utf-8')
    secret = SECRET.encode('utf-8')

    hashed = hmac.new(secret, msg, hashlib.sha256).digest()
    encoded_string = base64.b64encode(hashed)

    return encoded_string.decode('utf-8')
