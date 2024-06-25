import tkinter as tk
from tkinter import ttk
import os  
from tkinter import filedialog
root = tk.Tk()
def save_text():
    pass
root.title("sans titre - Bloc-notes")
root.geometry("800x500")
# Menu principal
menu_bar = tk.Menu(root)

global_file = None  

def set_global_value(new_value=""):
    global global_file  
    global_file = new_value  

set_global_value()
global_text = None
def set_global_text(new_value="") :
    global global_text
    global_text = new_value
    
set_global_text()

def cahnge_name():
    if global_file == "":
        root.title("sans titre - Bloc-notes")
    else:
        root.title(os.path.basename(global_file))


def save_content(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)
        return file_path
    
def open_file_dialog():
    filepath = filedialog.askopenfilename()
    if filepath:
        # Do something with the selected file path
        return filepath

def file_menu_nouveau():
    if global_file == "" :
        if text.get("1.0","end-1c") == "" :
            root.title("sans titre - Bloc-notes")
        else :
            window1=tk.Toplevel(root)
            window1.geometry("400x100")
            window1_label = tk.Label(window1,text="voulez vous enregistrer les modifications?")
            window1_label.place(x=90,y=0)
            
            def func_oui() :
                window1.destroy()
                content = text.get("1.0", "end-1c")
                save_content(content)
                set_global_value()
                text.delete(1.0,tk.END)
                text.focus_set()
                cahnge_name()  
            def func_non () :
                text.delete(1.0,tk.END)
                set_global_value()
                cahnge_name()
                window1.destroy()
                text.focus_set()
                
            button1 = tk.Button(window1, text="oui",width=10, command=func_oui)
            button2 = tk.Button(window1, text="non",width=10, command=func_non)
            button3 = tk.Button(window1, text="annuler",width=10, command=window1.destroy)
            button1.place(x=50,y=50)
            button2.place(x=150,y=50)
            button3.place(x=250,y=50)
    else :
        file=open(global_file,"r")
        if text.get("1.0","end-1c") == file.read() :  
            text.delete(1.0,tk.END)
            set_global_value()
            cahnge_name()
            file.close()
        else :
            window1=tk.Toplevel(root)
            window1.geometry("400x100")
            window1_label = tk.Label(window1,text="voulez vous enregistrer les modifications?")
            window1_label.place(x=90,y=0)
            def func_oui() :
                window1.destroy()
                content = text.get("1.0", "end-1c")
                file2=open(global_file,"w+")
                file2.write(content)
                file2.close()
                set_global_value()
                cahnge_name()
                text.delete(1.0,tk.END)
                text.focus_set()
                file.close()
            def func_non () :
                text.delete(1.0,tk.END)
                set_global_value()
                cahnge_name()
                window1.destroy()
                text.focus_set()
                file.close()
            button1 = tk.Button(window1, text="oui",width=10, command=func_oui)
            button2 = tk.Button(window1, text="non",width=10, command=func_non)
            button3 = tk.Button(window1, text="annuler",width=10, command=window1.destroy)
            #just save the content in the current opened file which is file"
            button1.place(x=50,y=50)
            button2.place(x=150,y=50)
            button3.place(x=250,y=50)      
