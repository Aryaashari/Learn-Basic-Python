"""
ISTILAH DALAM OOP :

Class = Prototipe yang ditentukan pengguna untuk objek yang mendefinisikan
        seperangkat atribut yang menjadi ciri objek kelas apapun. Atribut
        adalah dataanggota (variable kelas dan variable contoh) dan metode,
        diakses melalui notasi lirik.

Class Variable = Sebuah variabel yang dibagi oleh semua contoh kelas.
                 Variabel kelas didefinisikan dalam kelas tapi di luar metode
                 kelas manapun. Variabel kelas tidak digunakan sesering variabel
                 contoh.

Data Member = Variabel kelas atau variabel contoh yang menyimpan data yang
              terkaitdengan kelas dan objeknya.

Function overloading = Penugasan lebih dari satu perilaku ke fungsi tertentu.
                       Operasi yang dilakukan bervariasi menurut jenis objek
                       atau argumen yang terlibat.
                       
Instance variable = Variabel yang didefinisikan di dalam sebuah metode dan
                    hanya dimiliki oleh instance kelas saat ini.
                    
Inheritance = Pengalihan karakteristik kelas ke kelas lain yang berasal darinya.

Instance = Objek individu dari kelas tertentu. Obyek obj yang termasuk dalam
           Lingkaran kelas, misalnya, adalah turunan dari Lingkaran kelas.
           
Instantiation = Penciptaan sebuah instance dari sebuah kelas.

Method = Jenis fungsi khusus yang didefinisikan dalam definisi kelas.

Object = Contoh unik dari struktur data yang didefinisikan oleh kelasnya.
         Objek terdiri dari kedua anggota data (variabel kelas dan variabel
         contoh) dan metode.
         
Operator overloading = Penugasan lebih dari satu fungsi ke operator tertentu.

"""

class tkjb:
    #Atribut dengan underscore merupakan atribut private
    _kelas      = input("Masukkan kelas anda      : ")
    _walikelas  = input("Masukkan nama wali kelas : ")
    _ketukelas  = input("Masukkan nama ketua kelas: ")
    _wakilketua = input("Masukkan nama wakil ketua: ")
 
    #Atribut tanpa underscore merupakan atribut public
    serketaris  = input("Masukkan nama serketaris : ")
    

    def biodata(self):
        print("")
        print("PERANGKAT KELAS %s" % self._kelas)
        print("Wali Kelas  : %s" % self._walikelas)
        print("Ketua Kelas : %s" % self._ketukelas)
        print("Wakil Kelas : %s" % self._wakilketua)
        print("Serketaris  : %s" % self.serketaris)

#Proses intansiasi object
run = tkjb()

#Pemanggilan Method
run.biodata()
    
