import time
import tkinter
import vlc

url = 'https://stream-relay-geo.ntslive.net/stream'
#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
#Define VLC player
player=instance.media_player_new()
#Define VLC media
media=instance.media_new(url)
#Set player media
player.set_media(media)
playing = False

def toggle_radio():
  global playing
  if not playing:
    player.play()
    playing = True
  else:
    player.stop()
    playing=False

window = tkinter.Tk()
window.title("Radio Player")
window.geometry("500x500")

backgroundImage=tkinter.PhotoImage(file="background.png")
backgroundLabel = tkinter.Label(window, text = "Welcome to My Radio Player!", image=backgroundImage)
backgroundLabel.place(x=0, y=0)

playButtonImage=tkinter.PhotoImage(file="play_button.png")
playButton = tkinter.Button(window, command=toggle_radio)
playButton.config(image=playButtonImage)
playButton.place(x=100, y=100)

window.mainloop()


