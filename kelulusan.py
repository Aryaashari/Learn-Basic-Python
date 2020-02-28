#Program Kelulusan
def kelulusan():
    nama = input("Masukkan nama peserta didik: ")
    print("")

    mapel = ["Matematika", "Bahasa Indonesia", "Kimia", "Fisika", "Penjas", "Bahasa Inggris", "Seni Budaya", "PKN", "Biologi", "TIK"]

    for i in mapel:
        print(i, end="")
        nilai = int(input("| Masukkan nilai dari mapel tersebut dari 10 - 100: "))
        angka = (nilai + nilai + nilai + nilai + nilai + nilai + nilai + nilai + nilai + nilai)
    print("")
    print("Total nilai: ",angka)
    print("")
    lulus = angka >= 450
    tidak_lulus = angka < 450

    if lulus:
        print("SISWA/i YANG BERNAMA",nama,"NAIK KELAS")
    elif tidak_lulus:
        print("SISWA/i YANG BERNAMA",nama,"TIDAK NAIK KELAS")

    else:
        print("Nilai dari siswa/i yang bernama",nama,"tidak ada")
            
kelulusan()
