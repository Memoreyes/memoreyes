import cloudinary
import cloudinary.uploader
import cloudinary.api
from twilio.rest import Client
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='b13f85fd22ca4e48804a4ff2e0943fc3')
cloudinary.config( 
  cloud_name = "memoreyes", 
  api_key = "258378735945794", 
  api_secret = "dGns_DZrLvLDhBUtVrOe6fXy2Tk" 
)

account_sid = "AC0af2539a4b3464099277e467b55416e2"
auth_token = "6b0795ad780fce6469afe57f6724a557"
client = Client(account_sid, auth_token)

def get_relevant_tags(image_url):
    response_data = app.tag_urls([image_url])
 
    tag_urls = []
    for concept in response_data['outputs'][0]['data']['concepts']:
        tag_urls.append(concept['name'])
 
    return tag_urls

def get_tags(image):
	t = cloudinary.uploader.upload(str(image))
	url = t['url']
	print(url)
	ret = get_relevant_tags(url)
	st = "\n".join(ret)
	message = client.api.account.messages.create(to="+17036095733",
                                             from_="+12402610654",
                                             body="Relevant tags: " + st,
                                             media_url=[url])
	return ret

'''
if __name__ == '__main__':
	z = get_tags("images/imageN.jpg")
	print "\n".join(z)
'''
