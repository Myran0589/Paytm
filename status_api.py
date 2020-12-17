import requests
import json

# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
import PaytmChecksum

# initialize a dictionary
paytmParams = dict()

# body parameters
paytmParams["body"] = {

    # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    "mid" : "YOUR_MID_HERE",

    # Enter your order id which needs to be check status for
    "orderId" : "YOUR_ORDER_ID",
}

# Generate checksum by parameters we have in body
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "YOUR_MERCHANT_KEY")

# head parameters
paytmParams["head"] = {

    # put generated checksum value here
    "signature"	: checksum
}

# prepare JSON string for request
post_data = json.dumps(paytmParams)

# for Staging
url = "https://securegw-stage.paytm.in/v3/order/status"

# for Production
# url = "https://securegw.paytm.in/v3/order/status"

response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()

