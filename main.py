from tkinter import *
from tkinter import filedialog
import pygame

root = Tk()
root.title('MP3 PLAYER')
root.geometry("500x300")

pygame.mixer.init()

song_box = Listbox(root, bg="black", fg="red", width=80, selectbackground="silver", selectforeground="black")
song_box.pack(pady=20)


def add_song():
    song = filedialog.askopenfilename(initialdir='c:/gui/', title='Choose a song', filetypes=(("mp3 Files", "*.mp3"),))
    song = song.replace("C:/gui/", "")
    song = song.replace(".mp3", "")

    song_box.insert(END, song)


def play():
    song = song_box.get(ACTIVE)
    song = f'C:/gui/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)


global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='c:/gui/', title='Choose a song',
                                        filetypes=(("mp3 Files", "*.mp3"),))

    for song in songs:
        song = song.replace("C:/gui/", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)


def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0] + 1
    song = song_box.get(next_one)
    song = f'c:/gui/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.select_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last=None)


def previous_song():
    next_one = song_box.curselection()
    next_one = next_one[0] - 1
    song = song_box.get(next_one)
    song = f'c:/gui/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.select_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last=None)


def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()


back_btn_img = PhotoImage(file='c:/gui/Skip Back.png')
forward_btn_img = PhotoImage(file='c:/gui/Skip Fwd.png')
pause_btn_img = PhotoImage(file='c:/gui/Pause.png')
play_btn_img = PhotoImage(file='c:/gui/Play.png')
stop_btn_img = PhotoImage(file='c:/gui/stop.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)

back_button.grid(row=0, column=0, padx=5)
play_button.grid(row=0, column=1, padx=5)
pause_button.grid(row=0, column=2, padx=5)
stop_button.grid(row=0, column=3, padx=5)
forward_button.grid(row=0, column=4, padx=5)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist", command=add_song)
add_song_menu.add_command(label="Add all songs to playlist", command=add_many_songs)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete song", command=delete_song)
remove_song_menu.add_command(label="Delete all song", command=delete_all_songs)

root.mainloop()
