#CODED BY : MUHAMMAD HAMMAD
#AUTHOR : MUGHAL ZADA
#SOURCE : LOGO NAME
import os
import random
import requests
import pyfiglet
def clear():
    os.system('clear')
    print(logo)
def mughalxd():
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
logo = ("""
██╗  ██╗ █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗
██║  ██║██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗
███████║███████║██╔████╔██║██╔████╔██║███████║██║  ██║
██╔══██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║  ██║
██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mAuthor      : MUGHAL ZADA
 \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mFacebook    : MUHAMMAD HAMMAD
 \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mCode by     : MAKE LOGO""")
def generate_custom_ascii_logo(name, font_style='standard'):
    try:
        ascii_art = pyfiglet.figlet_format(name, font=font_style)
        print(ascii_art)
    except pyfiglet.FigletError as e:
  
        print(f"Error: {e}")
def generate_unique_logos(name, num_logos, font_style='standard'):
    used_styles = set()
    #YAHA NICHY LIMIT RAKH SAKTE HO AP KITNY LOGO GENERATE KRWANA CHAHTY HO
    for i in range(min(num_logos, 100)):
        while True:
            current_style = font_style if i == 0 else pyfiglet.Figlet().getFonts()[i % len(pyfiglet.Figlet().getFonts())]
            if current_style not in used_styles:
                used_styles.add(current_style)
                break
        generate_custom_ascii_logo(name, current_style)
os.system('clear')
print(logo)
mughalxd()
user_name = input(" \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mEnter Your Name : ")
num_logos = int(input(" \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mHow Many Logo Do You Want To Gen : "))
user_font_style = input(" \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mPress Enter : ")
if not user_font_style:
    user_font_style = 'standard'
    os.system("clear");print(logo)
    mughalxd();print(" \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mRUNNING START MAKE YOUR NAME LOGO");mughalxd()
generate_unique_logos(user_name, num_logos, user_font_style)
print(" \033[1;36m[\033[1;37m+\033[1;36m] \033[1;37mProcess Completed")
#CODE BY MUGHAL ZADA OPEN SOURCE