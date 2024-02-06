import pyautogui
import time
import keyboard
# Gerekli Kütüphanelerimizi Dahil Ettik

# Tarayıcıya Dönebilmek Adına 3sn Uykuya Aldık
time.sleep(3)

# Gerekli Değişkenlerimizi Tanımladık
cursor_counter = 0
grandma_counter = 0
for_counter = 100

# clickCookie Fonksiyonumuzu Oluşturduk
def clickCookie():
    # for_counter Değişkeninin global Olduğunu
    # Kodumuza Bildirdik
    global for_counter
    
    # Ekranda "cookie.png" Resmi Varmı Diye Kontrol Ettik
    # 'confidence' yani benzerlik oranını %80 olarak ayarladık
    # Eğer 'cookie.png' dosyasına %80 oranında benzerlik sağlayan
    # Herhangi Bir şey varsa Onun Koordinat Bilgilerini Alacak ve
    # 'cookie' Değişkenine Atayacak
    cookie = pyautogui.locateOnScreen("cookie.png", confidence=0.8)
    
    # 'cookie' Değişkeninin Olduğu Koordinata
    #Mouse'umuzu Götürüyoruz
    pyautogui.moveTo(cookie)

    # for_counter Değerimizi 100 Verdik
    # Buda 100 Kere Çalışacağı Anlamına Gelir
    for i in range(int(for_counter)):
        # Click İşlemini Yaparak Cookie'ye Tıklamasını Sağladık
        pyautogui.click()
        # Eğer F9 Tuşuna Basıldıysa break Atıp Koddan Çıkmasını Sağladık
        if keyboard.is_pressed("F9"):
            print("Program Durduruldu!")
            break
    
    # for_counter Değerinin Üstüne Kendinin %20 Fazlasını Ekledik
    # Örneğin 100 ise, 100'ün üstüne %20sini ekledik yani
    #100 += 20 ile Aynı Anlama Geliyor
    for_counter += for_counter * 0.2 
    
# Oyundayken Ekranın Sağ Tarafında ki Cursor Elementine
# Tıklaması İçin Gerekli İşlemleri Yaptık
def cursorController():
    # cursor_counter Değişkenimizin global Olduğunu Belirttik
    global cursor_counter
    # Eğer Ekranda 'cursor.png' Resmine %95 Oranla Benzeyen Bir şey
    # Var İse Bunu 'cursor' Değişkenine Atadık
    cursor = pyautogui.locateOnScreen("cursor.png", confidence=0.95)
    # Eğer 'cursor_counter' değişkeni 100'den Küçük ise ve 'cursor'
    # Değişkeni True, Tespit Edilebilmiş Durumda ise
    if cursor_counter < 100 and cursor:
        # 'cursor' Değişkeninde Bulunan Koordinatlara
        # Gitmesini Sağladık
        pyautogui.moveTo(cursor)
        # Gittiği Koordinata 2 Kere Tıklamasını Sağladık
        # (cursor elementine tıklattık)
        pyautogui.click(clicks=2)
        # 'cursor_counter' Değişkenine 2 Ekledik
        cursor_counter += 2
        # Ekrana Bilgilendirme Yazısını Yazdırdık
        print("[+]Satın Alınan Toplam Cursor:", cursor_counter)
    # Ek Seçenek Olarak 'cursor_counter' büyükse veya
    # Eşitse 100'e
    elif cursor_counter >= 100:
        # Ekranda Bilgilendirme Geçtik
        print("[-]100 Adet Cursor Satın Alındığı İçin Daha Fazla Alınamıyor...")
        # Aynı İşlemleri 'grandma' Elementi İçinde Yaptığımız
        # Fonksiyonu Çağırdık
        grandmaController()
    else:
        # Oyun Başında 'cursor' Elementini Görmeyeceği İçin
        # Olumsuz Durum İçin Ekrana Bilgilendirme Geçiyoruz
        print("[-]Oyun Başı Olduğu İçin Cursor Görülemiyor...")

# 'cursor' Elementinde Yapılan İşlemlerin Aynısını
# 'grandma' Elementi İçinde Yapıyoruz
def grandmaController():
    global grandma_counter
    grandma = pyautogui.locateOnScreen("grandma.png", confidence=0.95)
    if  grandma_counter < 200 and grandma:
        pyautogui.moveTo(grandma)
        pyautogui.click(clicks=1)
        grandma_counter += 1
        print("[+]Satın Alınan Toplam Grandma:", grandma_counter)
    elif grandma_counter >= 200:
        print("[-]200 Adet Grandma Satın Alındığı İçin Daha Fazla Alınamıyor...")
    else:
        print("[-]Oyun Başı Olduğu İçin Grandma Görülemiyor...")
        

# Döngünün Kaç Kere Devam Ettiğini Öğrenmek Adına 'sayac'
# Değişkeni Oluşturduk
sayac = 0

# Sonsuz Döngüyü Açtık
while True:
    # Eğer F9 Tuşuna Basıldıysa Programdan Çıkış Yaptık
    if keyboard.is_pressed("F9"):
        print("Program Durduruldu!")
        break
    # Sayacın Üstüne 1 Ekledik
    sayac += 1

    # Fonksiyonlarımızı Çalıştırdık
    cursorController()
    clickCookie()
    # Döngünün Kaçıncı Kez Döndüğünü Ekrana Yazdırdık
    print("[!]Döngü", sayac, "Kere Tekrar Etti")
