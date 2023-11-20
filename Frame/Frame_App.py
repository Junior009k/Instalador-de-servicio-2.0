import tkinter as tk 
from tkinter import ttk
from tkinter import Frame,Radiobutton
from Frame.Component.comboBox import cargarDatos
import tkinter.filedialog

class Frame_App:
    def Examine(self):
        Path = tkinter.filedialog.askopenfilename()
        self.pathLabel.config(text=Path) 
        #if(p==1 and validateService(Path.lower(),"sidesys.services.applicationservice.exe","middleware","bin")):label1.config(text=Path) 
    def __init__(self,titulo):
        self.primeraVez=True
        self.m=tk.Tk()
        self.frameSidebarUP=Frame(self.m)
        self.frameSidebarDown=Frame(self.m)
        self.frameNavbar=Frame(self.m)
        self.frameContent=Frame(self.m)
        self.m.config(bg="#FFF") 
        self.frameSidebarUP.config() 
        self.frameSidebarDown.config() 
        self.frameNavbar.config() 
        self.frameContent.config() 
        self.titulo = tk.Label(self.frameSidebarUP,text=titulo,pady=8,bg="#fff",fg="#000")
        self.boton_eFlow=tk.Button(self.frameSidebarDown,pady=8,text="e-Flow",command=lambda:self.accion_boton("e-Flow"),width=20)
        self.boton_Citas=tk.Button(self.frameSidebarDown,pady=8,text="Citas",command=lambda:self.accion_boton("Citas"),width=20)
        self.boton_Encuesta=tk.Button(self.frameSidebarDown,pady=8,text="Encuestas",command=lambda:self.accion_boton("Encuestas"),width=20)
        self.boton_Reportes=tk.Button(self.frameSidebarDown,pady=8,text="Reportes",command=lambda:self.accion_boton("Reportes"),width=20)
        self.boton_Client=tk.Button(self.frameSidebarDown,pady=8,text="Client",command=lambda:self.accion_boton("Client"),width=20)
        self.boton_Automatizador=tk.Button(self.frameSidebarDown,pady=8,text="Automatizador",command=lambda:self.accion_boton("Automatizador"),width=20)
        self.combo = ttk.Combobox(self.frameNavbar,
                state="readonly"
            )
          
        pass
    
    def accion_boton(self,text):
        if(self.primeraVez):self.cargarContenido()
        self.titulo.config(text=text)
        self.combo.config(values=cargarDatos(text))
    def accion_Combo(self,event):
        print(self.combo.get())
        if self.actual=="Instalador de servicio":
            self.borrarFrame1()
        if self.combo.get()=="Instalador de servicio":
            self.cargaFrame1()
        self.actual=self.combo.get()
    def mostrarFrame(self):
        self.frameSidebarUP.place(x=0,y=0,width=200,height=100)
        self.frameSidebarDown.place(x=0,y=100,width=200,height=400)
        self.frameNavbar.place(x=200,y=0,width=578,height=60)
        self.frameContent.place(x=200,y=60,width=578,height=440)
        self.titulo.pack(expand=True, fill=tk.BOTH)
        self.boton_eFlow.pack(padx=5,pady=8)
        self.boton_Citas.pack(padx=5,pady=8)
        self.boton_Encuesta.pack(padx=5,pady=8)
        self.boton_Reportes.pack(padx=5,pady=8)
        self.boton_Client.pack(padx=5,pady=8)
        self.boton_Automatizador.pack(padx=5,pady=8)
        self.combo.pack()
        
    
    def inicializarApp(self):
        self.m.geometry("768x500")
        self.mostrarFrame()
        self.m.mainloop()
        
    def cargarContenido(self):
        self.actual=0
        self.combo.bind('<<ComboboxSelected>>', self.accion_Combo)
        self.pathLabel = tk.Label(self.frameContent,text="") #se agregan las etiquetas al frame
        self.pathLabel.place(x=40,y=125)
        
        self.boton_buscar = tk.Button(self.frameContent,text="Buscar", command=lambda:self.Examine()).place(x=40,y=150)
        
    def cargaFrame1(self):
        self.R1 = Radiobutton(self.frameContent,text="Manual", value=1)
        self.R2 = Radiobutton(self.frameContent, text="Automatico", value=2)
        self.R1.place(x=0,y=40)
        self.R2.place(x=0,y=60)
        self.Titulo = tk.Label(self.frameContent,text="Instalador de servicios Unicos",pady=12)
        self.Titulo.place(x=75,y=0)
        self.Textbox = tk.Entry(self.frameContent,width=60)
        self.Textbox.insert(1,"e-Flow MiddleWare Service")
        self.Textbox.place(x=40,y=100)
        self.boton_Ejecutar = tk.Button(self.frameContent,text="Ejecutar", command=lambda:executeScript())
        self.boton_Ejecutar.place(x=90,y=150)
    def borrarFrame1(self):
        self.R1.destroy()
        self.R2.destroy()
        self.Titulo.destroy()
        self.Textbox.destroy()
        self.boton_Ejecutar.destroy()
                 
        
