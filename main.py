import curses
import requests
import time
import os
import sys
import platform
from datetime import datetime
import psutil
import math
from mcstatus import MinecraftServer
import json
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Astro - beta version - built: 8/25/2202 11:33")

from colorama import init, Fore
init()



def checkIfProcessRunning(processName):
        '''Check if there are any running process that contains the given name processName.
        Iterate over the all the running process'''
        for proc in psutil.process_iter():
                try:
                        # Check if process name contains the given name string.
                        if processName.lower() in proc.name().lower():
                                return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        return False;

with open("services.json") as file:
        servicechecks = json.load(file)

with open("servers.json") as file:
        mcserverchecks = json.load(file)
        

#servicechecks = ["faceit", "EasyAntiCheat", "vanguard","BattleEye", "xigncode3", "veracrypt", "avast", "cpuz", "csgo", "tf2", "Lunar Client", "steam"]
#mcserverchecks = ["mc.hypixel.net", "lunar.gg", "mineplex.com"]

def colorbool(textin):
    if str(textin)== "True":
        return((Fore.GREEN + "On" + Fore.WHITE))

    else:
        return((Fore.RED + "Off" + Fore.WHITE))
    

def main(stdscr):
        curses.noecho()
        curses.curs_set(0)
        #resize = curses.is_term_resized(22, 86)

