##İnternetten fotograf ındırme
import urllib.request 
url1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSjpqS9RwvPKLltMzuwa6xz6D3PDH1ixlwzgKuGfDE_0Jvya1Af"
urlliste = [url1]
for url in urlliste:
    urllib.request.urlretrieve(url, "0Resim"  ".jpg")
    