import json
import os

# Membaca provinsi
with open("provinsi.json", "r", encoding="utf-8") as f:
    provinsi = json.load(f)

wilayah = {}

for prov in provinsi:
    id_prov = prov["id"]
    nama_prov = prov["nama"]

    file_kab = f"kabupaten/{id_prov}.json"

    if not os.path.exists(file_kab):
        continue

    with open(file_kab, "r", encoding="utf-8") as f:
        kabupaten = json.load(f)

    for kab in kabupaten:
        id_kab = kab["id"]
        nama_kab = kab["nama"]

        file_kec = f"kecamatan/{id_kab}.json"

        if not os.path.exists(file_kec):
            continue

        with open(file_kec, "r", encoding="utf-8") as f:
            kecamatan = json.load(f)

        for kec in kecamatan:
            wilayah[kec["id"]] = {
                "provinsi": nama_prov,
                "kabupaten": nama_kab,
                "kecamatan": kec["nama"]
            }

# Simpan hasil
with open("wilayah.json", "w", encoding="utf-8") as f:
    json.dump(wilayah, f, ensure_ascii=False, indent=4)

print(f"Berhasil membuat wilayah.json ({len(wilayah)} kecamatan)")