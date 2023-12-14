# -*- coding: utf-8 -*-
import sys, os

from tkinter import Tk, filedialog, Button, Label, NORMAL, BOTH, LEFT, END
from tkinter.scrolledtext import ScrolledText

def openFile():
    my_filetypes = [('SRT files', '.srt'), ('TXT files', '.txt')]
    filepath = filedialog.askopenfilename(parent = window, initialdir = os.getcwd(), title="Alegeti fisierul SRT:", filetypes=my_filetypes)
    
    try:
        fo = open(filepath, "r", encoding="utf-8")
        line = fo.readlines()
        repla = ""
        for x in line:
            newx = x.replace('\u015f', 'º') \
                .replace('\u0219', 'º') \
                .replace('\u015e', 'ª') \
                .replace('\u0218', 'ª') \
                .replace('\u0102', 'Ã') \
                .replace('\u0103', 'ã') \
                .replace('\u0163', 'þ') \
                .replace('\u021b', 'þ') \
                .replace('\u0162', 'Þ') \
                .replace('\u021a', 'Þ')
            repla = repla + newx

        fo.close()

        fow = open(filepath, "w", encoding="utf-8")
        fow.write(repla)
        fow.close()

        st.insert(END, "Fi\u015fierul "+ os.path.basename(filepath) +" a fost modificat \u015fi poate fi folosit.\n", 'colorGreen' )
    except:
        #print("Nu a fost selectat nici un fisier")
        st.insert(END, "Nu a fost selectat nici un fi\u015fier SAU Fiserul este read-only.\n", 'colorRed' )


window = Tk()
window.title("Modificare diacritice")
window.resizable(False, False)
window.geometry('600x200')
button = Button(text="Start",command=openFile)
button.pack(ipadx=11, ipady=7)

st = ScrolledText(window, state = NORMAL)
st.pack(fill=BOTH, side=LEFT, expand=True)
st.tag_config('colorGreen', foreground='green')
st.tag_config('colorRed', foreground='red')
st.tag_config('colorMagenta', foreground='magenta')

st.insert(END, "Apasa butonul 'Start' \u015fi alege fi\u015fierul care trebuie convertit.\nSunt acceptate fi\u015fierele SRT \u015fi TXT.\n", 'colorMagenta' )
window.mainloop()