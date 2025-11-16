import numpy as np
data_nilai = np.array([77, 80, 75, 94, 85, 90, 74, 88, 83, 71, 81])

nilai_rata = np.mean(data_nilai).round(2)
nilai_tertinggi = np.max(data_nilai)
nilai_terendah = np.min(data_nilai)
siswa_diatas_rata = np.sum(data_nilai >= nilai_rata)
 
print("nilai rata - rata:", nilai_rata)
print("nilai tertinggi:", nilai_tertinggi)
print("nilai terendah:", nilai_terendah)
print(f"jumlah mahasiswa dengan nilai diatas rata rata: {siswa_diatas_rata} mahasiswa")

print()

hari_kerja=["senin","selasa","rabu","kamis","jumat",]

print("Hari di Indeks Kedua : " ,hari_kerja[2])

print ("Tiga Hari Pertama : ", hari_kerja[0:3])

print ("Hari Kerja Dalam Urutan Terbalik : ",hari_kerja[::-1])

hari_kerja[4]="jumat berkah"
print ("Ganti Nilai Jumat : ", hari_kerja[4])

print()

import numpy as np

#membuat array dengan skor awal
skor_tim = np.array([45,67,34,88,52])
print(f"array awal: {skor_tim}")

#menambahkan skor terbaru (75) kedalam array
skor_tim = np.append(skor_tim,75)
print(f"skor akhir: {skor_tim}")

#cari dan cetak skor tertinggi
skor_tertinggi = np.max(skor_tim)
print(f"skor tertinggi: {skor_tertinggi}")

#skor terendah
skor_terendah = np.min(skor_tim)
print(f"skor terendah: {skor_terendah}")

#hapus skor terendah
index_terendah = np.where(skor_tim == skor_terendah) #np.where untuk menemukan posisi elemen (2)
skor_tim = np.delete(skor_tim,index_terendah)
print(f"array setelah di hapus skor terendah: {skor_tim}")
