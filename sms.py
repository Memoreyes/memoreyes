from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse 
import os
 
app = Flask(__name__)
@app.route('/sms', methods=['POST'])
def sms():
    #os.system("rm name.txt | echo>name.txt")
    f = open("name.txt","w") 
    resp = MessagingResponse()
    body = request.values.get('Body', None)	
    print(body)
    f.write(body)
    resp.message('Hello, Memoreyes will add the face captured to the name: {}'.format(body))
    f.close()
    return str(resp)
 
if __name__ == '__main__':
    app.run()