# Action in loop if resize is True:
        curses.resize_term(39, 125)
        #input()
            
        dt=datetime.now()
        
        consolecreationtime = time.time()

        stdscr = curses.initscr()

        curses.echo()
        size = os.get_terminal_size()



        text = ("""
                      :::!~!!!!!:.            |
                  .xUHWH!! !!?M88WHX:.        |
                .X*#M@$!!  !X!M$$$$$$WWx:.    |
               :!!!!!!?H! :!$!$$$$$$$$$$8X:   |
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:  |
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!  |
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!  |
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!  |
               ~?WuxiW*`   `"#$$$$8!!!!??!!!  |
             :X- M$$$$       `"T#$T~!8$WUXU~  |
            :%`  ~#$$$m:        ~!~ ?$$$$$$   |
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"   |
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`    |
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :      |
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`      |
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~       |
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `          |
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!             |
$R@i.~~ !     :   ~$$$$$B$$en:``              |
?MXT@Wx.~    :     ~"##*$$$$M~                |
""")


        text2 = ("""
            ,-~¨^  ^¨-,           _,
           /          / ;^-._...,¨/
          /          / /         /
         /          / /         /
        /          / /         /
       /,.-:''-,_ / /         /
       _,.-:--._ ^ ^:-._ __../
     /^         / /¨:.._¨__.;
    /          / /      ^  /
   /          / /         /
  /          / /         /
 /_,.--:^-._/ /         /
^            ^¨¨-.___.:^ 

""")

        osuptime = (consolecreationtime - time.time())

        data_text1 = ("""
Windows OS Version: {osversion}
Windows OS Build:   {osbuild}
Window start time:  {osuptime}
""").format(osbuild = platform.version(), osversion = platform.release(), osuptime = math.floor(consolecreationtime))


        osuptime = (consolecreationtime - time.time())

        username = ("user")
        start = time.time()
        ipdata = requests.get('https://api.ipify.org').text
        ip = str(ipdata)[:2] + ((len(ipdata)-2)*"*")
        end = time.time()
        responsetime = (end - start)

        data_text2 = ("""
----Initialization data----
Version 1.0b
username: {username}
Requesting from: {userip}
Response time: {responsetime}ms

unread alarts: 0
unread conversations: 0
veteran: yes
beta: yes
vip: yes
posts: N/A
score: N/A
""").format(username=username, userip=ip, responsetime=str(math.floor(responsetime*1000)))

        #datetimedata_text=("""
        #%H:%M%S
        #%A - %b %d
        #""")

        datetimedata_text=dt.strftime("""%H:%M:%S
%A - %b %d""")
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

        skullwindow = curses.newwin(22, 48, 0, 0)
        try:
                skullwindow.addstr(0,0,text)
        except curses.error:
                pass
        #skullwindow.addstr(0,0,text)
        skullwindow.refresh()

        data1win = curses.newwin(4, 32, 0,48)

        try:
                data1win.addstr(0,0,data_text1)
        except curses.error:
                pass
        data1win.refresh()

        text2win = curses.newwin(16, 36, 4, 48)
        try:
                text2win.addstr(0,0,text2)
        except curses.error:
                pass

        text2win.refresh()

        curses.start_color()


        data2win = curses.newwin(16,32,5,86)
        try:
                data2win.addstr(0,0,data_text2)
        except curses.error:
                pass
        data2win.refresh()

        datetimedatawin = curses.newwin(2, 32,0, 86)
        try:
                datetimedatawin.addstr(0,0,datetimedata_text)
        except curses.error:
                pass
        datetimedatawin.refresh()

        task_text=("Initializating window")


        currenttaskwin = curses.newwin(2,32,3,86)
        try:
                currenttaskwin.addstr(0,0,"Current task: ")
                currenttaskwin.addstr(1,0,task_text)
        except curses.error:
                pass
        currenttaskwin.refresh()
        


        


        services = ("""faceit
EasyAntiCheat
vanguard
BattleEye
xigncode3
veracrypt
avast
cpuz
csgo
tf2
LunarClient
steam""")

        serviceswin1 = curses.newwin(16, 15, 23, 0)
        try:
                serviceswin1.addstr(0,0,"Service")
                serviceswin1.addstr(2,0, services)
        except curses.error:
                pass
        serviceswin1.refresh()


        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        checkstr=""
        #for i,v in enumerate(servicechecks):

        #checkstr = checkstr+(str(checkIfProcessRunning(x))) + "\n"


        serviceswin2 = curses.newwin(16,6,23,15)

        try:
                serviceswin2.addstr(0,0,"status")
        except curses.error:
                pass
        
        for i,v in enumerate(servicechecks):
                try:
                    currenttaskwin.clear()
                    currenttaskwin.addstr(1,0,("Checking proccess: " + str(v)))
                    currenttaskwin.refresh()

                    
                    currentbool = str(checkIfProcessRunning(v))
                    if currentbool=="True":
                        colortype = 2
                    else:
                        colortype=1
                
                    serviceswin2.addstr((i+2),0,currentbool, curses.color_pair(colortype))
                    serviceswin2.refresh()
                except curses.error:
                    pass

        bar=""
        for x in range(13):
                bar=bar+("""|
|
|
|
|
|
|
|
|
|
|
|
|
""") 


        servicexmcbar= curses.newwin(13,1,23, 22)
        try:
                servicexmcbar.addstr(0,0,bar)
        except curses.error:
                pass

        servicexmcbar.refresh()
        "servname | players | ping"

        mcbox = curses.newwin(10,40, 23,24)
        try:
                mcbox.addstr(0,0,"server ip | player count | ping")
        except curses.error:
                pass
        for i,v in enumerate(mcserverchecks):
                try:
                        currenttaskwin.clear()
                        currenttaskwin.addstr(1,0,("Checking server: " + str(v)))
                        currenttaskwin.refresh()
                        server = MinecraftServer.lookup(v)
                        status = server.status()
                        mctempdata = v +" | " + str(status.players.online) + " players" + " | " + str(math.floor(status.latency)) + "ms"
                except Exception as x:
                        mctempdata=("error " + str(v))
                        
                try:
                        mcbox.addstr((i+2),0,mctempdata)
                except curses.error:
                        pass
                mcbox.refresh()
                

        def timeupdatestuff():
                        osuptime = (math.floor((consolecreationtime - time.time())))*(-1)

                        data_text2 = ("""
Windows OS Version: {osversion}
Windows OS Build:   {osbuild}
Window Uptime:      {osuptime}
""").format(osbuild = platform.version(), osversion = platform.release(), osuptime = osuptime)
                        data1win.erase()
                        try:
                            data1win.addstr(0,0,data_text2)
                        except curses.error:
                            pass
                        
                        
                        dt=datetime.now()
                        datetimedata_text=dt.strftime("""%H:%M:%S
%A - %b %d""")
                        datetimedatawin.erase()
                        try:
                                datetimedatawin.addstr(0,0,datetimedata_text)
                        except curses.error:
                                pass
                        
                        stdscr.move(0, 0)
                        data1win.refresh()
                        datetimedatawin.refresh()

        
        while True:
                
                serviceswin2.clear()
                try:
                        serviceswin2.addstr(0,0,"status")
                except curses.error:
                       pass

                for i,v in enumerate(servicechecks):
                        time.sleep(.5)
                        try:


                            currenttaskwin.clear()
                            currenttaskwin.addstr(1,0,("Checking proccess: " + str(v)))
                            currenttaskwin.refresh()
                            
                            timeupdatestuff()
                            currentbool = str(checkIfProcessRunning(v))
                            if currentbool=="True":
                                colortype = 2
                            else:
                                colortype=1
        
                            serviceswin2.addstr((i+2),0,currentbool, curses.color_pair(colortype))
                        except curses.error:
                            pass

                serviceswin2.refresh()





########

                mcbox.clear()
                try:
                        mcbox.addstr(0,0,"server ip | player count | ping")
                except curses.error:
                        pass

                for i,v in enumerate(mcserverchecks):
                        time.sleep(.5)
                        currenttaskwin.clear()
                        currenttaskwin.addstr(1,0,("Checking server: " + str(v)))
                        currenttaskwin.refresh()
                        try:
                                timeupdatestuff()
                                server = MinecraftServer.lookup(v)
                                status = server.status()
                                mctempdata = v +" | " + str(status.players.online) + " players" + " | " + str(math.floor(status.latency)) + "ms"
                        except Exception as x:
                                mctempdata=("error " + str(v))
                                
                        try:
                                mcbox.addstr((i+2),0,mctempdata)
                        except curses.error:
                                pass
                mcbox.refresh()        


        



    
    
 #   curses.curs_set(0)
 #   stdscr.attron(curses.color_pair(1))
 #   stdscr.addchstr(0,0, text)
 #   stdscr.attroff(curses.color_pair(1))


#    stdscr.addchstr(48,48,data_text2)
    
#    stdscr.refresh()


curses.wrapper(main)

    
