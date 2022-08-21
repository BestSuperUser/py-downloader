from fileinput import filename
import os
from pytube import YouTube, Playlist
isPlaylist = input("Playlist mi ? (değilse enter basın): ")
if(isPlaylist):
    plLink = input("Playlist linki: ")
    quality = input("Video kalitesi ? (...720p / 480p / 360p / 240p / 144p): ")
    isNumericName = input("İsimlendirme numeric mi olsun ? (hayırsa boş bırak): ")
    pl = Playlist(plLink)
    i = 1
    if (isNumericName):
        for video in pl.videos:
            try: 
                video.streams.filter(resolution=quality).first().download(filename=str(i)+".mp4")
            except:
                print("İstediğiniz çözünürlük bulunamadı en büyük çözünürlükle indiriliyor.")
                try: 
                    video.streams.get_highest_resolution().download(filename=str(i)+".mp4")
                except:
                    print("Bir şeyler ters gitti.")
            print(str(i) + ". video indi.")
            i = i+1
    else:
        for video in pl.videos:
            try: 
                video.streams.filter(resolution=quality).first().download()
            except:
                print("İstediğiniz çözünürlük bulunamadı en büyük çözünürlükle indiriliyor.")
                try: 
                    video.streams.get_highest_resolution().download()
                except:
                    print("Bir şeyler ters gitti.")
            print(str(i) + ". video indi.")
            i = i+1
        
else:
    videoLink = input("Video linkini girin: ")
    quality = input("Video kalitesi ? (...720p / 480p / 360p / 240p / 144p): ")
    video = YouTube(videoLink)
    try: 
        video.streams.filter(resolution=quality).first().download()
    except:
        print("İstediğiniz çözünürlük bulunamadı en büyük çözünürlükle indiriliyor.")
        try: 
            video.streams.get_highest_resolution().download()
        except:
            print("Bir şeyler ters gitti.")
    print("video indi.")