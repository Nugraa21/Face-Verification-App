import cv2
import face_recognition
import pickle
import os
import numpy as np

data_path = "data/face_data.pkl"

def verify_face():
    if not os.path.exists(data_path):
        print("Belum ada data wajah! Silakan register dulu.")
        return
    
    with open(data_path, "rb") as f:
        data = pickle.load(f)

    known_names = list(data.keys())
    known_encodings = list(data.values())

    cam = cv2.VideoCapture(0)

    print("Arahkan wajah ke kamera...")
    print("Tekan 'SPACE' untuk verifikasi")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Verify Face", frame)

        if cv2.waitKey(1) == 32:
            break

    cam.release()
    cv2.destroyAllWindows()

    rgb = frame[:, :, ::-1]
    faces = face_recognition.face_encodings(rgb)

    if len(faces) == 0:
        print("Tidak mendeteksi wajah!")
        return

    encoding = faces[0]

    # Bandingkan wajah
    matches = face_recognition.compare_faces(known_encodings, encoding)
    face_dist = face_recognition.face_distance(known_encodings, encoding)

    best_index = np.argmin(face_dist)

    if matches[best_index]:
        print(f"VERIFIKASI BERHASIL! Halo {known_names[best_index]}")
    else:
        print("VERIFIKASI GAGAL! Wajah tidak cocok.")

# ================= MAIN =================
if __name__ == "__main__":
    verify_face()
