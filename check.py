from cProfile import label
from email.mime import image
from tkinter import*
from tkinter.font import BOLD
from turtle import back
from PIL import Image,ImageTk

from matplotlib.pyplot import text
import colorama
root=Tk()

root.title("<= Mr.JTX bug checklist =>")
root.geometry("800x500") 
chk=Label(root,text='''                                                 Mr.jtx Checklist                                                   ''',bg="black",fg="yellow",font=('arial',35,'bold'))
chk.pack(side=TOP)
imgae=Image.open("j.jpg")
photo=ImageTk.PhotoImage(imgae)
vl=Label(image=photo)
vl.pack()
def portscan():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit simple Port Bugs")
    a=Label(top,text='''Just run nmap on the target. if you find any of these port 
    try to some basic exploit like check fuzz the port 9100
    port 9100 contain may information
    try user enume exploit on 21
    any run vuln script of nmap on then 
    [*]If we find CVE for version 3.0.0 but got the cve exploit for 3.0.3 than it means 
    it may works on its older version
    [*]SSH=> version 2.3 to 7.7 all are vullenerable to one bug called user enume
    [*]9100=> Fuss this port it contain Information metrics info and many very confidientiol info
    eg:-127.0.0.1:9100/metrics
    [*]''',font=('arial',16,'bold'))
    a.pack()
def oldsession1():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit Old session dose't expire(emailorpasschange)  ")
    a=Label(top,text='''Open 2 browsers
    login in both browsers and then reset the password in one browser
    and then refresh both browser if you still loged in both browsers 
    means its a bug''',font=('arial',16,'bold'))
    a.pack()
def pasrestlinknexpir():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit Pass reset link dose't expire(afteronetimeuse")
    a=Label(top,text='''Deman the password reset link from the web site 
    and change the password by using the reset link 
    after you reset the pass word click and try to reset the password again 
    from the same link if you can do this that means it is a bug in the web site''',font=('arial',16,'bold'))
    a.pack()
def oldlinknexpemailch():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit Last pass reset link dose't expire(afteremailchange ")
    a=Label(top,text='''Demand a reset password link from the web site but do't
    click on the reset link instend go and change the user name or email and 
    then click on that reset link then if you able to reset the password 
    then its a bug ''',font=('arial',16,'bold'))
    a.pack()
def exifdtanotettripped():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit exif data not striped")
    a=Label(top,text='''Exif data is stored info in a image when picture is taken
    [+]Step to reproduce
    [*]Find image upload paremerter like logo/profile pic/grouppic etc
    [*]Upload an image that contain exif data in it
    [*]Download that file by doing copy or save as 
    [*]Upload that downloaded file to the jimpl.com to extrect its exif data
    [+]if you got the location in exif data that means its a P3 Bug''',font=('arial',16,'bold'))
    a.pack()
def emailHtml():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit email HTML injection")
    a=Label(top,text='''Step to reproduce :-
    [*] Enter the HTML code in the user name paremeter 
    [*] you will get the verification code in the email starting with you name is now 
    [+]started with html code got execute in the email. where the reflect should happen.
    
    [-]Paremeter :- Sinup page,invite user ,org name,
    company name etc''',font=('arial',16,'bold'))
    a.pack()

def Textinjecton():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit Text injection")
    a=Label(top,text='''Step to reproduce :-
    [+]This bug mostly find in word press
    [*]just check the url and the text in the website content
    are same eg:-
    https://hackerone.com/?error=can't+open+this+page
    
    eg:-
    [Domain]/confirm_email=<email>&email=<email>''',font=('arial',16,'bold'))
    a.pack()

def weakpaspoliy():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit weak password pass policy ")
    a=Label(top,text='''Step to reproduce :-
    just regester on the web site and try to set the simple password as 123456789
    if you can set the pass means its a bug
    
    Paremeter:-
    [*]singup page
    [*]reset password''',font=('arial',16,'bold'))
    a.pack()
def openredirec():
     top=Toplevel(root)
     top.geometry("750x750")
     top.title("How to exploit Open redirect")
     a=Label(top,text='''url redirection to untrustedsite:-
     eg:- jatin.com/login=app.jatin.com
          jatin.com/login=evil.com
    Parameter:-
    url=
    path=
    redirect=
    file=
    find=
    from=
    
    Bug mainly foundon:-
    [+]login panal
    if we want to redirect on login panal then we have to input the valid credentials.
    
    [*]Where to find openredirect paremeter:-
       we are logged in the website eg:- jatin.com/profile
       then LogOut and try to acces the same path now the website will 
       automaticly give the a paremeter 
       
       [_____________________One more method__________________]
       Open redirect by path fregment if jatin.com///evali.com
       
       we have to test the path:-
       do automate the path fregment.
       Use FUFF tool to automate the redirect.''',font=('arial',16,'bold'))
     a.pack()

