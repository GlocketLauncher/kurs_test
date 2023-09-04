print("ecnebice sözcükler sözlüğü")
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "MEME": "Komik video veya fotoğraflar",
            "DOUBLE": "Çift anlamına gelir",
            "OKEY": "Onay vermek için kullanılır"
            }
while True:    
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("kelime yok")

    soru = input("devam etmek için y,sözlüğü kapatmak için n yazın")
    if soru == "y":
        print("devam")
    elif soru == "n":
        break

