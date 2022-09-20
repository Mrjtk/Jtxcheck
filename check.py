from cProfile import label
from email.mime import image
from tkinter import*
from tkinter.font import BOLD
from turtle import back



import colorama
usr=Tk()
usr.title("<= Mr.JTX bug checklist =>")
usr.geometry("1100x800") 
chk=Label(usr,text='''                                                 Mr.jtx Checklist                                                   ''',bg="black",fg="yellow",font=('arial',35,'bold'))
chk.pack(side=TOP)
chk.configure(background='red')
usr.configure(background='black')
def lowhang():
                root=Tk()
                root.title("<= Mr.JTX bug checklist =>")
                root.geometry("1100x800") 
                           
                root.configure(background='black')
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
                    top.title("How to exploit Hyperlink execution ")
                    a=Label(top,text='''Step to reproduce :-
                    We can give any other web site link to a user name parammeter if that name parammeter is one 
                    click executable because the website link is reflected back in the mail.
                    [+]Testing param:-
                    org/company/group names => first Name,last name any parammeter which reflect in the invite email''',font=('arial',16,'bold'))
                    a.pack()
                def critfileexpo():
                    top=Toplevel(root)
                    top.geometry("750x750")
                    top.title("How to exploit Hyperlink execution ")
                    a=Label(top,text='''Step to reproduce :-
                    The important file can be expose to normal user
                    like->log files, .htaccess , info.php, web.conf, web.config ,filemanager
                    debug.log, matrix
                    
                    Tools to find this:-
                    
                    Fuzz
                    dirbuster
                    dirsearch etc...
                    
                    command for the dirsearch
                    
                    dirsearch -u <url> -w <wordlist> -i <greb the responce>''',font=('arial',16,'bold'))
                    a.pack()
                def incaccdeletion():
                    top=Toplevel(root)
                    top.geometry("750x750")
                    top.title("How to exploit Hyperlink execution ")
                    a=Label(top,text='''Step to reproduce :-
                Lack of password confermance(Delete Account)
                
                Whil we delete any account the website do not ask any OTP
                ,password,2FA etc from us to delete the account then its a bug
                
                [*]While we are doing any payment with any other confermation like 
                OTP,UPI its a bug''',font=('arial',16,'bold'))
                    a.pack()
                def csvinje():
                    top=Toplevel(root)
                    top.geometry("750x750")
                    top.title("How to exploit Hyperlink execution ")
                    a=Label(top,text='''Step to reproduce :-
                When ever we work on the website and the data get
                saved in the web site as excel file so we will try
                to inject some formula in that file and the file execute in the victum
                
                Where to test:-
                Make a CSV file and download and check it if it contain any reflected 
                data in it and change that reflected parameter with the CSV payload and 
                download the file and see if the payload execuite or not ''',font=('arial',16,'bold'))
                    a.pack()
                def serlogexp():
                    top=Toplevel(root)
                    top.geometry("750x750")
                    top.title("Expose server logs ")
                    a=Label(top,text='''Step to reproduce :-
                    logs:-
                    1. nginx-status
                    2.haproxy-status
                    3.exposed-metrix
                    4.through open port 

                    How to find:-
                        Use directory busting and fuzzing 
                        And add some special char in the input password peremeters
                ''',font=('arial',16,'bold'))
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


                chbt=Checkbutton(root,text="Broken Link Hijacking                                                     ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=500)
                chbt=Button(root,text="Help",command=BLH)
                chbt.pack()
                chbt.place(x=600,y=500)

                chbt=Checkbutton(root,text="Hyperlink execution                                                        ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=540)
                chbt=Button(root,text="Help",command=hyperexecution)
                chbt.pack()
                chbt.place(x=600,y=540)

                chbt=Checkbutton(root,text="Critical file exposed                                                        ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=580)
                chbt=Button(root,text="Help",command=critfileexpo)
                chbt.pack()
                chbt.place(x=600,y=580)


                chbt=Checkbutton(root,text="Inscure Account Deletion                                               ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=620)
                chbt=Button(root,text="Help",command=incaccdeletion)
                chbt.pack()
                chbt.place(x=600,y=620)


                chbt=Checkbutton(root,text="CSV Injection                                                         ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=700,y=100)
                chbt=Button(root,text="Help",command=csvinje)
                chbt.pack()
                chbt.place(x=1200,y=100)


                chbt=Checkbutton(root,text="Expose server logs                                                      ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=700,y=140)
                chbt=Button(root,text="Help",command=serlogexp)
                chbt.pack()
                chbt.place(x=1200,y=140)
                root.mainloop()
chbt=Button(usr,text="Low Hanging Bugs",font=('arial',16,'bold'),command=lowhang)
chbt.pack()
chbt.place(x=5,y=100)



def Goodbug():
                usr2=Tk()
                usr2.title("<= Good Bugs  =>")
                usr2.geometry("1100x800") 
                usr2.configure(background='black')
                

                def resmnuinviteuser():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to exploit Pass reset link dose't expire(afteronetimeuse")
                    a=Label(top,text='''Invite user
                    [*]We invite any user and it invite refflect in the responce 
                    than we can directly invite the user
                    
                    Bug:-
                    Check the invition token in the response.
                                        if you found the token then its a bug 
                                        
                    Reproduce:-
                     Invite user -> Intersept -> do intersept the responce -> and copy it and past it some where else and go to the
                     invited user mail and copy the url addres and check for the token frome the url in the responce 
                     
                     Parameter:-
                     Confermation
                     conferm
                     etc.''',font=('arial',16,'bold'))
                    a.pack()
                def applicationdos():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to exploit appllication level dos")
                    a=Label(top,text='''Step to re-pro :-
                    Try to enter super long password on singup and if it did't work then try it on singin page
                    
                    [*]If want to check i burp Suit go and check responce 500 .''',font=('arial',16,'bold'))
                    a.pack()
                def Emailverificationbypass():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to bypass email verification")
                    a=Label(top,text='''Step to re-pro :-
                    [*]We got a otp in email we will try to bypass that function
                    [*]Fill the wrong otp and intersept its request 
                    [*]click Do intercept the request and change the paremeters in the response         
                    ''',font=('arial',16,'bold'))
                    a.pack()
                def Oauthtoaccounttakovr():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to do Oauth leads to acount take over")
                    a=Label(top,text='''     
                    Oauth-> Info sharing with out showing the password 

                    [Oauth missconf leads to pre account takeover]
                    step to reproduce:-
                    * Creat an account with victum email munualy 
                    * Just go and do login Oauth from google or -- by the same victum email
                    *Log out from the Oauth loged in account 
                    *Go login by the user email and password which you created early in 1 step

                    If you get loged in and do't get any error worning then its a P2 BUG   
                    ''',font=('arial',16,'bold'))
                    a.pack()
                def Noratelimit():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to do Noratelimit")
                    a=Label(top,text='''     
                    No rate Limit:-
                    Parameter:-
                    login form
                    sing in
                    forget password
                    Otp/code
                    sir fav-> Contact form
                              invite user
                    Login form-> Brute force
                    sign up->email bombing
                    forget passwrod->email bombing
                    otp -> brute borce
                    contact form -> htnlinjection , bombing ''',font=('arial',16,'bold'))
                    a.pack()
                def Passwordspraying():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to do Password spraying")
                    a=Label(top,text='''     
                    If we can't do Password then we do Password spraying attack
                    
                    Brute Force:-
                    username-> Constant
                    Password->Rotating 
                    
                    But
                    
                    Spraying attack:-
                    username->Rotating
                    Password->Constant
                     
                     In this attack we will brute force username paremeter ''',font=('arial',16,'bold'))
                    a.pack()    
                def Intercommisconfig():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to Exploit Intercome Misconfig")
                    a=Label(top,text='''Intercome chat box :-
                    Go and find email on the website related domain like support etc.

                    Do Right click-> Console 
                    use payload 
                    Intercom('boot',{email:support@gmail});

                    if it show -> undefine then its a bug
                    other wise show any error then its not

                    ''',font=('arial',16,'bold'))
                    a.pack() 
                def sessionmange():
                    top=Toplevel(usr2)
                    top.geometry("750x750")
                    top.title("How to exploit sessionmange ")
                    a=Label(top,text='''We have 3 members in a group and Jatin is the admin
                    .Jatin remove user 1 but the removerd user session did't get expire 
                    and he still have access of the group until unless he logout from him self''',font=('arial',16,'bold'))
                    a.pack()
                chbt=Checkbutton(usr2,text="Responce manuplation invite usr                                  ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=140)
                chbt=Button(usr2,text="Help",command=resmnuinviteuser)
                chbt.pack()
                chbt.place(x=600,y=140)
               
                chbt=Checkbutton(usr2,text="Application level Dos...                                                   ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=180)
                chbt=Button(usr2,text="Help",command=applicationdos)
                chbt.pack()
                chbt.place(x=600,y=180)
                  
                chbt=Checkbutton(usr2,text="Email verification Bypass                                               ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=220)
                chbt=Button(usr2,text="Help",command=Emailverificationbypass)
                chbt.pack()
                chbt.place(x=600,y=220)

                chbt=Checkbutton(usr2,text="Oauth Email verification Bypass                                    ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=260)
                chbt=Button(usr2,text="Help",command=Oauthtoaccounttakovr)
                chbt.pack()
                chbt.place(x=600,y=260)

                chbt=Checkbutton(usr2,text="No rate Limit                                                                     ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=300)
                chbt=Button(usr2,text="Help",command=Oauthtoaccounttakovr)
                chbt.pack()
                chbt.place(x=600,y=300)
                
                chbt=Checkbutton(usr2,text="Password spraying                                                         ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=340)
                chbt=Button(usr2,text="Help",command=Passwordspraying)
                chbt.pack()
                chbt.place(x=600,y=340)
                
                chbt=Checkbutton(usr2,text="Intercome Misconfig                                                       ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=380)
                chbt=Button(usr2,text="Help",command=Intercommisconfig)
                chbt.pack()
                chbt.place(x=600,y=380)
                
                chbt=Checkbutton(usr2,text="Session management                                                     ",bg="black",fg="red",font=('arial',16,'bold'))
                chbt.place(x=5,y=420)
                chbt=Button(usr2,text="Help",command=sessionmange)
                chbt.pack()
                chbt.place(x=600,y=420)
                usr2.mainloop()

def recon():
                    top=Toplevel(usr)
                    top.geometry("750x750")
                    top.title("How to recon")
                    a=Label(top,text='''
                    Best tool 
                    [reconfw]=>need to have high CPU+GPU
                    this tool should be run in a cloud 

                    [*]We have to find some Subdomains from tools like sublist3r etc.

                    [*]Check for live subdomains by httpx:-
                    eg:- <file> | httpx

                    some steps:
                    1.Port scanning 
                    2.httpx
                    3.fuzzing 
                    4.Munual visit

                    Try to see uncomman ports

                    [*+*]Use {nuclie} tool to scan automate
                    ''',font=('arial',16,'bold'))
                    a.pack()               


























chbt=Button(usr,text="Easy to find Bugs",font=('arial',16,'bold'),command=Goodbug)
chbt.pack()
chbt.place(x=5,y=200)


chbt=Button(usr,text="Recon     ",font=('arial',16,'bold'),command=recon)
chbt.pack()
chbt.place(x=500,y=200)
usr.mainloop()
