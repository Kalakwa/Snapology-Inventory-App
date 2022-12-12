from tkinter import *

root = Tk()
root.title("Snapology Inventory List")
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("800x600")

mainfr = Frame(root, bg='#ff2a00')
mainfr.grid(sticky='news')

secfr = Frame(root, bg='#ff2a00')
secfr.grid(sticky='news')

mainca = Frame(mainfr, bg='#2fc25b')
mainca.grid(stick='news')

secca = Frame(secfr, bg='#74db93')
secca.grid(stick='news')

cat = ['Party\'s:', 'Gift Bags:', 'Slime Ingredients:', 'Cleaning Supplies:', 'Upstairs', 'Random:']

intipt = ""

# categories
Label(mainca, text="Parties:", fg='#309624', background='#ff2a00').grid(row=0, column=0)

Label(mainca, text="Gift Bags:", fg='#309624', background='#ff2a00').grid(row=10, column=0)

Label(mainca, text="Slime Ingredients:", fg='#309624', background='#ff2a00').grid(row=0, column=4)

Label(mainca, text="Cleaning Supplies:", fg='#309624', background='#ff2a00').grid(row=7, column=4)

Label(mainca, text="Random:", fg='#309624', background='#ff2a00').grid(row=0, column=8)

# Parties
Ent_1 = Entry(
    mainca,
    width=5,
    borderwidth=5,
)
Ent_1.insert(0, "0")
Ent_1.configure(state=DISABLED)
Ent_2 = Entry(mainca, width=5, borderwidth=5)
Ent_2.insert(0, "0")
Ent_3 = Entry(mainca, width=5, borderwidth=5)
Ent_3.insert(0, "0")
Ent_4 = Entry(mainca, width=5, borderwidth=5)
Ent_4.insert(0, "0")
Ent_4s = Entry(mainca, width=5, borderwidth=5)
Ent_4s.insert(0, "0")
Ent_4m = Entry(mainca, width=5, borderwidth=5)
Ent_4m.insert(0, "0")
Ent_4l = Entry(mainca, width=5, borderwidth=5)
Ent_4l.insert(0, "0")
Ent_5 = Entry(mainca, width=5, borderwidth=5)
Ent_5.insert(0, "0")
Ent_6 = Entry(mainca, width=5, borderwidth=5)
Ent_6.insert(0, "0")

Ent_1.grid(row=1, column=2)
Ent_2.grid(row=2, column=2)
Ent_3.grid(row=3, column=2)
Ent_4.grid(row=4, column=2)
Ent_4s.grid(row=5, column=2)
Ent_4m.grid(row=6, column=2)
Ent_4l.grid(row=7, column=2)
Ent_5.grid(row=8, column=2)
Ent_6.grid(row=9, column=2)

Label(mainca, text="Plates:", fg='#309624',
      background='#ff2a00').grid(row=1, column=1)
Label(mainca, text="Plasticware:", fg='#309624',
      background='#ff2a00').grid(row=2, column=1)
Label(mainca, text="Napkins:", fg='#309624',
      background='#ff2a00').grid(row=3, column=1)
Label(mainca, text="B-Day Shirts Total:", fg='#309624',
      background='#ff2a00').grid(row=4, column=1)
Label(mainca, text="B-Day Shirts (S):", fg='#309624',
      background='#ff2a00').grid(row=5, column=1)
Label(mainca, text="B-Day Shirts (M):", fg='#309624',
      background='#ff2a00').grid(row=6, column=1)
Label(mainca, text="B-Day Shirts (L):", fg='#309624',
      background='#ff2a00').grid(row=7, column=1)
Label(mainca, text="Tableclothes:", fg='#309624',
      background='#ff2a00').grid(row=8, column=1)
Label(mainca, text="Nametags:", fg='#309624',
      background='#ff2a00').grid(row=9, column=1)

