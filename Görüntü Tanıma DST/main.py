import pyautogui 
import time 
import keyboard

time.sleep(3)

# Oyunda ki resimler gif şeklinde ve zaman zaman arkaplanı değiştiği için 23 farklı fotoğraf aldık
# İsterseniz Çoğaltıp Azaltabilirsiniz.
dallar = ["dal_1.png", "dal_2.png", "dal_3.png", "dal_4.png", "dal_5.png", "dal_6.png", "dal_7.png",
          "dal_8.png", "dal_9.png", "dal_10.png", "dal_11.png", "dal_12.png", "dal_13.png",
          "dal_14.png", "dal_15.png", "dal_16.png", "dal_17.png", "dal_18.png", "dal_19.png",
          "dal_20.png", "dal_21.png", "dal_22.png", "dal_23.png"]

# oyunda dal toplamasını istediğim için 'dal_topla' adında fonksiyon oluşturdum
def dal_topla():
    # bir sayaç belirledik
    sayac = 0
    
    # sonsuz defa çalışsın istediğim için while döngümüzü açtık
    while True:

        #dallarımı tek tek oyunda taradık ve benzerlik oranını %70 yaptık
        # grayscale diyerek rengi gri tonda tararttık
        dal = pyautogui.locateOnScreen(dallar[0], confidence=0.7, grayscale=True)
        dal_2 = pyautogui.locateOnScreen(dallar[1], confidence=0.7, grayscale=True)
        dal_3 = pyautogui.locateOnScreen(dallar[2], confidence=0.7, grayscale=True)
        dal_4 = pyautogui.locateOnScreen(dallar[3], confidence=0.7, grayscale=True)
        dal_5 = pyautogui.locateOnScreen(dallar[4], confidence=0.7, grayscale=True)
        dal_6 = pyautogui.locateOnScreen(dallar[5], confidence=0.7, grayscale=True)
        dal_7 = pyautogui.locateOnScreen(dallar[6], confidence=0.7, grayscale=True)
        dal_8 = pyautogui.locateOnScreen(dallar[7], confidence=0.7, grayscale=True)
        dal_9 = pyautogui.locateOnScreen(dallar[8], confidence=0.7, grayscale=True)
        dal_10 = pyautogui.locateOnScreen(dallar[9], confidence=0.7, grayscale=True)
        dal_11 = pyautogui.locateOnScreen(dallar[10], confidence=0.7, grayscale=True)
        dal_12 = pyautogui.locateOnScreen(dallar[11], confidence=0.7, grayscale=True)
        dal_13 = pyautogui.locateOnScreen(dallar[12], confidence=0.7, grayscale=True)
        dal_14 = pyautogui.locateOnScreen(dallar[13], confidence=0.7, grayscale=True)
        dal_15 = pyautogui.locateOnScreen(dallar[14], confidence=0.7, grayscale=True)
        dal_16 = pyautogui.locateOnScreen(dallar[15], confidence=0.7, grayscale=True)
        dal_17 = pyautogui.locateOnScreen(dallar[16], confidence=0.7, grayscale=True)
        dal_18 = pyautogui.locateOnScreen(dallar[17], confidence=0.7, grayscale=True)
        dal_19 = pyautogui.locateOnScreen(dallar[18], confidence=0.7, grayscale=True)
        dal_20 = pyautogui.locateOnScreen(dallar[19], confidence=0.7, grayscale=True)
        dal_21 = pyautogui.locateOnScreen(dallar[20], confidence=0.7, grayscale=True)
        dal_22 = pyautogui.locateOnScreen(dallar[21], confidence=0.7, grayscale=True)
        dal_23 = pyautogui.locateOnScreen(dallar[22], confidence=0.7, grayscale=True)
        
        # eğer dal none'a eşit değilse yani dal'ı tanıdıysa
        if dal != None:
            # Ekrana çıktı verdik
            print("[+]Dal Göründü Alınıyor.")
            # yarım saniye uyuttuk
            time.sleep(0.5)
            # dal'ın olduğu koordinata mouse'ı 2 saniye de götürdük 
            pyautogui.moveTo(dal, duration=2)
            time.sleep(0.3)
            # 3 salise beklettik
            pyautogui.click()
            #tıkladık
            time.sleep(3.5)
            # 3.5 saniye beklettik
        # aynı işlemi 22 kere daha elif ile tekrar ettik
        
        elif dal_2 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_2, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_3 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_3, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_4 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_4, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_5 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_5, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_6 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_6, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_7 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_7, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_8 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_8, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_9 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_9, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_10 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_10, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_11 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_11, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_12 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_12, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_13 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_13, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_14 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_14, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_15 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_15, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_16 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_16, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_17 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_17, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_18 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_18, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_19 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_19, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
        
        elif dal_20 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_20, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_21 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_21, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)
            
        elif dal_22 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_22, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        elif dal_23 != None:
            print("[+]Dal Göründü Alınıyor.")
            time.sleep(0.5)
            pyautogui.moveTo(dal_23, duration=2)
            time.sleep(0.3)
            pyautogui.click()
            time.sleep(3.5)

        # eğer dal tanınmadıysa
        else:
            
            # eğer sayaç 4'e eşitse
            # 4 kere q harfine basıp ekranı normal haline döndürecek
            #ve sayacı sıfırlayıp 2 saniye boyunca w tuşuna basacak 
            if sayac == 4:
                time.sleep(0.3)
                pyautogui.press("q")
                time.sleep(0.3)
                pyautogui.press("q")
                time.sleep(0.3)
                pyautogui.press("q")
                time.sleep(0.3)
                pyautogui.press("q")
                time.sleep(0.3)
                sayac = 0
                time.sleep(0.5)
                pyautogui.keyDown("W")
                time.sleep(2)
                pyautogui.keyUp("W")
                # continue ile döngüyü yarıda kesip başa saracak
                continue
            
            # eğer sayaç 4'e eşit değilse
            # 1 salise bekletip e tuşuna basıp sayacı 1 arttıracak
            # 2 saniye boyunca w tuşuna basacak
            else:
                time.sleep(0.1)
                pyautogui.press("e")
                sayac += 1
                pyautogui.keyDown("W")
                time.sleep(2)
                pyautogui.keyUp("W")

dal_topla()