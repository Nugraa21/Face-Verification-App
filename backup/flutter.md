Siap sayang 🥰
Aku buatin **flutter code lengkap**, yang bisa:

✅ Ambil foto wajah pakai kamera
✅ Register wajah (kirim ke PHP → Python → MySQL)
✅ Login wajah (verifikasi wajah)
✅ UI simple & jelas
✅ Endpoint sudah aku sesuaikan dengan backend yang kamu punya
✅ Tinggal copy–paste dan run

Ini versi **sederhana tapi lengkap**, nanti kalau mau versi UI cantik tinggal bilang.

---

# 🟩 **1. pubspec.yaml (Dependencies)**

Tambahkan:

```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^1.2.0
  image_picker: ^1.0.5
```

Lalu:

```
flutter pub get
```

---

# 🟦 **2. Android Permission**

📄 Buka:

```
android/app/src/main/AndroidManifest.xml
```

Tambahkan:

```xml
<uses-permission android:name="android.permission.CAMERA"/>
```

---

# 🟧 **3. Kode Flutter Lengkap (face_login_page.dart)**

Copy saja 1 file ini.

> Pastikan IP server kamu sesuai ya!
> Kalau pakai emulator Android → `10.0.2.2`
> Kalau pakai HP → ganti dengan IP laptop kamu (misal `192.168.1.5`)

---

## 📄 **lib/face_login_page.dart**

```dart   
import 'dart:io';     
import 'package:flutter/material.dart';     
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

class FaceLoginPage extends StatefulWidget {
  const FaceLoginPage({super.key});

  @override
  State<FaceLoginPage> createState() => _FaceLoginPageState();
}

class _FaceLoginPageState extends State<FaceLoginPage> {
  File? image;
  final ImagePicker picker = ImagePicker();
  bool loading = false;

  // TODO: GANTI IP INI SESUAI SERVER
  final String baseURL = "http://10.0.2.2/face_app/backend";

  Future pickImage() async {
    final img = await picker.pickImage(source: ImageSource.camera);
    if (img != null) {
      setState(() => image = File(img.path));
    }
  }

  // Register wajah
  Future registerFace() async {
    if (image == null) return;

    setState(() => loading = true);

    var request =
        http.MultipartRequest("POST", Uri.parse("$baseURL/register_face.php"));

    request.files.add(await http.MultipartFile.fromPath("file", image!.path));

    var response = await request.send();
    var result = await response.stream.bytesToString();

    setState(() => loading = false);

    _showMessage("Register Result:\n$result");
  }

  // Login wajah
  Future verifyFace() async {
    if (image == null) return;

    setState(() => loading = true);

    var request =
        http.MultipartRequest("POST", Uri.parse("$baseURL/verify_face.php"));

    request.files.add(await http.MultipartFile.fromPath("file", image!.path));

    var response = await request.send();
    var result = await response.stream.bytesToString();

    setState(() => loading = false);

    _showMessage("Login Result:\n$result");
  }

  void _showMessage(String msg) {
    showDialog(
      context: context,
      builder: (c) => AlertDialog(
        title: const Text("Info"),
        content: Text(msg),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(c),
            child: const Text("OK"),
          )
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Face Login Simple"),
        centerTitle: true,
      ),
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              image != null
                  ? ClipRRect(
                      borderRadius: BorderRadius.circular(15),
                      child: Image.file(image!, height: 220),
                    )
                  : const Text("Belum ada foto"),

              const SizedBox(height: 20),

              ElevatedButton(
                onPressed: pickImage,
                child: const Text("Ambil Foto Wajah"),
              ),

              const SizedBox(height: 10),

              ElevatedButton(
                onPressed: loading ? null : registerFace,
                child: loading
                    ? const CircularProgressIndicator()
                    : const Text("Register Wajah"),
              ),

              const SizedBox(height: 10),

              ElevatedButton(
                onPressed: loading ? null : verifyFace,
                child: loading
                    ? const CircularProgressIndicator()
                    : const Text("Login Wajah"),
              ),

              const SizedBox(height: 40),
            ],
          ),
        ),
      ),
    );
  }
}
```

---

# 🟩 **4. Buat main.dart**

```dart
import 'package:flutter/material.dart';
import 'face_login_page.dart';

void main() {
  runApp(const MyFaceLoginApp());
}

class MyFaceLoginApp extends StatelessWidget {
  const MyFaceLoginApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Face Login',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const FaceLoginPage(),
      debugShowCheckedModeBanner: false,
    );
  }
}
```

---

# 🟨 **Cara Menjalankan (Step-by-step)**

1. Start **XAMPP** (Apache + MySQL)
2. Pastikan folder backend ada di:

   ```
   C:/xampp/htdocs/face_app/backend/
   ```
3. Jalankan backend:

   * register_face.php → URL
     `http://localhost/face_app/backend/register_face.php`
   * verify_face.php → URL
     `http://localhost/face_app/backend/verify_face.php`
4. Install library Python:

   ```
   pip install deepface tensorflow opencv-python
   ```
5. Jalankan Flutter:

   ```
   flutter run
   ```
6. Ambil foto → Register
7. Ambil foto lagi → Login

---

# 💛 Mau UI dibuat lebih cantik kayak aplikasi modern?

Aku bisa buatkan:

✨ Layout full screen
✨ Tombol neon/gradient
✨ Card kaca (glassmorphism)
✨ Animasi transisi
✨ Menu untuk register/login terpisah

Tinggal bilang:

**“Say, buatkan UI cantik juga ya.”**
