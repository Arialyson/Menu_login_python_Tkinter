from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Login')
app.geometry('200x100')
app.configure(bg='#425DEF')

#Credenciais
credenciais = ['Arialyson','2023']

#função
def obter():
    nome = en_1.get()
    senha = en_2.get()
    print('O usuário digitado foi, {} e a Senha digitada foi {}'.format(nome, senha))

    if nome == 'Arialyson' and senha == '2023':
        messagebox.showinfo('Login','Seja Bem Vindo!')
        #apagar o que tiver no frame baixo cima
        for widget in en_1.winfo_children():
            widget.destroy()
        for widget in en_2.winfo_children():
            widget.destroy()
        
        
    
    else:
        messagebox.showerror('ERROR', 'Senha inválida, por favor, tente novamente!')

#apos verificar



# Label e Entry do usuário
lb_1 = Label(app, text='Nome:',bg='#425DEF',fg='#fff')
lb_1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
en_1 = Entry(app)
en_1.grid(row=0, column=1, sticky=E, padx=5, pady=5)

# Label e Entry da senha
lb_2 = Label(app, text='Senha:',bg='#425DEF',fg='#fff')
lb_2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
en_2 = Entry(app, show='*')
en_2.grid(row=1, column=1, sticky=E, padx=5, pady=5)

# Botão login
btn = Button(app, text='Login',command=obter,bg='#1F2C70', fg='#fff')
btn.grid(row=2, column=1, sticky=E, padx=5, pady=5)


app.mainloop()