from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from Download.img import Google
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        tw=Tk()
        global getURL
        getURL = StringVar()
        o = download(tw)
        tw.mainloop()
        if num == 1:
            a = Google()
            a.dir_create(a4)
            urls = a.get_image(a3, f" {var1.get()}", var3.get(), 1)
            try:
                for i, url in enumerate(urls):
                    a.download_image(f'C://Users//svk76//PycharmProjects//EV4//App_Downloads//{a4}//', url,
                                     str(i) + f".{var1.get()}")
            except Exception as e:
                print(e)
            a.quit()
        return 'The Download was complted Successfuly'
    else:
        return render_template('index.html')

class download:
    def __init__(self,tw):
        global var3
        global var
        global var1
        global var2
        global num
        var = StringVar()
        var.set('Select')
        var1 = StringVar()
        var2 = StringVar()
        var3 = IntVar()
        var3.set(100)
        global op
        global op2
        global op1
        op2 = ['png', 'jpeg', 'jpg']
        op = [i for i in range(100, 601, 100)]
        op1 = [i for i in range(1, 11)]
        self.tw=tw
        self.tw.title('Everything Downloader')
        self.tw.geometry("955x600")
        self.a1=PhotoImage(file=r"C:\Users\svk76\Downloads\Telegram Desktop\e.png")
        self.tw.iconphoto(self.tw,self.a1)
        self.l=Label(self.tw,text="Choose what to download:")
        self.l.grid(row=0,column=0)
        self.drop_down = OptionMenu(self.tw, var, "Images", "Videos", command=self.got)
        self.drop_down.grid(row=0, column=1, padx=5, pady=5)
        self.b = Button(self.tw, text='Submit',command=self.ent)
        self.b.grid(row=4, column=0, pady=10)
        self.b1 = Button(self.tw, text="Quit", command=self.close)
        self.b1.grid(row=4, column=3, pady=10)

    def clickDownload(self):
        if (getURL.get() == ""):
            messagebox.showinfo("ERROR", "ENTER url ")
            return
        a4 = self.e1.get()
        c = 0
        try:
            if var3.get()>len(videos):
                messagebox.showwarning("ERROR", f"Choose a smaller number less than or eaual to {len(videos)} ")
            else:
                for i in range(var3.get()):
                    quality = videos[i]
                    location = f'C://Users//svk76//PycharmProjects//EV4//App_Downloads//{a4}//'
                    quality.download(location, filename=str(c) + ".mp4")
                    c += 1
                messagebox.showinfo("Downloading Finish", yt.title + " has been downloaded Sucessfully!!!")
                self.tw.quit()
        except Exception as e:
            print(e)

    def img_1(self,img_2):
        global op
        try:
            if img_2 == 'png':
                var3.set(0)
                op = [i for i in range(100, 301, 50)]
                self.drop_down_num = OptionMenu(self.tw, var3, *op)
                self.drop_down_num.grid(row=1, column=3, padx=5, pady=5)
            elif img_2 == "jpeg":
                var3.set(0)
                op = [i for i in range(100, 601, 100)]
                self.drop_down_num = OptionMenu(self.tw, var3, *op)
                self.drop_down_num.grid(row=1, column=3, padx=5, pady=5)
            elif img_2=='jpg':
                var3.set(0)
                op = [i for i in range(100, 1001, 100)]
                self.drop_down_num = OptionMenu(self.tw, var3, *op)
                self.drop_down_num.grid(row=1, column=3, padx=5, pady=5)
            return None
        except Exception as e:
            print(e)

    def setURL(self):
        try:

            # Get URL of the Video
            url = getURL.get()
            print(url)

            # Create Object to hold the URL
            global yt
            yt = YouTube(url)
            print(yt.title)

            # Get the Quality of the Videos and store in the 'videos' variable
            global videos
            videos = yt.streams.filter(mime_type='video/mp4').all()
        except Exception as e:
            print(e)

    def got(self,v):
        global num
        if v=="Images":
            try:
                num = 1
                m1 = messagebox.askquestion('INFO', "Do you want to download Images")
                if m1 == "no":
                    var.set('')
                    pass
                if m1 == 'yes':
                    self.l1 = Label(self.tw, text="Search:")
                    self.l1.grid(row=1, column=0)
                    self.l2 = Label(self.tw, text="Folder name:")
                    self.l2.grid(row=2, column=0)
                    self.e = Entry(self.tw, width=30, borderwidth=3, font=('calibre', 10, 'normal'))
                    self.e.grid(row=1, column=1)
                    self.e1 = Entry(self.tw, width=30, borderwidth=3, font=('calibre', 10, 'normal'))
                    self.e1.grid(row=2, column=1, pady=10)
                    var1.set('Select')
                    var3.set(0)
                    self.drop_down_img = OptionMenu(self.tw, var1,*op2,command=self.img_1)
                    self.drop_down_img.grid(row=1, column=2, padx=5, pady=5)
                    self.drop_down_num = OptionMenu(self.tw, var3, *op,command=self.img_1)
                    self.drop_down_num.grid(row=1, column=3, padx=5, pady=5)
            except Exception as e:
                print(e)
        if v=="Videos":
            try:
                num = 2
                m1 = messagebox.askquestion('INFO', "Do you want to download Videos")
                if m1=="no":
                    pass
                if m1=='yes':
                    self.b = Button(self.tw, text='Submit', command=self.clickDownload)
                    self.b.grid(row=4, column=0, pady=10)
                    var2.set('Select')
                    var3.set(1)
                    self.b2=Button(self.tw,text='Set URL',command=self.setURL)
                    self.b2.grid(row=1,column=4,padx=5, pady=5)
                    self.drop_down_num = OptionMenu(self.tw, var3, *op1)
                    self.drop_down_num.grid(row=1, column=3, padx=5, pady=5)
                    self.drop_down_img = OptionMenu(self.tw, var2, "mp4  ")
                    self.drop_down_img.grid(row=1, column=2, padx=5, pady=5)
                    self.l1 = Label(self.tw, text="URL   :")
                    self.l1.grid(row=1, column=0)
                    self.l2 = Label(self.tw, text="Folder name:")
                    self.l2.grid(row=2, column=0)
                    self.e = Entry(self.tw, width=30, borderwidth=3, font=('calibre', 10, 'normal'),textvariable = getURL)
                    self.e.grid(row=1, column=1)
                    self.e1 = Entry(self.tw, width=30, borderwidth=3, font=('calibre', 10, 'normal'))
                    self.e1.grid(row=2, column=1, pady=10)
            except Exception as e :
                print(e)

    def close(self):
        res=messagebox.askyesno('Box',"Do you want to close application")
        if res==1:
            self.tw.destroy()
        else:
            pass
    def ent(self):
        global a3
        global a4
        a3=self.e.get()
        a4=self.e1.get()
        self.tw.destroy()

# Running the program


#tw=Tk()
#getURL = StringVar()
#o=download(tw)
#tw.mainloop()
#print(num)
if __name__=="__main__":
    app.run(debug=True, port=8001)

