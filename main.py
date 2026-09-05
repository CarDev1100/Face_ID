import face_recognition
import pathlib as Path

"""
Face ID: simple facial recognition.

Compares every image in Faces/UNKNOWN_FACES against a library of known people
and prints who each one is, or "unknown" if there's no match.

Expected layout - one subfolder per person, named after them:
    Faces/KNOWN_FACES/Elon/photo1.jpg
    Faces/KNOWN_FACES/Elon/photo2.jpg
    Faces/UNKNOWN_FACES/mystery.jpg
"""

# Replace the paths below with your own
known_faces_dir = Path(r"C:\Users\chpro\Desktop\coding\Face_ID\Faces\KNOWN_FACES")
unknown_faces_dir = Path(r"C:\Users\chpro\Desktop\coding\Face_ID\Faces\UNKNOWN_FACES")

# Parallel lists: known_faces[i] is an encoding of the person known_names[i].
# Someone with several photos gets several entries, all under the same name.
known_names = []
known_faces = []

for person_dir in known_faces_dir.iterdir():
    for filename in person_dir.iterdir():
        image = face_recognition.load_image_file(filename)
        # [0] takes the first face found - assumes one person per training photo
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(person_dir.stem)

print("Processing unknown faces")

for filename in unknown_faces_dir.iterdir():
    image = face_recognition.load_image_file(filename)
    encoding = face_recognition.face_encodings(image)[0]
    # 0.6 is the distance tolerance - lower is stricter, higher matches loosely
    result = face_recognition.compare_faces(known_faces, encoding, 0.6)
