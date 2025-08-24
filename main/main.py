from tkinter import *
from db import Database
from tkinter import messagebox
from myapi import API
import paralleldots




class NlpApp:
    def __init__(self):
        self.dbo = Database()
        self.apio = API()
        self.root = Tk()
        self.root.title('Nlp')
        self.root.geometry('350x700')
        self.root.configure(bg='#0d1117')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        print(self.apio.ner("Hugging Face is based in Paris."))
        heading = Label(self.root,text="NlpApp",bg="#0d1117",fg='#f0f6fc')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))
        
        gmail = Label(self.root,text='Enter Email',bg="#0d1117",fg='#7d8590')
        gmail.pack(pady=(10,10))
        gmail.configure(font=('verdana',20,'bold'))
        
        self.gmail = Entry(self.root,width=30,bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.gmail.pack(pady=(5,10),ipady=8)
        
        Passwd = Label(self.root,text='Enter Password',bg="#0d1117",fg='#7d8590')
        Passwd.pack(pady=(10,10))
        Passwd.configure(font=('verdana',20,'bold'))
        
        self.Passwd = Entry(self.root,width=30,show='*',bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.Passwd.pack(pady=(5,10),ipady=8)
        
        Sign_up_Button = Button(self.root,text='Sign Up',width=20,bg='#238636',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#2ea043',cursor='hand2',command=self.perform_login)
        Sign_up_Button.pack(pady=(40,10),ipady=5)
        
        Not_mem = Label(self.root,text='Register Below -->',bg="#0d1117",fg='#58a6ff')
        Not_mem.pack(pady=(30,10))
        
        Redirect_Button = Button(self.root,text='Register Now',width=20,command=self.register_gui,bg='#1f6feb',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#388bfd',cursor='hand2')
        Redirect_Button.pack(pady=(30,10),ipady=5)

    def clear(self):
        # clear gui
        for i in self.root.pack_slaves():
            print(i.destroy())

    def register_gui(self):
        self.clear()
        
        heading = Label(self.root,text="NlpApp",bg="#0d1117",fg='#f0f6fc')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))
        
        name = Label(self.root,text='Enter Your Name',bg="#0d1117",fg='#7d8590')
        name.pack(pady=(10,10))
        name.configure(font=('verdana',20,'bold'))
        
        self.name = Entry(self.root,width=30,bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.name.pack(pady=(5,10),ipady=8)
        
        gmail = Label(self.root,text='Enter Email',bg="#0d1117",fg='#7d8590')
        gmail.pack(pady=(10,10))
        gmail.configure(font=('verdana',20,'bold'))
        
        self.gmail = Entry(self.root,width=30,bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.gmail.pack(pady=(5,10),ipady=8)
        
        Passwd = Label(self.root,text='Enter Password',bg="#0d1117",fg='#7d8590')
        Passwd.pack(pady=(10,10))
        Passwd.configure(font=('verdana',20,'bold'))
        
        self.Passwd = Entry(self.root,width=30,show='*',bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.Passwd.pack(pady=(5,10),ipady=8)
        
        Register_Button = Button(self.root,text='Register',width=20,command=self.perform_registeration,bg='#238636',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#2ea043',cursor='hand2')
        Register_Button.pack(pady=(40,10),ipady=5)
        
        Alr_mem = Label(self.root,text='Already a Member? -->',bg="#0d1117",fg='#58a6ff')
        Alr_mem.pack(pady=(30,10))
        
        Redirect_Button = Button(self.root,text='Login',width=20,command=self.login_gui,bg='#1f6feb',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#388bfd',cursor='hand2')
        Redirect_Button.pack(pady=(30,10),ipady=5)

    def perform_registeration(self):
        name = self.name.get()
        gmail = self.gmail.get()
        passwd = self.Passwd.get()
        
        response = self.dbo.add_data(name,gmail,passwd)
        if response:
            messagebox.showinfo('Success!',"Registeration Successfull. You can login now.")
        else:
            messagebox.showerror('Error!','Email already Exists')

    def perform_login(self):
        gmail = self.gmail.get()
        passwd = self.Passwd.get()

        response = self.dbo.search(gmail,passwd)

        if response:
            messagebox.showinfo("Logged in!","Login Successful!")
            self.home_gui()
        else:
            messagebox.showerror('Error!',"Incorrect email or password")

    def home_gui(self):
        self.clear()
        heading = Label(self.root,text="NlpApp",bg="#0d1117",fg='#f0f6fc')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))

        Sentiment_Button = Button(self.root,text='Sentiment Analysis',width=25,command=self.sentiment_gui,bg='#da3633',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#f85149',cursor='hand2')
        Sentiment_Button.pack(pady=(30,10),ipady=5)

        Ner_Button = Button(self.root,text='Named Entity Recognition',width=25,command=self.ner_gui,bg='#a855f7',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#c084fc',cursor='hand2')
        Ner_Button.pack(pady=(30,10),ipady=5)        

        Emotion_Button = Button(self.root,text='Emotion Analysis',width=25,command=self.emotion_gui,bg='#0ea5e9',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#38bdf8',cursor='hand2')
        Emotion_Button.pack(pady=(30,10),ipady=5)

        Logout_Button = Button(self.root,text='🚪 Logout',width=25,command=self.login_gui,bg='#ef4444',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#dc2626',cursor='hand2')
        Logout_Button.pack(pady=(30,10),ipady=5)


    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root,text="NlpApp",bg="#0d1117",fg='#f0f6fc')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))   

        heading2 = Label(self.root,text="Sentiment Analysis",bg="#0d1117",fg='#7d8590')
        heading2.pack(pady=(5,20))
        heading2.configure(font=('verdana',26))

        Para = Label(self.root,text='Enter Your Paragraph -->',bg="#0d1117",fg='#58a6ff')
        Para.pack(pady=(30,10))

        self.sentiment = Entry(self.root,width=30,bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.sentiment.pack(pady=(5,10),ipady=8)

        Sentiment_Button = Button(self.root,text='Analyze Now',width=20,command=self.perform_sentiment,bg='#1f6feb',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#388bfd',cursor='hand2')
        Sentiment_Button.pack(pady=(30,10),ipady=5)

        self.Result_sent = Label(self.root,text="",bg="#0d1117",fg='#7d8590')
        self.Result_sent.pack(pady=(5,20))
        self.Result_sent.configure(font=('verdana',18))

        Goback_Button = Button(self.root,text='🚪 Back',width=25,command=self.home_gui,bg='#ef4444',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#dc2626',cursor='hand2')
        Goback_Button.pack(pady=(30,10),ipady=5)

    def perform_sentiment(self):
        text = self.sentiment.get()
        response = self.apio.sentiment_analysis(text)

        txt = ''
        for i in response:   # response is already a list of dicts
            txt += f"{i['label']} -> {round(i['score'], 3)}\n"

        result = Label(self.root, text=txt, bg='#0d1117', fg='#7d8590')
        result.pack(pady=(10, 10))

    def ner_gui(self):
        self.clear()
        heading = Label(self.root,text="NlpApp",bg="#0d1117",fg='#f0f6fc')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))   

        heading2 = Label(self.root,text="Named Entity Recognition",bg="#0d1117",fg='#7d8590')
        heading2.pack(pady=(5,20))
        heading2.configure(font=('verdana',20))

        Para = Label(self.root,text='Enter Your Paragraph -->',bg="#0d1117",fg='#58a6ff')
        Para.pack(pady=(30,10))

        self.ner = Entry(self.root,width=30,bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.ner.pack(pady=(5,10),ipady=8)

        ner_Button = Button(self.root,text='Analyze Now',width=20,command=self.perform_ner,bg='#1f6feb',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#388bfd',cursor='hand2')
        ner_Button.pack(pady=(30,10),ipady=5)

        self.Result_sent = Label(self.root,text="",bg="#0d1117",fg='#7d8590')
        self.Result_sent.pack(pady=(5,20))
        self.Result_sent.configure(font=('verdana',18))

        Goback_Button = Button(self.root,text='🚪 Back',width=25,command=self.home_gui,bg='#ef4444',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#dc2626',cursor='hand2')
        Goback_Button.pack(pady=(30,10),ipady=5)

    def perform_ner(self):
        text = self.ner.get()
        response = self.apio.ner(text)

        txt = ""
        if response:
            for ent in response:
                txt += f"{ent.word} -> {ent.entity_group} ({round(ent.score, 3)})\n"
        else:
            txt = "No entities found."

        result = Label(self.root, text=txt, bg='#0d1117', fg='#7d8590', justify="left")
        result.pack(pady=(10, 10))

    def emotion_gui(self):
        self.clear()
        heading = Label(self.root,text="NlpApp",bg="#0d1117",fg='#f0f6fc')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))   

        heading2 = Label(self.root,text="Emotion Detector",bg="#0d1117",fg='#7d8590')
        heading2.pack(pady=(5,20))
        heading2.configure(font=('verdana',25))

        Para = Label(self.root,text='Enter Your Paragraph -->',bg="#0d1117",fg='#58a6ff')
        Para.pack(pady=(30,10))

        self.emotion = Entry(self.root,width=30,bg='#21262d',fg='#f0f6fc',insertbackground='#58a6ff',bd=0)
        self.emotion.pack(pady=(5,10),ipady=8)

        emotion_Button = Button(self.root,text='Analyze Now',width=20,command=self.perform_emotion,bg='#1f6feb',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#388bfd',cursor='hand2')
        emotion_Button.pack(pady=(30,10),ipady=5)

        self.Result_sent = Label(self.root,text="",bg="#0d1117",fg='#7d8590')
        self.Result_sent.pack(pady=(5,20))
        self.Result_sent.configure(font=('verdana',18))

        Goback_Button = Button(self.root,text='🚪 Back',width=25,command=self.home_gui,bg='#ef4444',fg='white',bd=0,font=('verdana',12,'bold'),activebackground='#dc2626',cursor='hand2')
        Goback_Button.pack(pady=(30,10),ipady=5)

        
    def perform_emotion(self):
        text = self.emotion.get()
        response = self.apio.emotion(text)

        txt = ""
        for r in response:
            txt += f"{r['label']} -> {round(r['score'], 3)}\n"

        result = Label(self.root, text=txt, bg='#0d1117', fg='#7d8590')
        result.pack(pady=(10, 10))



object = NlpApp()