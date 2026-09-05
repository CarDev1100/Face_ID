from pathlib import Path
import face_recognition
import cv2

known_faces_dir = Path(r"C:\Users\chpro\Desktop\coding\Face_ID\Faces\KNOWN_FACES")
unknown_faces_dir = Path(r"C:\Users\chpro\Desktop\coding\Face_ID\Faces\UNKNOWN_FACES")

known_names = []
known_faces = []

for name in known_faces_dir.iterdir():
    name = name.stem
    for filename in Path(rf"C:\Users\chpro\Desktop\coding\Face_ID\Faces\KNOWN_FACES\{name}").iterdir():
        image = face_recognition.load_image_file(filename)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

print("Prossesing unknown faces")

for filename in unknown_faces_dir.iterdir():
    image = face_recognition.load_image_file(filename)
    encoding = face_recognition.face_encodings(image)[0]
    result = face_recognition.compare_faces(known_faces, encoding, 0.6)
    if True in result:
        index = result.index(True)
        print(filename.stem + " is " + known_names[index])
    else:
        print(filename.stem + " is unknown")
        