def file_menu_ouvrir():
    if global_file == "" :
        if text.get("1.0","end-1c") == "" :
            file= open(open_file_dialog(),'r+')
            set_global_value(file.name)
            cahnge_name()
            content=file.read()
            file.close()
            text.insert(tk.END, f"{content}")
            text.focus_set()
        else : 
            window1=tk.Toplevel(root)
            window1.geometry("400x100")
            window1_label = tk.Label(window1,text="voulez vous enregistrer les modifications?")
            window1_label.place(x=90,y=0)
            
            def func_oui() :
                window1.destroy()
                content = text.get("1.0", "end-1c")
                save_content(content)
                text.delete(1.0,tk.END)
                text.focus_set()
                file= open(open_file_dialog(),'r+')
                set_global_value(file.name)
                cahnge_name()
                content=file.read()
                file.close()
                text.insert(tk.END, f"{content}")
                text.focus_set()
                
            def func_non () :
                text.delete(1.0,tk.END)
                window1.destroy()
                file= open(open_file_dialog(),'r+')
                set_global_value(file.name)
                cahnge_name()
                content=file.read()
                file.close()
                text.insert(tk.END, f"{content}")
                text.focus_set()
                
            button1 = tk.Button(window1, text="oui",width=10, command=func_oui)
            button2 = tk.Button(window1, text="non",width=10, command=func_non)
            button3 = tk.Button(window1, text="annuler",width=10, command=window1.destroy)
            button1.place(x=50,y=50)
            button2.place(x=150,y=50)
            button3.place(x=250,y=50)
    else : 
        file=open(global_file,'r')
        if text.get("1.0","end-1c") == file.read() : 
            file1= open(open_file_dialog(),'r+')
            text.delete(1.0,tk.END)
            set_global_value(file1.name)
            cahnge_name()
            content=file1.read()
            file.close()
            file1.close()
            text.insert(tk.END, f"{content}")
            text.focus_set()
        else :
            window1=tk.Toplevel(root)
            window1.geometry("400x100")
            window1_label = tk.Label(window1,text="voulez vous enregistrer les modifications?")
            window1_label.place(x=90,y=0)
            
            def func_oui() :
                window1.destroy()
                file2 = open(global_file,'w+')
                file2.write(text.get("1.0", "end-1c"))
                file2.close()
                text.delete(1.0,tk.END)
                file1= open(open_file_dialog(),'r+')
                set_global_value(file1.name)
                cahnge_name()
                content=file1.read()
                file.close()
                file1.close()
                text.insert(tk.END, f"{content}")
                text.focus_set()
                ########################################################################
            def func_non () :
                text.delete(1.0,tk.END)
                window1.destroy()
                file1= open(open_file_dialog(),'r+')
                set_global_value(file1.name)
                cahnge_name()
                content=file1.read()
                file.close()
                file1.close()
                text.insert(tk.END, f"{content}")
                text.focus_set()
                
            button1 = tk.Button(window1, text="oui",width=10, command=func_oui)
            button2 = tk.Button(window1, text="non",width=10, command=func_non)
            button3 = tk.Button(window1, text="annuler",width=10, command=window1.destroy)
            button1.place(x=50,y=50)
            button2.place(x=150,y=50)
            button3.place(x=250,y=50)

def file_menu_enregistrer():
    if global_file == "" :
        content = text.get("1.0", "end-1c")
        file = save_content(content)
        set_global_value(file.name)
        text.focus_set()
        cahnge_name()  
    else :
        file = open(global_file,'w+')
        file.write(text.get("1.0", "end-1c"))
        file.close()
        text.focus_set()

def file_menu_enregistrer_sous():
    content = text.get("1.0", "end-1c")
    file = save_content(content)
    file1 = open(file,'w+')
    file1.write(content)
    set_global_value(file1.name)
    cahnge_name() 
    file1.close()
    text.focus_set() 

def edit_menu_copier():
    selected_text = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    set_global_text(selected_text)

def edit_menu_couper():
    selected_text = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    set_global_text(selected_text)
    text.delete(tk.SEL_FIRST,tk.SEL_LAST)
    
def edit_menu_coller():
    text.insert(tk.INSERT,global_text)
def help_menu_command():
    window=tk.Tk()
    window.title("À propos")
    label1=tk.Label(master=window,text=f"application de bloc-note de but de simuler bloc note de windows10 \n \n\ndeveloppée par Houssam IBNCHAKROUNE")
    label1.place(x=90,y=10)
    button= tk.Button(window,text="ok",command=window.destroy,width=10,bg="blue")
    button.place(x=350,y=80)
    window.geometry("500x250")
    window.mainloop()

# Menu "Fichier"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=file_menu_nouveau)
file_menu.add_command(label="Ouvrir", command=file_menu_ouvrir)
file_menu.add_command(label="Enregistrer", command=file_menu_enregistrer)
file_menu.add_command(label="Enregistrer sous", command=file_menu_enregistrer_sous)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.destroy)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Menu "Édition"
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Couper", command=edit_menu_couper)
edit_menu.add_command(label="Copier", command=edit_menu_copier)
edit_menu.add_command(label="Coller", command=edit_menu_coller)
menu_bar.add_cascade(label="Édition", menu=edit_menu)

# Menu "Aide"
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="À propos", command=help_menu_command)
menu_bar.add_cascade(label="Aide", menu=help_menu)

root.config(menu=menu_bar)
text = tk.Text(root, height=39, width=170)
text.place(x=0,y=0)
text.focus_set()

root.mainloop()
############point à devloppé
#1)le menu edition copie justement dans l'application et non pas dans le press papier
#2)quitter ne verifie pas le modifications faites dans le fichier ouvert 
#3) il faut ajouter les shortcuts


