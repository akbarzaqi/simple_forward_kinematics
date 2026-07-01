# Inverse Kinematics 2-DOF Robot Arm

Program ini merupakan implementasi algoritma **Inverse Kinematics (IK)** untuk lengan robot planar dengan dua derajat kebebasan (2-DOF) menggunakan Python. Program menghitung sudut kedua joint berdasarkan koordinat target yang diberikan, kemudian memvalidasi hasil menggunakan **Forward Kinematics** serta menampilkan visualisasi konfigurasi lengan robot.

## Program Flow

```
Start
  │
  ▼
Input:
- Target (x, y)
- Panjang Link (L1, L2)
  │
  ▼
Hitung Jarak Target (d)
  │
  ▼
Periksa Keterjangkauan Target
(|L1 − L2| ≤ d ≤ L1 + L2)
  │
  ├── Tidak Terjangkau
  │       │
  │       ▼
  │   Program Berhenti
  │
  ▼
Hitung Sudut θ₂
(Hukum Cosinus)
  │
  ▼
Hitung Sudut θ₁
(atan2 dan geometri segitiga)
  │
  ▼
Validasi dengan
Forward Kinematics
  │
  ▼
Visualisasi Lengan Robot
  │
  ▼
Finish
```
