from tkinter import *
from tkinter.scrolledtext import ScrolledText
import random
from PIL import ImageTk, Image
import os
# MAIN WINDOW
gg = Tk()
gg.title("Text Based Adverture game")
f = Canvas(gg, width=1270, height=800)
f.pack(fill="both", expand=True)
# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path to the image within the 'assets' folder
img = ImageTk.PhotoImage(Image.open(
    current_directory+"/assets/images/castle1.jpg"))
f.create_image(0, 0, anchor=NW, image=img)
d = Button(gg, text="start", fg="orange", bg="purple", font="bold")
img1 = ImageTk.PhotoImage(Image.open(
    current_directory+"/assets/images/ransacked1.jpg"))
img3 = ImageTk.PhotoImage(Image.open(
    current_directory+"/assets/images/bar3.jpg"))
img5 = ImageTk.PhotoImage(Image.open(
    current_directory+"/assets/images/cart1.jpg"))
img7 = ImageTk.PhotoImage(Image.open(
    current_directory+"/assets/images/garden3.jpg"))
img4 = ImageTk.PhotoImage(Image.open(
    current_directory+"/assets/images/house4.jpg"))
img8 = ImageTk.PhotoImage(Image.open(
    current_directory+"/assets/images/app1.jpg"))
I = Label(gg, image=img1)
I3 = Label(gg, image=img3)
I4 = Label(gg, image=img4)
I5 = Label(gg, image=img5)
I7 = Label(gg, image=img7)
I8 = Label(gg, image=img8)


