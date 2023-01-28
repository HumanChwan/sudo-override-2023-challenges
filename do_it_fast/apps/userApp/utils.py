import jwt
import datetime
COOKIEE_SECRET_KEY='$uP3r_S3cRet_K3y'

def generateCookie():
    payload = {
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1),
    }
    return jwt.encode(payload, COOKIEE_SECRET_KEY, algorithm='HS256')

def checkCookie(cookie):
    try:
        jwt.decode(cookie, COOKIEE_SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return False
    return True


# c = generateCookie()
# d = checkCookie(c)