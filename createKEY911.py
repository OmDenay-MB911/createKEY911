import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'+'*60)
print(a+'\t        Tombol Tambahan Termux ')
print(a+'\t        UP,HOME,LEFT, CTRL, AUTO ')
print(b+'\t      Create Bye Om Denay Zee Dagama ')
print(a+'+'*60)
print('\t     Whatsapp : 085930060122')
print('\t      Youtube : MENEMBUS BATAS 911')
print('\t      Github  : https://github.com/OmDenay-MB911')
print(a+'+'*60)
print('\nProses..')
print(a+'+'*60)
sleep(1)
print(b+'\n[!] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] menambahkan File Tambahan..')
sleep(1)

key = "extra-keys =[['chmod','$HOME/','wget','pkg','install','apt','git clone','exit'],['ESC','w3m','bash','python2','HOME','UP','nano','cd'],['python','cd /sdcard','CTRL','ALT','LEFT','DOWN','RIGHT','ls']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Memproses  !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !! ^^'+c+'\n\nsubscribe dan share channel MENEMBUS BATAS 911*\n\n')
print(a+'+'*60)
