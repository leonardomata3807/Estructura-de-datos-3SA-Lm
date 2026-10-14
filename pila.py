
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Funcionamiento de una Pila")
ventana.geometry("500x550")

pila = []

def dibujar_pila():
    lienzo.delete("all")

    lienzo.create_text(250, 30, text="PILA (STACK)",
                       font=("Arial", 16, "bold"))

    for i, elemento in enumerate(pila):
        x1 = 150
        y1 = 420 - (i * 50)
        x2 = 350
        y2 = y1 - 40

        lienzo.create_rectangle(x1, y2, x2, y1,
                                fill="lightblue",
                                outline="black")

        lienzo.create_text(250, y2 + 20,
                           text=str(elemento),
                           font=("Arial", 12, "bold"))

    if len(pila) > 0:
        lienzo.create_text(250, 455,
                           text="Tope: " + str(pila[-1]),
                           font=("Arial", 11))
    else:
        lienzo.create_text(250, 455,
                           text="La pila esta vacia",
                           font=("Arial", 11))

def push():
    elemento = entrada.get()

    if elemento != "":
        if len(pila) < 7:
            pila.append(elemento)
            entrada.delete(0, tk.END)
            dibujar_pila()
        else:
            messagebox.showwarning("Aviso", "La pila esta llena")
    else:
        messagebox.showwarning("Aviso", "Escribe un elemento")

def pop():
    if len(pila) > 0:
        elemento = pila.pop()
        dibujar_pila()
        messagebox.showinfo("Pop", "Elemento eliminado: " + elemento)
    else:
        messagebox.showwarning("Aviso", "La pila esta vacia")

lienzo = tk.Canvas(ventana, width=500, height=480,
                   bg="white")
lienzo.pack()

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

boton_push = tk.Button(ventana, text="Agregar (PUSH)",
                       command=push)
boton_push.pack(pady=3)

boton_pop = tk.Button(ventana, text="Eliminar (POP)",
                      command=pop)
boton_pop.pack(pady=3)

dibujar_pila()

ventana.mainloop()
