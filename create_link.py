import requests
import json

# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
import PaytmChecksum

paytmParams = dict()

paytmParams["body"] = {
    "mid"             : "YOUR_MID_HERE",
    "linkType"        : "GENERIC",
    "linkDescription" : "Test Payment",
    "linkName"        : "Test",
}

# Generate checksum by parameters we have in body
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "SnOLzayQTh_ty169")

paytmParams["head"] = {
    "tokenType"       : "AES",
    "signature"       : checksum
}

post_data = json.dumps(paytmParams)

# for Staging
url = "https://securegw-stage.paytm.in/link/create"

# for Production
# url = "https://securegw.paytm.in/link/create"

response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
print(response)
