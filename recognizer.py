
import face_recognition
import argparse
import pickle
import cv2
from gtts import gTTS

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())


print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())


image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb,
	model=args["detection_method"])
encodings = face_recognition.face_encodings(rgb, boxes)


names = []


for encoding in encodings:

	matches = face_recognition.compare_faces(data["encodings"],
		encoding)
	name = "Unknown"


	if True in matches:

		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts = {}


		for i in matchedIdxs:
			name = data["names"][i]
			counts[name] = counts.get(name, 0) + 1


		name = max(counts, key=counts.get)


	names.append(name)
print(names)
if names!="Unknown":
	#t1= int(round(time.time()))
    mytext="Welcome "+names
    flag=1;
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    os.remove("welcome.mp3")
	os.remove(args["image"])
else:
	mytext="Face recognition failed please report to office for more info.Thank You"
    flag=1;
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    os.remove("welcome.mp3")

"""for ((top, right, bottom, left), name) in zip(boxes, names):
	# draw the predicted face name on the image
	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	y = top - 15 if top - 15 > 15 else top + 15
	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.75, (0, 255, 0), 2)

# show the output image
cv2.imshow("Image", image)"""
cv2.waitKey(0)
