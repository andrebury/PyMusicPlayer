import os
from tkinter.filedialog import askdirectory
from musicas import *
from tkinter import *
from tkinter import messagebox


class Application:

    def __init__(self, master=None):
        self.musicas = musicas()
        self.tamanho_lista = 0
        self.listofsongs = []
        self.realnames = []
        self.index = 0
        self.album = StringVar()
        self.artista = StringVar()
        self.musica = StringVar()

        self.fonte = ("Verdana", "8")

        self.containerl = Frame(master)
        self.containerl["pady"] = 10
        self.containerl.pack()


        self.containerr = Frame(master)
        self.containerr["pady"] = 10
        self.containerr.pack()


        self.container1 = Frame(self.containerl)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(self.containerl)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(self.containerl)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(self.containerl)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(self.containerl)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(self.containerl)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(self.containerr)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()

        self.titulo = Label(self.container1, text="Music Player")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblmusica = Label(self.container2, text="Título:", font=self.fonte, width=10)
        self.lblmusica.pack(side=LEFT)

        self.txtmusica = Entry(self.container2,textvariable=self.musica)
        self.txtmusica["width"] = 25
        self.txtmusica["font"] = self.fonte
        self.txtmusica.pack(side=LEFT)


        self.lblartista = Label(self.container3, text="Artista:", font=self.fonte, width=10)
        self.lblartista.pack(side=LEFT)

        self.txtartista = Entry(self.container3,textvariable=self.artista)
        self.txtartista["width"] = 25
        self.txtartista["font"] = self.fonte
        self.txtartista.pack(side=LEFT)

        self.lblalbum = Label(self.container4, text="Album:", font=self.fonte, width=10)
        self.lblalbum.pack(side=LEFT)

        self.txtalbum = Entry(self.container4,textvariable=self.album)
        self.txtalbum["width"] = 25
        self.txtalbum["font"] = self.fonte
        self.txtalbum.pack(side=LEFT)

        self.btnCarrega = Button(self.container8, text="Carrega", font=self.fonte, width=12)
        self.btnCarrega.pack(side=LEFT)
        self.btnCarrega["command"] = self.directorychooser

        self.btnPlay = Button(self.container8, text="Play", font=self.fonte, width=12)
        self.btnPlay.pack(side=LEFT)
        self.btnPlay["command"] = self.btnplaymethod

        self.btnStop = Button(self.container8, text="Stop", font=self.fonte, width=12)
        self.btnStop.pack(side=LEFT)
        self.btnStop["command"] = self.btnstopmethod

        self.btnNext = Button(self.container8, text="Next", font=self.fonte, width=12)
        self.btnNext.pack(side=RIGHT)
        self.btnNext["command"] = self.btnnextmethod

        self.btnPrevious = Button(self.container8, text="Prev", font=self.fonte, width=12)
        self.btnPrevious.pack(side=RIGHT)
        self.btnPrevious["command"] = self.btnprevmethod

        self.btnSalva = Button(self.container8, text="Salva", font=self.fonte, width=12)
        self.btnSalva.pack(side=RIGHT)
        self.btnSalva["command"] = self.cadastrar_ID3

        self.listbox = Listbox(self.container9, width=80, selectmode=SINGLE)
        self.listbox.bind("<Double-Button-1>", self.curselet)
        self.scrollbar = Scrollbar(self.container9, orient="vertical")
        #
        # self.btnPlay.bind(Event, self.btnplaymethod)
        # self.btnStop.bind(Event, self.btnstopmethod)
        # self.btnPlay.bind(Event, self.btnnextmethod)
        # self.btnPlay.bind(Event, self.btnprevmethod)
        # self.btnPlay.bind(Event, self.btnarquivosmethod)


    def curselet(self, event):
        widget = event.widget
        selection = widget.curselection()
        print(selection)
        self.musicas.paraamusica()
        self.index = selection[0]
        self.mostrar_ID3()
        self.musicas.playsong(self.listofsongs, self.index)


    def directorychooser(self):
        # askdirectory é um método do Tkinter que abre uma janela para escolher o diretorio
        directory = askdirectory()
        os.chdir(directory)
        self.listbox.pack(side=LEFT)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        # change directory para o diretório escolhido
        # lista todos os arquivos e se for mp3, ele coloca a tag id3 de nome da música
        # realnames é o nome dos arquivos mp3
        # listofsongs tbem
        self.tamanho_lista = 0
        for files in os.listdir(directory):
            if files.endswith(".mp3"):
                realdir = os.path.realpath(files)
                # audio = ID3(realdir)
                # realnames.append(audio['TIT2'].text[0])
                self.listofsongs.append(files)
                self.listbox.insert(self.tamanho_lista, files)
                self.tamanho_lista += 1
        print(self.listofsongs)



    def btnplaymethod(self):
        self.mostrar_ID3()
        self.musicas.playsong(self.listofsongs, self.index)


    def btnstopmethod(self):
        self.mostrar_ID3()
        self.musicas.stopsong()

    def btnnextmethod(self):
        if self.index + 1 < len(self.listofsongs):
            print("antes " + str(self.index))
            self.index = self.index + 1
            print("depois " + str(self.index))
            self.mostrar_ID3()
            self.musicas.nextsong(self.listofsongs, self.index)
        else:
            messagebox.showinfo("MP3 Player", "Essa é a última música")
        print (self.listofsongs)
        print(self.index)

    def btnprevmethod(self):
        if self.index != 0:
            self.index =- 1
            self.mostrar_ID3()
            self.musicas.prevsong(self.listofsongs, self.index)
        else:
            messagebox.showinfo("MP3 Player", "Essa é a primeira música")

    def btnarquivosmethod(self):
        self.directorychooser()
        self.mostrar_ID3()

    def cadastrar_ID3(self):
        print("cadastrado")
        """self.musica = self.txtmusica["text"]
        self.artista = self.txtartista["text"]
        self.album = self.txtalbum["text"] """

        self.musicas.salvaID3(
            self.txtartista.get(), 
            self.txtalbum.get(),
            self.txtmusica.get(),
            self.listofsongs[self.index]
            )
        self.mostrar_ID3()

    def mostrar_ID3(self):        
        print(self.listofsongs[self.index])
        songInfo = self.musicas.pegaTagsID3(self.listofsongs[self.index])
        self.musica = songInfo['ID3TagV2']['song']
        self.artista = songInfo['ID3TagV2']['artist']
        self.txtmusica.delete(0, END)
        self.txtartista.delete(0, END)


        self.txtmusica.insert(0, self.musica)
        self.txtartista.insert(0, self.artista)

        print(songInfo['ID3TagV2']['artist'])
        print(songInfo['ID3TagV2']['song'])

root = Tk()
Application(root)
root.mainloop()