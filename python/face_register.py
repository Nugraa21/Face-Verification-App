import cv2
import face_recognition
import pickle
import os

# Buat folder data
if not os.path.exists("data"):
    os.makedirs("data")

data_path = "data/face_data.pkl"

def register_face(name):
    cam = cv2.VideoCapture(0)

    print("Arahkan wajah ke kamera...")
    print("Tekan 'SPACE' untuk mengambil gambar")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Register Face", frame)

        if cv2.waitKey(1) == 32:  # Tombol SPACE
            break

    cam.release()
    cv2.destroyAllWindows()
 
    # Proses wajah        
    rgb = frame[:, :, ::-1] 
    faces = face_recognition.face_encodings(rgb)

    if len(faces) == 0:
        print("Wajah tidak terdeteksi, coba lagi!")
        return
    
    encoding = faces[0]

    # Simpan ke file
    data = {}

    if os.path.exists(data_path):
        with open(data_path, "rb") as f:
            data = pickle.load(f)

    data[name] = encoding

    with open(data_path, "wb") as f:
        pickle.dump(data, f)

    print(f"Wajah atas nama '{name}' berhasil diregistrasi!")

# =============== MAIN =================
if __name__ == "__main__":
    user_name = input("Masukkan nama untuk wajah ini: ")
    register_face(user_name)
