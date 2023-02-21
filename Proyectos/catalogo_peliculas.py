import tkinter as tk
from Catalogo_Peliculas.Cliente.gui_app import Frame,barra_menu

def main():
    root = tk.Tk()#creamos una ventana
    root.title("Catalogo de Peliculas")
    root.iconbitmap("Proyectos/Catalogo_Peliculas/imagenes/mini-cd2.ico")
    root.resizable(0,0)#valores booleanos 1 o 0 para permitir o no agrandar la ventana

    barra_menu(root)
    app = Frame(root = root)
    app.mainloop()#tipo break ya que despues de esto no se ejecuta nada mas

if __name__ == '__main__':
    main()