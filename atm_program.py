import random
import datetime
from custumer import Customer

while True:
    trial = 0
    id = int(input("Masukan pin anda: "))
    atm = Customer(id)
    
    while(id!=atm.cekPin() and trial < 3):
        id = int(input("Pin anda salah. Silahkan masukan lagi: "))
        trial+=1
        if trial==3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()
    
    while True:
        print("Selamat datang di ATM Python")
        print("\n1 - Cek saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        selectMenu = int(input("\nSilahkan pilih menu: "))
        if(selectMenu ==1):
            print("\nSaldo anda sekarang: Rp. "+str(atm.cekBalance())+"\n")
        elif(selectMenu==2):
            nominal = float(input("Input nominal saldo: "))
            verify_withdraw = input("Konfirmasi: anda akan melakukan debet dengan nominal berikut ? y/n "+str(nominal)+" ")
            if(verify_withdraw == "y"):
                print("Saldo awal anda adalah: Rp. "+str(atm.cekBalance())+"")
            else:
                break
            if nominal < atm.cekBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. "+str(atm.cekBalance())+"")
            else:
                print("Maaf. Saldo anda tidak cukup melakukan debet!")
                print("Silahkan melakukan penambahan saldo.")
        elif(selectMenu==3):
            nominal = float(input("Masukan nominal saldo: "))
            verify_deposit = input("Konfirmasi: anda melakukan penyimpanan dengan nominal berikut y/n "+str(nominal)+" ")
            if(verify_deposit=="y"):
                atm.deposite(nominal)
                print("Saldo anda sekarang adalah: Rp."+str(atm.cekBalance())+"\n")
            else:
                break
        elif(selectMenu==4):
            verify_pin = int(input("masukan pin anda:"))
            while(verify_pin!=int(atm.cekPin())):
                break
            updated_pin = int(input("Silahkan masukan pin baru: "))
            verify_newpin = int(input("verify pin baru: "))
            if(updated_pin==verify_newpin):
                print("pin berhasil di ganti")
            else:
                print("pin tidak sama")
        elif(selectMenu ==5):
            print("Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ",random.randint(100000,1000000))
            print("Tanggal: ",datetime.datetime.now())
            print("Saldo terakhir: ",atm.cekBalance())
            print("Terimakasih telah menggunakan ATM python")
            exit()