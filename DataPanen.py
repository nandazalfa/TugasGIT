# Data Panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# Soal No 1
print("1. Seluruh yang ada di Data Panen:")
for lokasi, detail in data_panen.items():
    print(f"Nama Lokasi: {detail['nama_lokasi']}, Hasil Panen: {detail['hasil_panen']}")
print("\n")
    
# Soal No 2
print("2. Hasil Panen Jagung di Lokasi2:")
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung dari lokasi2: {hasil_jagung_lokasi2}")
print("\n")

# Soal No 3
print("3. Nama Lokasi pada Lokasi3:")
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")
print("\n")

# Soal No 4
print("4. Hasil Panen Padi dan Kedelai ke dalam Variabel yang Terpisah:")
hasil_panen_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
hasil_panen_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print("Hasil Panen Padi:", hasil_panen_padi)
print("Hasil Panen Kedelai:", hasil_panen_kedelai)
print("\n")

# Soal No 6
print("6. Lokasi yang Memerlukan Perhatian Khusus:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} membutuhkan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")
