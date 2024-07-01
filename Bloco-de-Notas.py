from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from os.path import dirname

class Master(Tk):
    def __init__(self, width=int, height=int, title=str, resizable=bool,icon=str):
        super().__init__()
        self.title(title)
        self.iconphoto(True, PhotoImage(file=dirname(__file__) + '/resources/icon.png'))
        self.minsize(width, height)
        self.resizable(resizable,resizable)
        self.config(menu= MenuBar(self))
        self.style()

    def themeClear(self):
       self.style.configure('.', background= "#ffffff")

    def themeDark(self):
        self.style.configure('.', background= "black")#171717 #002240

    def style(self):
        self.style= Style(self)
        self.style.configure('.', side="top", fill= "both", expand=True)

#Barra de menu
class MenuBar(Menu):
    def __init__(self, master):
        super().__init__(master)
        #Criando seus submenus
        self.menuFile= Menu(self,tearoff=0)
        self.menuEdit= Menu(self,tearoff=0)
        self.menuConfig= Menu(self,tearoff=0)
        self.menuHelp= Menu(self,tearoff=0)
        #Configurando submenus
        #Arquivo
        self.menuFile.add_command(label="Novo",accelerator="Ctrl+N",command= self.newFile)
        self.menuFile.add_command(label="Abrir...",accelerator="Ctrl+O",command= self.openFile)
        self.menuFile.add_command(label="Salvar", accelerator="Ctrl+S",command=None)
        self.menuFile.add_command(label="Salvar como...", accelerator="Ctrl+Shift+S",command=None)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Sair", command= master.destroy)
        self.add_cascade(label="Arquivo",menu=self.menuFile)
        #Editar
        self.menuEdit.add_command(label="Localizar",command=None)
        self.menuEdit.add_command(label="Substituir", command=None)
        self.menuEdit.add_command(label="desfazer", command=None)
        self.menuEdit.add_command(label="selecionar tudo", command= None)
        self.add_cascade(label="Editar", menu=self.menuEdit)
        #Configurações
        self.menuConfig.add_command(label="personalizar estilos...",command=self.customizeStyles)
        self.add_cascade(label="Configurações", menu=self.menuConfig)
        #Ajuda
        self.menuHelp.add_command(label="Sobre o Notepad", command= self.about)
        self.add_cascade(label="Ajuda", menu= self.menuHelp)

    def newFile(self):
        global Master,App
        newMaster = Master(400, 500,"Notepad",True)
        app= App(newMaster)
        newMaster.mainloop()

    def openFile(self):
        from os import getcwd
        from tkinter import filedialog
        #Importando arquivos TXT/DOCX
        '''
        Definindo:
            -Diretorio inicial do explorador de arquivos
            -Titulo da aba
            -Tipos de arquivos aceitaveis(.pdf/.txt)
        ''' 
        filedir= filedialog.askopenfilename(initialdir= getcwd(),
                                             title="selecionar arquivo",
                                             filetype=(("Txt File", ".txt"),
                                             ("Doc File", ".docx"),
                                             ("All File", ".*")))
    
        #Abrindo arquivo selecionado
        with open(filedir,"r") as file:
            global app
            #Lendo os dados do arquivo selecionado
            #Adicionando  os dados do arquivo selecionado na entrada de texto
            fileText= file.read()        
            app.text.insert('1.0', fileText)
        return filedir
        
    def customizeStyles(self):
        global master
        
        newMaster = Toplevel()
        newMaster.minsize(400,160)
        newMaster.resizable(False,False)

        #FONTES
        fontFrame= LabelFrame(newMaster, text="Estilo de Fontes",labelanchor="nw")
        fontFrame.pack(fill="both", expand=True)


        fontFamilyFrame= Frame(fontFrame)
        fontFamilyFrame.place(relx=.1,rely=.1)

        Label(fontFamilyFrame, text="Font-Family:",font="-size 10").pack(anchor="nw", padx=10)
        Combobox(fontFamilyFrame,values=["Arial", "times New Roman","Comic Sans"]).pack(anchor="nw", padx=10)

        sizeFrame= Frame(fontFrame)
        sizeFrame.place(relx=.5,rely=.1)
        Label(sizeFrame, text="Size:",font="-size 10").pack(anchor="nw", padx=20)
        Combobox(sizeFrame,values=[n for n in range(2,30,2)], width= 2).pack(anchor="nw", padx=20)

        colorFrame= Frame(fontFrame)
        colorFrame.place(relx=.78,rely=.1)
        Label(colorFrame, text="Color:",font="-size 10").pack(anchor="nw")
        Button(colorFrame,width=5,command=None).pack(anchor="nw")

        #TEMAS
        themeFrame = LabelFrame(newMaster, text="Tema",labelanchor="nw")
        themeFrame.pack(fill="both", expand=True)

        butonFrame1= Frame(themeFrame)
        butonFrame2= Frame(themeFrame)
        butonFrame1.place(relx=.1,rely=.1)
        butonFrame2.place(relx=.5,rely=.1)
        Button(butonFrame1,text="Theme light", width=15,command=master.themeClear).pack(anchor="nw", padx=10, pady=10)
        Button(butonFrame2,text="Theme Dark", width=15,command=master.themeDark).pack(anchor="nw", padx=20, pady=10)

    def about(self):
        from webbrowser import open_new
        newMaster= Toplevel()   
        newMaster.minsize(410,200)
        newMaster.resizable(False,False)
        
        newMaster.grid_rowconfigure(1, weight=3)
        newMaster.grid_columnconfigure(1, weight=3)
        #Imgs
        icon=PhotoImage(file=dirname(__file__) + '/resources/icon 64x64.png')
        Label(newMaster,image=icon).grid(row=0, column=0)
        Label(newMaster,image=icon).grid(row=0, column=2)
        #Texto
        Label(newMaster,text="Simple Notes",font="-weight bold -size 25 -underline True").grid(row=0, column=1)
        Label(newMaster,text="Criado e licensiado por Abel Lucas, \nPara mais informações acesse o \nmeu protifolio." ,font="-size 12 ", justify="left").grid(row=1, column=1)
        #Botões
        Button(newMaster,text="Instagram",command= lambda: open_new("https://www.instagram.com/abelarduu/")).grid(row=2, column=0,sticky='ew')
        Button(newMaster,text="Github", command= lambda: open_new("https://github.com/abelarduu")).grid(row=2, column=1,sticky='ew')
        Button(newMaster,text="Linkedin",command= lambda:open_new("https://www.linkedin.com/in/Abel-Lucas/")).grid(row=2, column=2,sticky='ew')
        newMaster.mainloop()

class App:
    def __init__(self, master):
        #Entrada de texto
        self.text = ScrolledText(master, width=50,wrap= WORD, height=10)
        self.text.pack(fill="both", side=LEFT, expand=True)

if __name__== "__main__":
    master = Master(400, 500,"Bloco de Notas",True)
    app= App(master)
    master.mainloop()