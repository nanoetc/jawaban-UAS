from view.input_nilai import *

def ubah():
    pilihan3 = input("masukkan data yang akan diubah : ")
    if pilihan3 == "nim":
        masnim = str(input("masukkan nim :"))
        masnim2 = str(input("masukkan nim yang baru :"))
        for i in range(len(nim)):
            if masnim == nim[i]['nim']:
                nim[i]['nim'] = masnim2
    elif pilihan3 == "nama":
        masnama = str(input("masukkan nama :"))
        masnama2 = str(input("masukkan nama yang baru :"))
        for i in range(len(nama)):
            if masnama == nama[i]['nama']:
                nama[i]['nama'] = masnama2
    elif pilihan3 == "tugas":
        mastugas = str(input("masukkan nilai tugas :"))
        mastugas2 = str(input("masukkan nilai tugas yang baru :"))
        for i in range(len(tugas)):
            if mastugas == tugas[i]['tugas']:
                tugas[i]['tugas'] = mastugas2
    elif pilihan3 == "uts":
        masuts = input("masukkan nilai uts :")
        masuts2 = input("masukkan nilai uts yang baru :")
        for i in range(len(uts)):
            if masuts == uts[i]['uts']:
                uts[i]['uts'] = masuts2
    elif pilihan3 == "uas":
        masuas = str(input("masukkan nilai uas : "))
        masuas2 = input("masukkan nilai uas yang baru :")
        for i in range(len(uas)):
            if masuas == uas[i]['uas']:
                uas[i]['uas'] = masuas2

def hapus():
    masnim = input("masukan nim : ")
    for i in range(len(nim)):
        if masnim == nim[i]['nim']:
            del nim[i]
            del nama[i]
            del tugas[i]
            del uts[i]

def keluar():
    print("pilihan yang anda masukkan tidak ada")

