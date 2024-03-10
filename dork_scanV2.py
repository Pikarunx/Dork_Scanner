import os
from colorama import Fore, Style, init
from googlesearch import search
import pyfiglet
import time


logo = """oooooooooo.     .oooooo.   ooooooooo.   oooo    oooo       .oooooo..o   .oooooo.         .o.       ooooo      ooo ooooo      ooo oooooooooooo ooooooooo.   
`888'   `Y8b   d8P'  `Y8b  `888   `Y88. `888   .8P'       d8P'    `Y8  d8P'  `Y8b       .888.      `888b.     `8' `888b.     `8' `888'     `8 `888   `Y88. 
 888      888 888      888  888   .d88'  888  d8'         Y88bo.      888              .8"888.      8 `88b.    8   8 `88b.    8   888          888   .d88' 
 888      888 888      888  888ooo88P'   88888[            `"Y8888o.  888             .8' `888.     8   `88b.  8   8   `88b.  8   888oooo8     888ooo88P'   CODED BY:PİKARUN
 888      888 888      888  888`88b.     888`88b.              `"Y88b 888            .88ooo8888.    8     `88b.8   8     `88b.8   888    "     888`88b.    
 888     d88' `88b    d88'  888  `88b.   888  `88b.       oo     .d8P `88b    ooo   .8'     `888.   8       `888   8       `888   888       o  888  `88b.  
o888bood8P'    `Y8bood8P'  o888o  o888o o888o  o888o      8""88888P'   `Y8bood8P'  o88o     o8888o o8o        `8  o8o        `8  o888ooooood8 o888o  o888o  
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           """
print(Fore.RED + logo + Style.RESET_ALL)

while True:
    dork = input(Fore.GREEN + "[+]Taranacak Olan Dorku Girin.Çıkmak İçin exit YAzın:")

    if dork == "exit":
        print(Fore.RED +  "Tooldan Çıkış Yapılıyor.." + Style.RESET_ALL)
        time.sleep(1)
        break

    else:
        print(Fore.GREEN + "Bulunan Web Siteleri:" + Style.RESET_ALL)
        time.sleep(1)
        bulunan_siteler = list(search(dork))  # Search sonuçlarını listeye çevir

        for url in bulunan_siteler:
            print(Fore.RED + url + Style.RESET_ALL)

        kaydet = input(Fore.BLUE + "Çıktıyı Kaydetmek İster Misiniz[E/H]:" + Style.RESET_ALL)
        if kaydet.lower() == "e":
            dosya_adi = input(Fore.MAGENTA + "Çıktının Kaydedileceği Adı Girin:" + Style.RESET_ALL)
            with open(dosya_adi, 'w', encoding='utf-8') as f:
                for url in bulunan_siteler:
                    f.write(url + "\n")

            print(Fore.LIGHTBLACK_EX + "Başarılı Bir Şekilde Kaydedildi." + Style.RESET_ALL)

        elif kaydet.lower() == "h":
            continue

        else:
            print(Fore.RED + "Hatalı Seçim Yapıldı.Tooldan Çıkış Yapılıyorr..." + Style.RESET_ALL)
            time.sleep(1)


    

#The End  