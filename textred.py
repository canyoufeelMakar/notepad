from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def change_theme(theme):
    text_fild['bg']=view_colors[theme]['text_bg']
    text_fild['fg']=view_colors[theme]['text_fg']
    text_fild['insertbackground']=view_colors[theme]['cursor']
    text_fild['selectbackground']=view_colors[theme]['select_background']

def change_fonts(fontss):
          text_fild['font']=fonts[fontss]['font']


def notepad_exit():
    answer = messagebox.askokcancel('You sure you want to exit?')
    if answer:
        root.destroy()


def open_file():
    file_path= filedialog.askopenfilename(
        title='choose a file', filetypes=(('Text docs(*.txt)',
                                '*.txt'), ('All files', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path,
                            encoding='utf-8').read())



def save_file():
    file_path= filedialog.asksaveasfilename(
        filetypes=(('Text docs(*.txt)','*.txt'), ('All files', '*.*')))
    f = open(file_path,'w',encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()

root=Tk()
root.title('textred')
root.geometry('600x700')




main_menu=Menu(root)


# file
file_menu=Menu(main_menu, tearoff=0)

file_menu.add_command(label='Open',
                      command=open_file)

file_menu.add_command(label='Save',
                      command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Close', 
                      command=notepad_exit)

root.config(menu=file_menu)


#вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='dark',
                          command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='light',
                          command=lambda: change_theme('light'))
view_menu.add_cascade(label='Theme', menu=view_menu_sub)
                     
font_menu_sub.add_command(label='Arial', 
                          command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS',
                          command=lambda: change_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman',
                          command=lambda: change_fonts('TNR'))
view_menu.add_cascade(label='font', menu=font_menu_sub)


#Добавление списков меню
main_menu.add_cascade(label='file', menu=file_menu)
main_menu.add_cascade(label='view', menu=view_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand = 1)


#библиотека для темsdfv
view_colors = {
    'dark' : {
        'text_bg': 'black', 'text_fg': 'white', 'cursor': 'white',
        'select_background': 'red'
        },
    'light': {
        'text_bg': 'pink', 'text_fg': 'black', 'cursor': 'black',
        'select_background': 'red'
        }
    }

fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
        },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
        },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
        }
    }


#text

text_fild = Text(f_text,
                 bg='pink', 
                 fg='black',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='black',
                 selectbackground='red',
                 spacing3=10,
                 width=30,
                 font='Arial 14 bold' 
            )


scroll=Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=RIGHT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)
text_fild.pack(expand=1, fill=BOTH, side=LEFT )

root.mainloop()