dosya = open("zDeneme.txt","r")
"""3 fonsiyon var read(Bütün dosyayı alır) readline(Bu sadece tek bir satırı alır) readlines(bu butun satırları lıste seklınde alır)"""

#print(dosya.read()) 
#print(dosya.readline()) 
#print(dosya.readline()) 
#print(dosya.readlines())
liste = dosya.readlines()
print(liste[2]) #2.indisi burda satır olarak kabul goruyor
dosya.close()#isimiz bitince kapatmalıyız

