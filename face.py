import kairos_face

kairos_face.settings.app_id = "55f5803f"
kairos_face.settings.app_key = "d5b54dd5365416aa82506ef2c1f0b2e8"


def enroll_face(image_file,name,gallery):
	z = kairos_face.enroll_face(file=image_file, subject_id=name, gallery_name=gallery)
	print(z)
def detect_face(image_file,gallery):
	recognized_faces = kairos_face.detect_face(file=image_file, gallery_name=gallery)
def recognize_face(image_file,gallery):
	z = recognized_faces = kairos_face.recognize_face(file=image_file, gallery_name=gallery)
	print(z)
def verify_face(image_file,gallery):
	recognized_faces = kairos_face.verify_face(file=image_file, gallery_name=gallery)
def get_galleries():
	galleries_list = kairos_face.get_galleries_names_list()
	return galleries_list
def check_galleries(gallery):
	gallery_subjects = kairos_face.get_gallery(gallery)
	return gallery_subjects
def delete_face(name,gallery):
	kairos_face.remove_face(subject_id=name, gallery_name=gallery)

if __name__ == "__main__":
	enroll_face("image.jpg","Shalini","mainppl")
	#recognize_face("image.jpg",'m')
	#verify_face('image.jpg',"mainppl")
#	recognized_faces = kairos_face.recognize_face(file= 'imageN.jpg', gallery_name='mainppl')
#	print(recognized_faces['images'][0]['transaction']['subject_id'])
#	print(recognized_faces[0])