# Gift Bags
Ent_7 = Entry(mainca, width=5, borderwidth=5)
Ent_7.insert(0, "0")
Ent_8 = Entry(mainca, width=5, borderwidth=5)
Ent_8.insert(0, "0")
Ent_9 = Entry(mainca, width=5, borderwidth=5)
Ent_9.insert(0, "0")
Ent_10 = Entry(mainca, width=5, borderwidth=5)
Ent_10.insert(0, "0")
Ent_11 = Entry(mainca, width=5, borderwidth=5)
Ent_11.insert(0, "0")
Ent_12 = Entry(mainca, width=5, borderwidth=5)
Ent_12.insert(0, "0")
Ent_13 = Entry(mainca, width=5, borderwidth=5)
Ent_13.insert(0, "0")

Ent_7.grid(row=11, column=2)
Ent_8.grid(row=12, column=2)
Ent_9.grid(row=13, column=2)
Ent_10.grid(row=14, column=2)
Ent_11.grid(row=15, column=2)
Ent_12.grid(row=16, column=2)
Ent_13.grid(row=17, column=2)

Label(mainca, text="Pencils:", fg='#309624',
      background='#ff2a00').grid(row=11, column=1)
Label(mainca, text="Bags:", fg='#309624', background='#ff2a00').grid(row=12,
                                                                     column=1)
Label(mainca, text="Kits:", fg='#309624', background='#ff2a00').grid(row=13,
                                                                     column=1)
Label(mainca, text="Bracelets:", fg='#309624',
      background='#ff2a00').grid(row=14, column=1)
Label(mainca, text="Stickers:", fg='#309624',
      background='#ff2a00').grid(row=15, column=1)
Label(mainca, text="Tattoos:", fg='#309624',
      background='#ff2a00').grid(row=16, column=1)
Label(mainca, text="Camp Flyers:", fg='#309624',
      background='#ff2a00').grid(row=17, column=1)

# Slime
Ent_14 = Entry(mainca, width=5, borderwidth=5)
Ent_14.insert(0, "0")
Ent_15 = Entry(mainca, width=5, borderwidth=5)
Ent_15.insert(0, "0")
Ent_16 = Entry(mainca, width=5, borderwidth=5)
Ent_16.insert(0, "0")
Ent_17 = Entry(mainca, width=5, borderwidth=5)
Ent_17.insert(0, "0")
Ent_a = Entry(mainca, width=5, borderwidth=5)
Ent_a.insert(0, "0")

Ent_14.grid(row=1, column=6)
Ent_15.grid(row=2, column=6)
Ent_16.grid(row=3, column=6)
Ent_17.grid(row=4, column=6)
Ent_a.grid(row=5, column=6)

Label(mainca, text="Bowls:", fg='#309624', background='#ff2a00').grid(row=1,
                                                                      column=5)
Label(mainca, text="Shaving cream:", fg='#309624',
      background='#ff2a00').grid(row=2, column=5)
Label(mainca, text="Glue:", fg='#309624', background='#ff2a00').grid(row=3,
                                                                     column=5)
Label(mainca, text="Baking Soda:", fg='#309624',
      background='#ff2a00').grid(row=4, column=5)
Label(mainca, text="Contact Solution:", fg='#309624',
      background='#ff2a00').grid(row=5, column=5)

# Cleaning
Ent_18 = Entry(mainca, width=5, borderwidth=5)
Ent_18.insert(0, "0")
Ent_19 = Entry(mainca, width=5, borderwidth=5)
Ent_19.insert(0, "0")
Ent_20 = Entry(mainca, width=5, borderwidth=5)
Ent_20.insert(0, "0")
Ent_21 = Entry(mainca, width=5, borderwidth=5)
Ent_21.insert(0, "0")
Ent_22 = Entry(mainca, width=5, borderwidth=5)
Ent_22.insert(0, "0")
Ent_23 = Entry(mainca, width=5, borderwidth=5)
Ent_23.insert(0, "0")
Ent_24 = Entry(mainca, width=5, borderwidth=5)
Ent_24.insert(0, "0")
Ent_25 = Entry(mainca, width=5, borderwidth=5)
Ent_25.insert(0, "0")