def insecdesing():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit weak password pass policy ")
    a=Label(top,text='''In Some websit we can invite many users by their email address 
    so we can exploit the flow by enter many email of one person we can and sepreat them with commas
    eg:-
    Enter email to invite :- rjatin305@gmail.com
    
    Attacker:-
    Enter email to invite :- rjatin305@gmail.com,rjatin305@gmail.com,rjatin305@gmail.com
    
    this missconfigration can lead to email bombing.''',font=('arial',16,'bold'))
    a.pack()
def BLH():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit Broken Link Hijacking ")
    a=Label(top,text='''Description :-
    Broken Link Hijacking (BLH) is a web-based attack where the attackers take over 
    expired, stale, and invalid external links on credible websites/ web applications
    for malicious/ fraudulent purposes. These external links are used for a multitude
    of purposes ranging from SEO to load resources from external URLs/ points.''',font=('arial',16,'bold'))
    a.pack()
def hyperexecution():
    top=Toplevel(root)
    top.geometry("750x750")
    top.title("How to exploit weak password pass policy ")
    a=Label(top,text='''Step to reproduce :-
    We can give any other web site link to a user name parammeter if that name parammeter is one 
    click executable because the website link is reflected back in the mail.
    [+]Testing param:-
    org/company/group names => first Name,last name any parammeter which reflect in the invite email''',font=('arial',16,'bold'))
    a.pack()
chbt=Checkbutton(root,text="Check vuln port(21,111,9100,22)                                    ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=100)
chbt=Button(root,text="Help",command=portscan)
chbt.pack()
chbt.place(x=600,y=100)

chbt=Checkbutton(root,text="Old session dose't expire(emailorpasschange)           ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=140) 
chbt=Button(root,text="Help",command=oldsession1)
chbt.pack()
chbt.place(x=600,y=140)

chbt=Checkbutton(root,text="Pass reset link dose't expire(afteronetimeuse)            ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=180)
chbt=Button(root,text="Help",command=pasrestlinknexpir)
chbt.pack()
chbt.place(x=600,y=180)

chbt=Checkbutton(root,text="Last pass reset link dose't expire(afteremailchange)  ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=220)
chbt=Button(root,text="Help",command=oldlinknexpemailch)
chbt.pack()
chbt.place(x=600,y=220)

chbt=Checkbutton(root,text="Exif data not sttripped from uploded img                     ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=260)
chbt=Button(root,text="Help",command=exifdtanotettripped)
chbt.pack()
chbt.place(x=600,y=260)

chbt=Checkbutton(root,text="Email HTML injection                                                      ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=300)
chbt=Button(root,text="Help",command=emailHtml)
chbt.pack()
chbt.place(x=600,y=300)

chbt=Checkbutton(root,text="Text injection/content soofing                                       ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=340)
chbt=Button(root,text="Help",command=Textinjecton)
chbt.pack()
chbt.place(x=600,y=340)


chbt=Checkbutton(root,text="Weak password policy                                                   ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=380)
chbt=Button(root,text="Help",command=weakpaspoliy)
chbt.pack()
chbt.place(x=600,y=380)

chbt=Checkbutton(root,text="Open redirect                                                                  ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=420)
chbt=Button(root,text="Help",command=openredirec)
chbt.pack()
chbt.place(x=600,y=420)


chbt=Checkbutton(root,text="Incure Desing Flow                                                         ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=460)
chbt=Button(root,text="Help",command=insecdesing)
chbt.pack()
chbt.place(x=600,y=460)


chbt=Checkbutton(root,text="Broken Link Hijacking                                                       ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=500)
chbt=Button(root,text="Help",command=BLH)
chbt.pack()
chbt.place(x=600,y=500)

chbt=Checkbutton(root,text="Hyperlink execution                                                       ",bg="black",fg="red",font=('arial',16,'bold'))
chbt.place(x=5,y=540)
chbt=Button(root,text="Help",command=hyperexecution)
chbt.pack()
chbt.place(x=600,y=540)

























root.mainloop()
