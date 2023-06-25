from tkinter import *
from tkinter import ttk
class Aplicacion():
    __cantidad1=None
    __cantidad2=None
    __cantidad3=None
    __aniobase1=None
    __aniobase2=None
    __aniobase3=None
    __anioactual1=None
    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.geometry('575x409')
        self.__ventana.title('CalculadoraIPC')
        salir=ttk.Button(self.__ventana, text='Salir',command=self.__ventana.destroy)
        calcular=ttk.Button(self.__ventana, text='CalcularIPC',command=self.calcular)
        item = ttk.Label(self.__ventana, text="Item", padding=(30,20))
        vestimenta = ttk.Label(self.__ventana, text="Vestimenta")
        alimentos = ttk.Label(self.__ventana, text="Alimentos")
        educacion = ttk.Label(self.__ventana, text="Educación")
        cantidad = ttk.Label(self.__ventana, text="Cantidad")
        preciobase = ttk.Label(self.__ventana, text="Precio Año Base")
        precioactual = ttk.Label(self.__ventana, text="Precio Año Actual")
        text1 = ttk.Entry(self.__ventana, textvariable=self.__cantidad1,width=10)
        text2 = ttk.Entry(self.__ventana, textvariable=self.__aniobase1,width=10)
        text3 = ttk.Entry(self.__ventana, textvariable=self.__anioactual1,width=10)
        text4 = ttk.Entry(self.__ventana, textvariable=self.__cantidad2,width=10)
        text5 = ttk.Entry(self.__ventana, textvariable=self.__aniobase2,width=10)
        text6 = ttk.Entry(self.__ventana, textvariable=self.__aniobase3,width=10)
        item.grid(row=0, column=0)
        vestimenta.grid(row=1, column=0)
        text1.grid(row=1, column=1)
        text2.grid(row=1, column=2)
        text3.grid(row=1, column=3)
        text4.grid(row=2, column=1)
        text5.grid(row=2, column=2)
        text6.grid(row=2, column=3)
        alimentos.grid(row=2, column=0, pady=20)
        educacion.grid(row=3, column=0, pady=5)
        cantidad.grid(row=0, column=1, pady=5, padx=20)
        preciobase.grid(row=0, column=2,padx=20, pady=5)
        precioactual.grid(row=0, column=3,padx=20, pady=5)
        salir.grid(row = 5, column = 3, padx=10)
        calcular.grid(row=5, column=2)
    def calcular(self):
        pass
    def ejecutar(self):
        self.__ventana.mainloop()
if __name__ == '__main__':
    app=Aplicacion()
    app.ejecutar()

