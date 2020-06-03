import face_recognition

def recognizer(data_set, unknown):
    pictures_known = face_recognition.load_image_file(data_set)
    known_face_encoding = face_recognition.face_encodings(pictures_known)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

    unknown_picture = face_recognition.load_image_file(unknown)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

    results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

    if results[0] == True:
        return 1
    else:
        return 0