Ent_18.grid(row=8, column=6)
Ent_19.grid(row=9, column=6)
Ent_20.grid(row=10, column=6)
Ent_21.grid(row=11, column=6)
Ent_22.grid(row=12, column=6)
Ent_23.grid(row=13, column=6)
Ent_24.grid(row=14, column=6)
Ent_25.grid(row=15, column=6)

Label(mainca, text="Surface Cleaner:", fg='#309624',
      background='#ff2a00').grid(row=8, column=1)
Label(mainca, text="Paper Towels:", fg='#309624',
      background='#ff2a00').grid(row=9, column=5)
Label(mainca, text="Clorox Wipes:", fg='#309624',
      background='#ff2a00').grid(row=10, column=5)
Label(mainca, text="L Black Bags:", fg='#309624',
      background='#ff2a00').grid(row=11, column=5)
Label(mainca, text="Sm White Bags:", fg='#309624',
      background='#ff2a00').grid(row=12, column=5)
Label(mainca, text="Windex:", fg='#309624',
      background='#ff2a00').grid(row=13, column=5)
Label(mainca, text="Dish Soap:", fg='#309624',
      background='#ff2a00').grid(row=14, column=5)
Label(mainca, text="Toilet Cleaner:", fg='#309624',
      background='#ff2a00').grid(row=15, column=5)

# Random
Ent_26 = Entry(mainca, width=5, borderwidth=5)
Ent_26.insert(0, "0")
Ent_27 = Entry(mainca, width=5, borderwidth=5)
Ent_27.insert(0, "0")
Ent_28 = Entry(mainca, width=5, borderwidth=5)
Ent_28.insert(0, "0")
Ent_29 = Entry(mainca, width=5, borderwidth=5)
Ent_29.insert(0, "0")
Ent_30 = Entry(mainca, width=5, borderwidth=5)
Ent_30.insert(0, "0")
Ent_31 = Entry(mainca, width=5, borderwidth=5)
Ent_31.insert(0, "0")
Ent_32 = Entry(mainca, width=5, borderwidth=5)
Ent_32.insert(0, "0")
Ent_33 = Entry(mainca, width=5, borderwidth=5)
Ent_33.insert(0, "0")
Ent_34 = Entry(mainca, width=5, borderwidth=5)
Ent_34.insert(0, "0")

Ent_26.grid(row=1, column=10)
Ent_27.grid(row=2, column=10)
Ent_28.grid(row=3, column=10)
Ent_29.grid(row=4, column=10)
Ent_30.grid(row=5, column=10)
Ent_31.grid(row=6, column=10)
Ent_32.grid(row=7, column=10)
Ent_33.grid(row=8, column=10)
Ent_34.grid(row=9, column=10)

Label(mainca, text="Snacks:", fg='#309624',
      background='#ff2a00').grid(row=1, column=9)
Label(mainca, text="Kleenex:", fg='#309624',
      background='#ff2a00').grid(row=2, column=9)
Label(mainca, text="Ziploc Total:", fg='#309624',
      background='#ff2a00').grid(row=3, column=9)
Label(mainca, text="Ziploc Sandwich:", fg='#309624',
      background='#ff2a00').grid(row=4, column=9)
Label(mainca, text="Ziploc Quart:", fg='#309624',
      background='#ff2a00').grid(row=5, column=9)
Label(mainca, text="Ziploc Gallon:", fg='#309624',
      background='#ff2a00').grid(row=6, column=9)
Label(mainca, text="Water Cups:", fg='#309624',
      background='#ff2a00').grid(row=7, column=9)
Label(mainca, text="WEDO Extras:", fg='#309624',
      background='#ff2a00').grid(row=8, column=9)
Label(mainca, text="USB'S:", fg='#309624', background='#ff2a00').grid(row=9,
                                                                      column=9)

# Buttons
button = Button(secca, padx=6, pady=2, activebackground='#4b9c63')


def Updatebox(Ent):
    try:
        global newnum
        newnum = Ent.get()
        Ent.delete(0, END)

    except Ent != int():
        return


a = Updatebox(Ent_1)
for c in cat:
    Label(text='')

# Frame Update
root.mainloop()   