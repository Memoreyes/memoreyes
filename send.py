import requests
url = "http://192.81.213.206:5000/"
files = { 'photo': open('image.jpg', 'rb'),}
data = {'userId': '12345'}
#files = {'userId':"12345", 'photo': open('image.jpg', 'rb'),}
#headers = {'enc-type': 'multipart/form-data'}
r = requests.post(url, data=data, files=files )
print(r)
print(r.json())