def start():
    d.destroy()
    st = ScrolledText(gg, width=150, height=20)
    c_window = f.create_window(20, 10, anchor=NW, window=st)
    st.insert(END, "WELCOME TO TEXT BASED ADVENTURE GAME")
    st.insert(END,
              "\nYou are lancelot and the town people call you the engineering god because of your ingenious inventions.\nYou made your fortune by your inventions")
    st.insert(END,
              "\nOne day you wake up and see that all your fortune has been stolen from your safe , and there is no sign of your wife.\n you search the whole house for clues but wont find any")
    c1_window = f.create_window(20, 350, anchor=NW, window=I)
    st.insert(END, "\nWhat do you want to do?")
    st.yview(END)

    def lastpart():
        def check1():
            st.insert(END, "there is a letter and a pouch of gold")
            st.insert(END,
                      "\t\t\t  LETTER\nahhh lancelot!! i am the one who stole ur fortune .\nYou and your arrogant behaviour was making me sick so it serves u right")
            c12 = Checkbutton(gg, text="look around for more clues")
            c13 = Checkbutton(gg, text="go back")
            c12_window = f.create_window(850, 450, anchor=NW, window=c12)
            c13_window = f.create_window(850, 500, anchor=NW, window=c13)
            st.yview(END)

            def last():
                c12.destroy()
                c13.destroy()
                c1_window = f.create_window(20, 350, anchor=NW, window=I8)
                st.insert(END,
                          "\n hmm let me look around \n wait is that gold??.... \n there is a trail of gold here!!....  ")
                st.insert(END,
                          " \n FOLLOWING THE GOLD COIN TRAIL\nhmm the apparatus, its a living thing which uses pure metal as blood ./n It looks down for some reason and it has been following me from the start of the trail i wonder why?\n well, I have to find the one who took my fortune \n   CONTINUES TO FOLLOW THE TRAIL\nyou:AHHH!! i found my fortune!!\nyou: whaat.. are you doing here emma??\nEmma:hi lancelot i was the one who took wour fortune \n you: that explains why the safe was not damaged \n Emma : you were so  polite and kind when you were inventing but now you have become arrogant and rude  because of your fortune.You are not the lancelot that i knew\nyou : so we are on our ways now ig? \nEmma: i will be waiting\nyou: hmm i offered my fortune to alot of people who might have needed it but they refused it. Now what will i do with this money? \nThe apparatus maintains the land there is no doubt that there is spikes every where \nmaybe i will give it the gold and save his life")
                st.yview(END)
                def s7():
                    st.insert(END,
                              "\n \n would u like to save the apparatus? ")
                    ic = Checkbutton(gg, text="y")
                    ic1 = Checkbutton(gg, text="n")
                    ic_window = f.create_window(850, 450, window=ic, anchor=NW)
                    ic1_window = f.create_window(
                        850, 500, window=ic1, anchor=NW)
                    st.yview(END)
                    def b():
                        st.insert(END, "\nthe apparatus (-_-)->(>_<)->(*,*) ")
                        st.insert(END,"\n*the apparatus is happy*")
                        st.insert(END,"\n the apparatus thanks lancelot for saving his life and making it happy!!\n")
                        st.insert(END,"""\n ON IN HIS WAY BACK FROM THE TRAIL\n 
                                  Emma: I was waiting for you here
                                  you: so you didnt go your way
                                  Emma: So you decided to help apparatus
                                  you: yes
                                  Emma: It's great to see you changed back to the lancelot i knew
                                  you: yes.....i think it would be for the better
                                  Emma: are you sure you wouldnt change for a long time?""")
                        cx = Checkbutton(gg, text="y")
                        cy = Checkbutton(gg, text="n")
                        cx_window = f.create_window(850, 450, anchor=NW, window=cx)
                        cy_window = f.create_window(850, 500, anchor=NW, window=cy)
                        
                        f.create_text(
                            1000, 480, text="please give feedback of the game", fill="yellow")
                        T = Entry(gg, width=40)
                        T_window = f.create_window(
                            900, 500, window=T, anchor=NW)
                        h = Button(gg, text="enter")
                        h_window = f.create_window(
                            900, 550, anchor=NW, window=h)
                        st.yview(END)

                        def read():
                            l = []
                            with open('feedback.txt', "r")as myfile:
                                l.append(myfile.read())
                            g = T.get()
                            l.append(g)
                            with open('feedback.txt', "w") as myfile:
                                for i in l:
                                   myfile.write("%s\n" % i)
                        h.configure(command=read)
                        ic.destroy()
                        ic1.destroy()

                    ic.configure(command=b)
                    ic1.configure(command=b)

                s7()

            def go():
                def TrailAction():
                    c10 = Checkbutton(gg, text="1).follow the  trail")
                    c11 = Checkbutton(
                        gg, text="2).look around to find more clues")
                    c10_window = f.create_window(
                        850, 450, window=c10, anchor=NW)
                    c11_window = f.create_window(
                        850, 500, window=c11, anchor=NW)
                    st.yview(END)

                    def seeCart():
                        c1_window = f.create_window(
                            20, 350, anchor=NW, window=I5)
                        c10.destroy()
                        c11.destroy()
                        st.insert(END, "\n the cart is there ")
                        c14 = Checkbutton(gg, text="check inside the cart")
                        c14_window = f.create_window(
                            850, 450, window=c14, anchor=NW)
                        c15 = Checkbutton(gg, text="check outside")
                        c15_window = f.create_window(
                            850, 500, window=c15, anchor=NW)
                        c16 = Checkbutton(gg, text="go back")
                        c16_window = f.create_window(
                            850, 550, window=c16, anchor=NW)
                        st.yview(END)

                        def SeeCart2():
                            c14.destroy()
                            c15.destroy()
                            c16.destroy()
                            st.insert(END, "\n chest is open")
                            seeCart()
                            st.yview(END)

                        def apparatus():
                            c14.destroy()
                            c15.destroy()
                            c16.destroy()
                            st.insert(
                                END, "hmm there is a paper,lets see what is written in that ")
                            st.insert(END,
                                      "THE APPARATUS \nis a living thing which uses pure metal as blood.\nIt keeps the land in order,other wise the land will be filled with thorns and traps ")
                            seeCart()
                            st.yview(END)

                        def bh():
                            c14.destroy()
                            c15.destroy()
                            c16.destroy()
                            TrailAction()
                            st.yview(END)

                        c14.configure(command=SeeCart2)
                        c15.configure(command=apparatus)
                        c16.configure(command=bh)

                    def pree():
                        c10.destroy()
                        c11.destroy()
                        last()
                        st.yview(END)

                    c10.configure(command=seeCart)
                    c11.configure(command=pree)

                TrailAction()

            def last2():
                c12.destroy()
                c13.destroy()
                go()
                st.yview(END)

            c12.configure(command=last)
            c13.configure(command=last2)

        check1()

    def beginning():
        c1 = Checkbutton(gg, text=" 1)go to the post office")
        c_window = f.create_window(850, 450, window=c1, anchor=NW)
        c2 = Checkbutton(gg, text="2)go to the bar")
        c_window = f.create_window(850, 500, window=c2, anchor=NW)
        st.yview(END)

        def postOffice():
            st.insert(END, "\nThere are no letters for you")
            c1.destroy()
            c2.destroy()
            beginning()
            st.yview(END)

        def bar():
            c1_window = f.create_window(20, 350, anchor=NW, window=I3)
            st.insert(END, """ \n IN THE BAR  :
                                baxter: hey mate how are you?, I heard that you were robbed .
                                you: ahhh yea those thugs took all my fortune without
                                leaving a single clue (sigh).
                                baxter: hmm what if some one you close to you did it cause
                                no one knows how your inventions work.
                                you: hmm you have a good point.""")
            st.yview(END)
            c1.destroy()
            c2.destroy()

            def leave():
                st.insert(END, "\nWhat do you want to do?")
                c3 = Checkbutton(
                    gg, text="1)hang around looking for more info")
                c_window = f.create_window(850, 450, window=c3, anchor=NW)
                c4 = Checkbutton(gg, text="2)leave the bar")
                c_window = f.create_window(850, 500, window=c4, anchor=NW)
                st.yview(END)

                def noInfo():
                    st.insert(END, "\n no useful information")
                    c3.destroy()
                    c4.destroy()
                    leave()
                    st.yview(END)

                def leaveBar():
                    c3.destroy()
                    c4.destroy()

                    def inner():
                        st.insert(
                            END, " \n okay you are outside the bar.\n What do you want to do \n")
                        c5 = Checkbutton(f, text="1)to the village headman\n")
                        c6 = Checkbutton(f, text="2)home")
                        c_window = f.create_window(
                            850, 450, window=c5, anchor=NW)
                        c_window = f.create_window(
                            850, 500, window=c6, anchor=NW)
                        st.yview(END)

                        def Headman():
                            c5.destroy()
                            c6.destroy()
                            st.insert(END,
                                      "\n you lodge a complaint about the robbery and the headman promises to do as much as he can.")
                            inner()
                            st.yview(END)

                        def home():
                            st.insert(END, "\nAT HOME")
                            st.yview(END)

                            def checkHome():
                                c5.destroy()
                                c6.destroy()

                                def inner1():
                                    st.insert(
                                        END, "\nWhat do you want to do?\n")
                                    c1_window = f.create_window(
                                        20, 350, anchor=NW, window=I4)
                                    c7 = Checkbutton(
                                        f, text=")check the bulding windows for damage")
                                    c8 = Checkbutton(
                                        f, text="2).check the safe for damages")
                                    c9 = Checkbutton(
                                        f, text="3).check the garden.")
                                    c7_window = f.create_window(
                                        850, 450, window=c7, anchor=NW)
                                    c8_window = f.create_window(
                                        850, 500, window=c8, anchor=NW)
                                    c9_window = f.create_window(
                                        850, 550, window=c9, anchor=NW)
                                    st.yview(END)

                                    def homeWindow():
                                        st.insert(
                                            END, "  \n hmm the bulding windows are not damaged ")
                                        c7.destroy()
                                        c8.destroy()
                                        c9.destroy()
                                        inner1()
                                        st.yview(END)

                                    def safe():
                                        st.insert(END,
                                                  "\nwait the safe is also not damaged \n hmmm now i have a feeling that someone who knows about my inventions stole my fortune")
                                        c7.destroy()
                                        c8.destroy()
                                        c9.destroy()
                                        inner1()
                                        st.yview(END)

                                    def cart():
                                        st.insert(END,
                                                  "\n hmm cart trails hmm I guess they used a cart to steal my fortune")
                                        c7.destroy()
                                        c8.destroy()
                                        c9.destroy()
                                        st.yview(END)

                                        def TrailAction():
                                            st.insert(
                                                END, "\n what you wanna do")
                                            c10 = Checkbutton(
                                                f, text="1).follow the  trail")
                                            c11 = Checkbutton(
                                                f, text="2).look around to find more clues")
                                            c1_window = f.create_window(
                                                20, 350, anchor=NW, window=I7)
                                            c10_window = f.create_window(
                                                850, 450, window=c10, anchor=NW)
                                            c11_window = f.create_window(
                                                850, 500, window=c11, anchor=NW)
                                            st.yview(END)

                                            def seeCart():
                                                c10.destroy()
                                                c11.destroy()
                                                st.insert(
                                                    END, "\nhmm a clearing and there is a cart ")
                                                c1_window = f.create_window(
                                                    2000, 350, anchor=NW, window=I7)
                                                st.yview(END)

                                                def checkCart():
                                                    c1_window = f.create_window(
                                                        20, 350, anchor=NW, window=I5)
                                                    st.insert(
                                                        END, "\nwant to check the cart?")
                                                    l1 = Checkbutton(
                                                        f, text="y")
                                                    l1_window = f.create_window(
                                                        850, 450, window=l1, anchor=NW)
                                                    l2 = Checkbutton(
                                                        f, text="n")
                                                    l2_window = f.create_window(
                                                        850, 500, window=l2, anchor=NW)
                                                    st.yview(END)

                                                    def chestOpenTrial():
                                                        l1.destroy()
                                                        l2.destroy()

                                                        def paper():
                                                            st.insert(END,
                                                                      "\nThis cart is not designed by me \n oh there is a chest and a paper here")
                                                            o1 = Checkbutton(
                                                                f, text="try to open the chest")
                                                            o1_window = f.create_window(
                                                                850, 450, window=o1, anchor=NW)
                                                            o2 = Checkbutton(
                                                                f, text="see the paper")
                                                            o2_window = f.create_window(
                                                                850, 500, window=o2, anchor=NW)
                                                            st.yview(END)

                                                            def puzzleSolve():
                                                                o1.destroy()
                                                                o2.destroy()
                                                                st.insert(END,
                                                                          "\n PAPER \nSolve the puzzle below to open the chest")
                                                                st.insert(
                                                                    END, "\ndo yo want to solve it?")
                                                                o3 = Checkbutton(
                                                                    f, text="yes")
                                                                o3_window = f.create_window(
                                                                    850, 450, window=o3, anchor=NW)
                                                                o4 = Checkbutton(
                                                                    f, text="no")
                                                                o4_window = f.create_window(
                                                                    850, 500, window=o4, anchor=NW)
                                                                st.yview(END)

                                                                def sudokuOpen():
                                                                    o3.destroy()
                                                                    o4.destroy()

                                                                    def sike():
                                                                        p = Tk()
                                                                        p.configure(
                                                                            background="purple")
                                                                        b = Button(
                                                                            p, text="enter")
                                                                        p.title(
                                                                            "solve this puzzle")
                                                                        nicex = []
                                                                        nicey = []
                                                                        nice = []
                                                                        y = 0
                                                                        l = [[2, 9, 7, 4, 3, 1, 8, 6, 5],
                                                                             [3, 1, 4, 5, 6,
                                                                                 8, 9, 2, 7],
                                                                             [6, 5, 8, 9, 7,
                                                                                 2, 1, 4, 3],
                                                                             [5, 8, 1, 7, 2,
                                                                                 6, 3, 9, 4],
                                                                             [7, 4, 3, 8, 9,
                                                                                 5, 2, 1, 6],
                                                                             [9, 6, 2, 3, 1,
                                                                                 4, 7, 5, 8],
                                                                             [8, 2, 9, 6, 5,
                                                                                 7, 4, 3, 1],
                                                                             [1, 7, 6, 2, 4,
                                                                                 3, 5, 8, 9],
                                                                             [4, 3, 5, 1, 8, 9, 6, 7, 2]]
                                                                        for i in l:

                                                                            for j in range(0, 9):
                                                                                x = random.randint(
                                                                                    1, 9)
                                                                                if i[j] != x:
                                                                                    i[j] = Button(p, text=i[j], width=4,
                                                                                                  bg="orange",
                                                                                                  fg="purple")
                                                                                    i[j].grid(row=0 + j, column=0 + y,
                                                                                              sticky=W,
                                                                                              pady=2, padx=2)
                                                                                else:
                                                                                    nice.append(
                                                                                        i[j])
                                                                                    u = Entry(
                                                                                        p, width=4)
                                                                                    u.grid(row=0 + j, column=0 + y,
                                                                                           sticky=W,
                                                                                           pady=2, padx=2)
                                                                                    nicex.append(
                                                                                        j)
                                                                                    nicey.append(
                                                                                        y)
                                                                            y += 1
                                                                        d = {}
                                                                        for i in range(0, len(nice)):
                                                                            j = []
                                                                            j.append(
                                                                                nicex[i] + 1)
                                                                            j.append(
                                                                                nicey[i] + 1)
                                                                            d[nice[i]] = j

                                                                        def enter():
                                                                            y = random.sample(
                                                                                nice, 4)
                                                                            g = Label(p,
                                                                                      text="the password is in this coordinates")
                                                                            g.grid(
                                                                                row=0, column=11)
                                                                            k = 0
                                                                            for g in y:
                                                                                y[k] = str(
                                                                                    y[k])
                                                                                g = Label(
                                                                                    p, text=f'{g}]{d[g]}')
                                                                                g.grid(
                                                                                    row=1 + k, column=11)
                                                                                k += 1
                                                                                e = Entry(p,
                                                                                          text="enter the password here",
                                                                                          width=20)
                                                                                e.grid(
                                                                                    row=6, column=11)
                                                                            co = Button(
                                                                                p, text="continue")
                                                                            co.grid(
                                                                                row=6, column=12)

                                                                            def check():
                                                                                g = e.get()
                                                                                x = "".join(
                                                                                    y)
                                                                                if g == x:
                                                                                    e.destroy()
                                                                                    co.destroy()
                                                                                    f = Label(
                                                                                        p, text="correct!!")
                                                                                    f.grid(
                                                                                        row=6, column=31)
                                                                                    con1 = Button(p,
                                                                                                  text="continue the game")
                                                                                    con1.grid(
                                                                                        row=7, column=11)

                                                                                    def des():
                                                                                        p.destroy()
                                                                                        lastpart()

                                                                                    con1.configure(
                                                                                        command=des)
                                                                                else:
                                                                                    x = Label(
                                                                                        p, text="try again")
                                                                                    enter()

                                                                            co.config(
                                                                                command=check)

                                                                        b.grid(
                                                                            row=75, column=40)
                                                                        b.config(
                                                                            command=enter)
                                                                        p.mainloop()

                                                                    sike()

                                                                def chestOpenTrial():
                                                                    o3.destroy()
                                                                    o4.destroy()
                                                                    paper()

                                                                o3.configure(
                                                                    command=sudokuOpen)
                                                                o4.configure(
                                                                    command=chestOpenTrial)

                                                            def chestLock():

                                                                st.insert(
                                                                    END, "\nthe chest is locked")
                                                                st.insert(
                                                                    END, "\n what you wanna do")
                                                                o1.destroy()
                                                                o2.destroy()
                                                                paper()
                                                                st.yview(END)

                                                            o1.configure(
                                                                command=chestLock)
                                                            o2.configure(
                                                                command=puzzleSolve)

                                                        paper()
                                                        l1.destroy()
                                                        l2.destroy()

                                                    def n():
                                                        l1.destroy()
                                                        l2.destroy()
                                                        TrailAction()

                                                    l1.configure(
                                                        command=chestOpenTrial)
                                                    l2.configure(command=n)

                                                checkCart()

                                            def nothingElse():
                                                c10.destroy()
                                                c11.destroy()
                                                st.insert(
                                                    END, "\n There is nothing else here")
                                                TrailAction()
                                                st.yview(END)

                                            c10.configure(command=seeCart)
                                            c11.configure(command=nothingElse)

                                        TrailAction()

                                    c7.configure(command=homeWindow)
                                    c8.configure(command=safe)
                                    c9.configure(command=cart)

                                inner1()

                            checkHome()

                        c5.configure(command=Headman)
                        c6.configure(command=home)

                    inner()

                c3.configure(command=noInfo)
                c4.configure(command=leaveBar)

            leave()

        c1.configure(command=postOffice)
        c2.configure(command=bar)
    beginning()


d.configure(command=start)
d_window = f.create_window(100, 0, anchor=NW, window=d)
gg.mainloop()
