dosya = open("Yazılım.txt","w") # w:yazmak eger yazılım ısmınde dosya varsa onu sılıp senın yazdıklarını yazar eger oyle degilse dosya yoksa olusturup yazdıkların yazar
dosya.write("Naber")

dosya = open("Yazılım.txt","a")
dosya.write(" ekleme yapildi")

dosya2 = open("Yazılım2.txt","a") #dosya varsa ekleme yapar yoksa olusturup yazar
dosya2.write("iyimisin")
