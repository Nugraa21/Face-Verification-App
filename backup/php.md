Siap sayang, aku tulis **SELURUH CODE LENGKAP** dari:

✅ SQL untuk database
✅ PHP backend (register + verify)
✅ Python script DeepFace
✅ Struktur foldernya juga sudah sesuai

Dan semuanya sudah **siap pakai di XAMPP + Python**.

---

# 🟩 **1. SQL DATABASE (Ketik di phpMyAdmin)**

Buat database dulu:

```
CREATE DATABASE face_db;
```

Lalu pilih database `face_db`, dan buat tabel:

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  face_embedding LONGTEXT NOT NULL
);
```

---

# 🟧 **2. Struktur Folder Backend (Copy Paste)**

Di:

```
C:/xampp/htdocs/face_app/backend/
```

Struktur:

```
backend/
│
├── face_embedding.py
├── register_face.php
├── verify_face.php
└── upload/           ← WAJIB ada
```

---

# 🟨 **3. PYTHON CODE (face_embedding.py)**

**SIMPAN file ini di:**
`C:/xampp/htdocs/face_app/backend/face_embedding.py`

```python
import sys
import json
from deepface import DeepFace

# Ambil path foto dari argumen PHP
image_path = sys.argv[1]

# Generate embedding wajah dengan model Facenet
embedding = DeepFace.represent(
    img_path=image_path,
    model_name="Facenet"
)

# Ambil vector embedding saja
vector = embedding[0]["embedding"]

# Print dalam format JSON (dibaca PHP)
print(json.dumps(vector))
```

### Install dependensi Python:

Buka CMD:

```
pip install deepface
pip install tensorflow
pip install opencv-python
```

---

# 🟦 **4. PHP Backend Code**

## ▶ A. **register_face.php**

**SIMPAN di:**
`C:/xampp/htdocs/face_app/backend/register_face.php`

```php
<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");

// Folder upload
$uploadDir = "upload/";
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0777, true);
}

// Simpan file foto sementara
$target = $uploadDir . uniqid() . ".jpg";
move_uploaded_file($_FILES["file"]["tmp_name"], $target);

// Jalankan Python untuk mengambil embedding
$command = "python face_embedding.py " . escapeshellarg($target);
$output = shell_exec($command);
$embedding = $output;

// Koneksi ke MySQL
$conn = new mysqli("localhost", "root", "", "face_db");

if ($conn->connect_error) {
    die(json_encode(["status" => "error", "message" => $conn->connect_error]));
}

// Simpan embedding ke database
$stmt = $conn->prepare("INSERT INTO users (face_embedding) VALUES (?)");
$stmt->bind_param("s", $embedding);
$stmt->execute();

echo json_encode([
    "status" => "success",
    "message" => "Wajah berhasil diregistrasi!",
    "user_id" => $conn->insert_id
]);
?>
```

---

## ▶ B. **verify_face.php**

**SIMPAN di:**
`C:/xampp/htdocs/face_app/backend/verify_face.php`

```php
<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");

function cosineSimilarity($a, $b) {
    $dot = 0.0; $normA = 0.0; $normB = 0.0;

    for ($i = 0; $i < count($a); $i++) {
        $dot += $a[$i] * $b[$i];
        $normA += $a[$i] ** 2;
        $normB += $b[$i] ** 2;
    }

    return $dot / (sqrt($normA) * sqrt($normB));
}

// Upload foto baru untuk login
$uploadDir = "upload/";
$target = $uploadDir . uniqid() . ".jpg";
move_uploaded_file($_FILES["file"]["tmp_name"], $target);

// Generate embedding wajah baru
$command = "python face_embedding.py " . escapeshellarg($target);
$output = shell_exec($command);
$newEmbedding = json_decode($output, true);

// Koneksi DB
$conn = new mysqli("localhost", "root", "", "face_db");
$result = $conn->query("SELECT id, face_embedding FROM users");

$bestMatch = null;
$bestScore = -1;

// Bandingkan embedding baru dengan semua di DB
while ($row = $result->fetch_assoc()) {
    $dbEmbedding = json_decode($row["face_embedding"], true);
    $similarity = cosineSimilarity($newEmbedding, $dbEmbedding);

    if ($similarity > $bestScore) {
        $bestScore = $similarity;
        $bestMatch = $row["id"];
    }
}

// Threshold cocok (0.75 sudah lumayan aman)
if ($bestScore > 0.75) {
    echo json_encode([
        "status" => "success",
        "user_id" => $bestMatch,
        "similarity" => $bestScore
    ]);
} else {
    echo json_encode([
        "status" => "failed",
        "message" => "Wajah tidak cocok.",
        "similarity" => $bestScore
    ]);
}
?>
```

---

# 🟩 **Sampai sini semua backend siap dipakai.**

Yang sudah lengkap:

✔ SQL database
✔ Script Python DeepFace
✔ PHP register wajah
✔ PHP login wajah
✔ Struktur folder backend

---

# 💛 Mau aku lanjutkan bagian Flutter-nya juga?

Yang nanti aku buatkan:

✔ Flutter code ambil foto
✔ Flutter code upload ke PHP
✔ Register wajah
✔ Login wajah
✔ UI simple & clean

Tinggal bilang:

**“Say, lanjut buatkan Flutter-nya.”** 😘
