def sequential_search(nama, daftar_nama, daftar_telepon):
    for i in range(len(daftar_nama)):
        if daftar_nama[i] == nama:
            return daftar_telepon[i]
    
    return "Nomor telepon tidak ditemukan."

# Daftar nama dan nomor telepon
daftar_nama = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis"]
daftar_telepon = ["081234567890", "089876543210", "087811223344", "082122232425"]

# Pencarian nomor telepon Jane
nomor_telepon_jane = sequential_search("Jane Smith", daftar_nama, daftar_telepon)

print("Nomor telepon Jane: " + nomor_telepon_jane)


