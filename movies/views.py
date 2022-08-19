from django.shortcuts import render

kategori_liste = ["macera","romantik","dram","bilimkurgu"]
film_liste=[
    
    {
        "film_adı":"film 1",
        "aciklama":"film_1 açıklama",
        "resim":"1.jpeg",
        "anasayfa":True
    },
    {
        "film_adı":"film 2",
        "aciklama":"film_2 açıklama",
        "resim":"2.jpeg",
        "anasayfa":True

    },
    {
        "film_adı":"film 3",
        "aciklama":"film_3 açıklama",
        "resim":"3.jpeg",
        "anasayfa":False

    },
    {
        "film_adı":"film 4",
        "aciklama":"film_4 açıklama",
        "resim":"4.jpeg",
        "anasayfa":False

    }
   
    
    ]

def home(request):
    data = {
        "kategoriler":kategori_liste,
        "filmler":film_liste
    }
    return render(request, "index.html",data)

def movies(request):
    data = {
        "kategoriler":kategori_liste,
        "filmler":film_liste
    }
    return render(request, "movies.html",data)