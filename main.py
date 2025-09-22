#!/usr/bin/env python3
import os
import platform
import random
import shutil
import socket
import subprocess
import sys
import time
import requests
from colorama import Fore


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_all_ips():
    try:
        public_ip = requests.get("https://api.ipify.org?format=text", timeout=5).text.strip()
    except Exception as e:
        public_ip = f"Could not fetch | Error >> {e}"

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except Exception as e:
        hostname = local_ip = f"Could not fetch Hostname - Error >> {e}"

    print(f"Public IP >> {public_ip}\nLocal IP >> {local_ip}\nHostname >> {hostname}")

def ip_pinger_download(run_option, return_to_menu=True, download_option=True):
    ip_pinger_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/ip_pinger/ip_pinger.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "ip_pinger")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "ip_pinger.py")
    try:
        response = requests.get(ip_pinger_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded ip_pinger.py")
                else:
                    print("Failed to Download File ip_pinger.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':       
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def b64_download(run_option, return_to_menu=True, download_option=True):
    b64_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/base64/b64.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "base64")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "b64.py")
    try:
        response = requests.get(b64_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded b64.py")
                else:
                    print("Failed to Download File b64.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename]) 
                except Exception as e:
                    print(f"Error >> {e}")    
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()   
                else:
                    return      
    except Exception as e:
        print(f"Error >> {e}")

def username_lookup_download(run_option, return_to_menu=True, download_option=True):
    username_lookup_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/username_lookup/username_lookup.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "username_lookup")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "username_lookup.py")
    try:
        response = requests.get(username_lookup_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded username_lookup.py")
                else:
                    print("Failed to Download username_lookup.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename]) 
                except Exception as e:
                    print(f"Error >> {e}")    
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()   
                else:
                    return      

    except Exception as e:
        print(f"Error >> {e}")
    if return_to_menu:
        input("Press Enter to return...")
        tools_menu()
    else:
        return

def ip_lookup_download(run_option, return_to_menu=True, download_option=True):
    ip_lookup_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/ip_lookup/ip_lookup.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "ip_lookup")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "ip_lookup.py")
    try:
        response = requests.get(ip_lookup_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded ip_lookup.py")
                else:
                    print("Failed to Download File ip_lookup.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def webhook_multitool_download(run_option, return_to_menu=True, download_option=True):
    webhook_multitool_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/webhook_multitool/webhook_multitool.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "webhook_multitool")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "webhook_multitool.py")
    try:
        response = requests.get(webhook_multitool_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded webhook_multitool.py")
                else:
                    print("Failed to Download File webhook_multitool.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    pass
    except Exception as e:
        print(f"Error >> {e}")

def site_delay_tracker_download(run_option, return_to_menu=True, download_option=True):
    url = "https://raw.githubusercontent.com/lockieLocks/Tools/main/site_delay_tracker/site_delay_tracker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "site_delay_tracker")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "site_delay_tracker.py")
    try:
        response = requests.get(url)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded site_delay_tracker.py")
                else:
                    print("Failed to Download site_delay_tracker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def site_redirect_tracker_download(run_option, return_to_menu=True, download_option=True):
    url = "https://raw.githubusercontent.com/lockieLocks/Tools/main/site_redirect_tracker/site_redirect_tracker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "site_redirect_tracker")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "site_redirect_tracker.py")
    try:
        response = requests.get(url)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded site_redirect_tracker.py")
                else:
                    print("Failed to Download site_redirect_tracker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def nitro_gen_download(run_option, return_to_menu=True, download_option=True):
    nitro_gen_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/nitro_generator/nitro_gen.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "nitro_generator")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "nitro_gen.py")
    try:
        response = requests.get(nitro_gen_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded nitro_generator.py")
                else:
                    print("Failed to Download File nitro_gen.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def pwd_strength_checker_download(run_option, return_to_menu=True, download_option=True):
    pwd_strength_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/password_strength_checker.py/pwd_strength_checker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "password_strength_checker.py")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "pwd_strength_checker.py")
    try:
        response = requests.get(pwd_strength_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded pwd_strength_checker.py")
                else:
                    print("Failed to Download pwd_strength_checker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return

    except Exception as e:
        print(f"Error >> {e}")

def token_validator_download(run_option, return_to_menu=True, download_option=True):
    token_validator_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/token_validator/token_validator.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "token_validator")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "token_validator.py")
    file_token = os.path.join(folder_name, "tokens.txt")
    try:
        response = requests.get(token_validator_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded token_validator.py")
                else:
                    print("Failed to Download token_validator.py")
            else:
                print("File Already Exists")
                pass
                if not os.path.exists(file_token):
                    with open(file_token, "w") as t:
                        t.write("put tokens here twin")
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def server_checker_download(run_option, return_to_menu=True, download_option=True):
    server_checker_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/server_checker/server_info_checker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "server_checker")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "server_info_checker.py")
    try:
        response = requests.get(server_checker_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded server_checker.py")
                else:
                    print("Failed to Download server_checker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
        if run_option.lower().strip() == 'y':
            try:
                subprocess.run([sys.executable, filename])
            except Exception as e:
                print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def url_shortener_download(run_option, return_to_menu=True, download_option=True):
    url_shortener_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/url_shortener/url_shortener.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "url_shortener")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "url_shortener.py")
    try:
        response = requests.get(url_shortener_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded url_shortener.py")
                else:
                    print("Failed to Download url_shortener.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
        if run_option.lower().strip() == 'y':
            try:
                subprocess.run([sys.executable, filename])
            except Exception as e:
                print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def token_info_checker_download(run_option, return_to_menu=True, download_option=True):
    token_info_checker_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/token_info_checker/token_info_checker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "token_info_checker")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "token_info_checker.py")
    try:
        response = requests.get(token_info_checker_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded token_info_checker.py")
                else:
                    print("Failed to Download token_info_checker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
        if run_option.lower().strip() == 'y':
            try:
                subprocess.run([sys.executable, filename])
            except Exception as e:
                print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def file_shredder_download(run_option, return_to_menu=True, download_option=True):
    file_shredder_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/file_shredder/file_shredder.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "file_shredder")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "file_shredder.py")
    file_token = os.path.join(folder_name, "shred_list.txt")
    try:
        response = requests.get(file_shredder_link)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded file_shredder.py")
                else:
                    print("Failed to Download file_shredder.py")
            else:
                print("File Already Exists")
                pass
                if not os.path.exists(file_token):
                    with open(file_token, "w") as t:
                        t.write("put file paths here twin")
        else:
            pass
        if not os.path.exists(filename):
            print("\nFile Doesn't Exist...")
            print()
            download_input = input("Would you like to download it now? [Y or N] >> ")
            if download_input.lower().strip() == 'y':
                file_shredder_download(run_option='y', download_option=True)
            else:
                pass
        if run_option.lower().strip() == 'y':
            try:
                subprocess.run([sys.executable, filename])
            except Exception as e:
                print(f"Error >> {e}")
        else:
            if return_to_menu:
                 print("Returning...")
                 time.sleep(0.5)
                 tools_menu()
            else:
                return
    except Exception as e:
        print(f"Error >> {e}")

def roblox_player_count_tracker_download(run_option, return_to_menu=True, download_option=True):
    url = "https://raw.githubusercontent.com/lockieLocks/Tools/main/roblox_player_count_tracker/roblox_player_count_tracker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "roblox_player_count_tracker")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "roblox_player_count_tracker.py")
    try:
        response = requests.get(url)
        if download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded roblox_player_count_tracker.py")
                else:
                    print("Failed to Download roblox_player_count_tracker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
        if run_option.lower().strip() == 'y':
            try:
                subprocess.run([sys.executable, filename])
            except Exception as e:
                print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def get_pc_info():
    number = random.randint(3, 5)
    for i in range(number):
        print(f"\rGetting PC Info{'.' * (i+1)}", end="", flush=True)
        time.sleep(0.5)
    print()
    print(f"\nSystem Info >> {platform.system()}")
    print(f"Machine Info >> {platform.machine()}")
    print(f"Processor Info >> {platform.processor()}")
    print(f"Release Info >> {platform.release()}")
    print(f"Version Info >> {platform.version()}")
    print(f"Platform Info >> {platform.platform()}")
    print(f"Architecture Info >> {platform.architecture()}")
    print(f"Node Info >> {platform.node()}")
    print(f"Processor Info >> {platform.processor()}")
    print(f"Python Version Info >> {platform.python_version()}")
    input("\nPress Enter to return...")


def full_wipe():
    main_dir = os.getcwd()
    for name in os.listdir(main_dir):
        path = os.path.join(main_dir, name)
        if os.path.isdir(path):
            if name.lower() in [".vs", "__pycache__", "main.py", ".git", ".github"]:  
                continue
            shutil.rmtree(path)
            print(f"Deleted All Folders >> {path}")

def full_cleanup(script_name="main.py"):
    github_url = "https://raw.githubusercontent.com/lockieLocks/Multitool/main/main.py"
    temp_script = "_new_main.py"
    batch_file = "_new_file.bat"
    print("Downloading latest version...")
    r = requests.get(github_url)
    if r.status_code == 200:
        full_wipe()
        with open(temp_script, "wb") as f:
            f.write(r.content)
    else:
        print("Failed to download latest version.")
    with open(batch_file, "w") as bf:
        bf.write(f"""
@echo off
move {temp_script} {script_name}
start "" "{sys.executable}" "{script_name}"
del {batch_file}
""")
        print("Restarting script...")
    os.startfile(batch_file)
    sys.exit()

def update():
    main_dir = os.getcwd()
    for name in os.listdir(main_dir):
        path = os.path.join(main_dir, name)
        if os.path.isdir(path):
            if name.lower() in [".vs", "__pycache__", ".git", ".github"]:  
                continue
            shutil.rmtree(path)
            print(f"Deleted All Folders >> {path}")
    print("Redownloading files...")
    time.sleep(0.5)
    install_all()

def install_all():
    ip_lookup_download(run_option='n', return_to_menu=False)
    ip_pinger_download(run_option='n', return_to_menu=False)
    b64_download(run_option='n', return_to_menu=False)
    username_lookup_download(run_option='n', return_to_menu=False)
    webhook_multitool_download(run_option='n', return_to_menu=False)
    site_delay_tracker_download(run_option='n', return_to_menu=False)
    pwd_strength_checker_download(run_option='n', return_to_menu=False)
    nitro_gen_download(run_option='n', return_to_menu=False)
    token_validator_download(run_option='n', return_to_menu=False)
    server_checker_download(run_option='n', return_to_menu=False)
    url_shortener_download(run_option='n', return_to_menu=False)
    token_info_checker_download(run_option='n', return_to_menu=False)
    file_shredder_download(run_option='n', return_to_menu=False)
    roblox_player_count_tracker_download(run_option='n', return_to_menu=False)
    site_redirect_tracker_download(run_option='n', return_to_menu=False)
    input("\nPress Enter to return...")
    tools_menu()

def tools_ascii():
    ascii_art = f""" {Fore.RED}                                                                                                                                   
                                 ,;L.                                                        t#,         t#,                           .
                               f#i EW:        ,ft t           .    .                        ;##W.       ;##W.             i           ;W
                             .E#t  E##;       t#E Ej GEEEEEEELDi   Dt           GEEEEEEEL  :#L:WE      :#L:WE            LE          f#E
       ,##############Wf.   i#W,   E###t      t#E E#,,;;L#K;;.E#i  E#i          ,;;L#K;;. .KG  ,#D    .KG  ,#D          L#E        .E#f 
        ........jW##Wt     L#D.    E#fE#f     t#E E#t   t#E   E#t  E#t             t#E    EE    ;#f   EE    ;#f        G#W.       iWW;  
              tW##Kt     :K#Wfff;  E#t D#G    t#E E#t   t#E   E#t  E#t             t#E   f#.     t#i f#.     t#i      D#K.       L##Lffi
            tW##E;       i##WLLLLt E#t  f#E.  t#E E#t   t#E   E########f.          t#E   :#G     GK  :#G     GK      E#K.       tLLG##L 
          tW##E;          .E#L     E#t   t#K: t#E E#t   t#E   E#j..K#j...          t#E    ;#L   LW.   ;#L   LW.    .E#E.          ,W#i  
       .fW##D,              f#E:   E#t    ;#W,t#E E#t   t#E   E#t  E#t             t#E     t#f f#:     t#f f#:    .K#E           j#E.   
     .f###D,                 ,WW;  E#t     :K#D#E E#t   t#E   E#t  E#t             t#E      f#D#;       f#D#;    .K#D          .D#j     
   .f####Gfffffffffff;        .D#; E#t      .E##E E#t   t#E   f#t  f#t             t#E       G#t         G#t    .W#G          ,WK,      
  .fLLLLLLLLLLLLLLLLLi          tt ..         G#E E#t    fE    ii   ii              fE        t           t    :W##########Wt EG.       
                                               fE ,;.     :                          :                         :,,,,,,,,,,,,,.,         
{Fore.LIGHTWHITE_EX}==================================================================================================================================================={Fore.RED}
                               {Fore.LIGHTWHITE_EX}||{Fore.RED}    Press {Fore.LIGHTWHITE_EX}b{Fore.RED} to return to main menu           {Fore.LIGHTWHITE_EX}||{Fore.RED}
                               {Fore.LIGHTWHITE_EX}||{Fore.RED}    Press {Fore.LIGHTWHITE_EX}99{Fore.RED} to Install and Update all tools {Fore.LIGHTWHITE_EX}||{Fore.RED}
                               {Fore.LIGHTWHITE_EX}||{Fore.RED}    Press {Fore.LIGHTWHITE_EX}404{Fore.RED} to Exit                        {Fore.LIGHTWHITE_EX}||{Fore.RED}
                 {Fore.LIGHTWHITE_EX}==============||_____________________________________________||======================={Fore.RED}   
                 {Fore.LIGHTWHITE_EX}||{Fore.RED}            Step 1{Fore.LIGHTWHITE_EX}:{Fore.RED}                   {Fore.LIGHTWHITE_EX}||{Fore.RED}                Step 2{Fore.LIGHTWHITE_EX}:{Fore.RED}                   {Fore.LIGHTWHITE_EX}||{Fore.RED}
                 {Fore.LIGHTWHITE_EX}||{Fore.RED}     {Fore.YELLOW}Star{Fore.RED} The Tool in Github          {Fore.LIGHTWHITE_EX}||{Fore.RED}     Press {Fore.LIGHTWHITE_EX}!{Fore.RED} to Join the {Fore.BLUE}Discord{Fore.RED} Server   {Fore.LIGHTWHITE_EX}||{Fore.RED}
                 ========================================{Fore.LIGHTWHITE_EX}||{Fore.RED}============================================
                 {Fore.LIGHTWHITE_EX}||{Fore.RED}            Step 3:                   {Fore.LIGHTWHITE_EX}||{Fore.RED}                Step 4{Fore.LIGHTWHITE_EX}:{Fore.RED}                   {Fore.LIGHTWHITE_EX}||{Fore.RED}
                 {Fore.LIGHTWHITE_EX}||{Fore.RED}     Press {Fore.LIGHTWHITE_EX}S{Fore.RED} to run the Setup         {Fore.LIGHTWHITE_EX}||{Fore.RED}             Enjoy Yourself               {Fore.LIGHTWHITE_EX}||{Fore.RED}
                 {Fore.LIGHTWHITE_EX}||{Fore.RED}                                      {Fore.LIGHTWHITE_EX}||{Fore.RED}                                          {Fore.LIGHTWHITE_EX}||{Fore.RED}
        {Fore.LIGHTWHITE_EX}[{Fore.RED}------Network Tools------{Fore.LIGHTWHITE_EX}]{Fore.RED}          {Fore.LIGHTWHITE_EX}[{Fore.RED}------Utility Tools------{Fore.LIGHTWHITE_EX}]{Fore.RED}           {Fore.LIGHTWHITE_EX}[{Fore.RED}------Discord Tools------{Fore.LIGHTWHITE_EX}]{Fore.RED}
            {Fore.LIGHTWHITE_EX}[{Fore.RED}1{Fore.LIGHTWHITE_EX}]{Fore.RED} - Grab Your Own IP              {Fore.LIGHTWHITE_EX}[{Fore.RED}7{Fore.LIGHTWHITE_EX}]{Fore.RED} - B64 Tools                      {Fore.LIGHTWHITE_EX}[{Fore.RED}13{Fore.LIGHTWHITE_EX}]{Fore.RED} - Webhook Multitool
            {Fore.LIGHTWHITE_EX}[{Fore.RED}2{Fore.LIGHTWHITE_EX}]{Fore.RED} - IP Lookup                     {Fore.LIGHTWHITE_EX}[{Fore.RED}8{Fore.LIGHTWHITE_EX}]{Fore.RED} - Username Lookup                {Fore.LIGHTWHITE_EX}[{Fore.RED}14{Fore.LIGHTWHITE_EX}]{Fore.RED} - Token Validator
            {Fore.LIGHTWHITE_EX}[{Fore.RED}3{Fore.LIGHTWHITE_EX}]{Fore.RED} - IP Pinger                     {Fore.LIGHTWHITE_EX}[{Fore.RED}9{Fore.LIGHTWHITE_EX}]{Fore.RED} - Password Strength Checker      {Fore.LIGHTWHITE_EX}[{Fore.RED}15{Fore.LIGHTWHITE_EX}]{Fore.RED} - Nitro Generator
            {Fore.LIGHTWHITE_EX}[{Fore.RED}4{Fore.LIGHTWHITE_EX}]{Fore.RED} - Site Delay Tracker            {Fore.LIGHTWHITE_EX}[{Fore.RED}10{Fore.LIGHTWHITE_EX}]{Fore.RED} - URL Shortener                 {Fore.LIGHTWHITE_EX}[{Fore.RED}16{Fore.LIGHTWHITE_EX}]{Fore.RED} - Server Info Checker
            {Fore.LIGHTWHITE_EX}[{Fore.RED}5{Fore.LIGHTWHITE_EX}]{Fore.RED} - Site Redirect Checker         {Fore.LIGHTWHITE_EX}[{Fore.RED}11{Fore.LIGHTWHITE_EX}]{Fore.RED} - File Shredder                 {Fore.LIGHTWHITE_EX}[{Fore.RED}17{Fore.LIGHTWHITE_EX}]{Fore.RED} - Token Info Checker
            {Fore.LIGHTWHITE_EX}[{Fore.RED}6{Fore.LIGHTWHITE_EX}]{Fore.RED} - Roblox Player Tracker         {Fore.LIGHTWHITE_EX}[{Fore.RED}12{Fore.LIGHTWHITE_EX}]{Fore.RED} - Get Your PC Info
"""
    print(ascii_art)

def tools_menu():
    clear()
    tools_ascii()
    raw_option = input("Option >> ")
    option = raw_option.lower().strip()
    if option == '1':
        get_all_ips()

    elif option == '2':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        ip_lookup_download(run_option, download_option=False)

    elif option == '3':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        ip_pinger_download(run_option, download_option=False)

    elif option == '4':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        site_delay_tracker_download(run_option, download_option=False)

    elif option == '5':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        site_redirect_tracker_download(run_option, download_option=False)

    elif option == '6':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        roblox_player_count_tracker_download(run_option, download_option=False)

    elif option == '7':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        username_lookup_download(run_option, download_option=False)

    elif option == '8':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        url_shortener_download(run_option, download_option=False)

    elif option == '9':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        file_shredder_download(run_option, download_option=False)

    elif option == '10':
        get_pc_info()
        tools_menu()

    elif option == '11':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        webhook_multitool_download(run_option, download_option=False)

    elif option == '12':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        token_validator_download(run_option, download_option=False)

    elif option == '13':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        nitro_gen_download(run_option, download_option=False)

    elif option == '14':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        server_checker_download(run_option, download_option=False)

    elif option == '15':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        token_info_checker_download(run_option, download_option=False)

    elif option == '99':
        update()

    elif option == 'b':
        print("Taking you to main menu...")
        time.sleep(0.5)
        main()

    else:
        print("Invalid Input...")
        time.sleep(0.5)
        tools_menu()

def main_ascii():
    ascii_art = f"""  {Fore.LIGHTMAGENTA_EX}
    
        888 888b    | ,d88~~\ ~~~888~~~      e      888     888     888~~  888~-_              e    e      888~~  888b    | 888   | 
        888 |Y88b   | 8888       888        d8b     888     888     888___ 888   \            d8b  d8b     888___ |Y88b   | 888   | 
        888 | Y88b  | `Y88b      888       /Y88b    888     888     888    888    |          d888bdY88b    888    | Y88b  | 888   | 
        888 |  Y88b |  `Y88b,    888      /  Y88b   888     888     888    888   /          / Y88Y Y888b   888    |  Y88b | 888   | 
        888 |   Y88b|    8888    888     /____Y88b  888     888     888    888_-~          /   YY   Y888b  888    |   Y88b| Y88   | 
        888 |    Y888 \__88P'    888    /      Y88b 888____ 888____ 888___ 888 ~-_        /          Y888b 888___ |    Y888  "8__/  
                                                __  _      ___ ___    
                                                 / |_ |\ |  |   | |_| 
                                                /_ |_ | \| _|_  | | |  
{Fore.LIGHTWHITE_EX}----------------------------------------------------------------------------------------------------------------------------------------{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}                                                     {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}   {Fore.LIGHTWHITE_EX}3:<{Fore.LIGHTMAGENTA_EX} Welcome to MAIN MENU of Lockie's multitool {Fore.LIGHTWHITE_EX}>:3{Fore.LIGHTMAGENTA_EX}{Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}         {Fore.LIGHTWHITE_EX}404{Fore.LIGHTMAGENTA_EX} - FULL WIPE AND REINSTALL               {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}          {Fore.LIGHTWHITE_EX}100{Fore.LIGHTMAGENTA_EX} - INSTALL and UPDATE ALL Tools         {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}         {Fore.LIGHTWHITE_EX}T{Fore.LIGHTMAGENTA_EX}  - ALL Tools Runner")                     {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                -------------------------------------------------------
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}         {Fore.LIGHTWHITE_EX}D{Fore.LIGHTMAGENTA_EX} - Discord Tools runner                    {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}         {Fore.LIGHTWHITE_EX}N{Fore.LIGHTMAGENTA_EX} - Network Tools runner                    {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}         {Fore.LIGHTWHITE_EX}U{Fore.LIGHTMAGENTA_EX} - Utility Tools runner                    {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}                 Have Fun :3                         {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}
                                {Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}_____________________________________________________{Fore.LIGHTWHITE_EX}||{Fore.LIGHTMAGENTA_EX}"""
    print(ascii_art)

def main():
    while True:
        clear()
        main_ascii()
        print(f"\n{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}1{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} - Install Discord Tools = Webhook spammer, Token Validator, Nitro Generator, Server Info Checker, Token Info Checker")
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}2{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} - Install Network Tools = IP Lookup, IP Pinger, Site Multitool")
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}3{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} - Install Utility Tools = Username lookup, B64 multitool, Pwd Strength Checker, Url Shortener, File Shredder")
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}4{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} - Install All tools = All of above")
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}99{Fore.LIGHTWHITE_EX}]{Fore.LIGHTMAGENTA_EX} - Exit")
        raw_option = input("Option >> ")
        option = raw_option.lower().strip()
        if option == '1':
            token_validator_download(run_option='n', return_to_menu=False)
            webhook_multitool_download(run_option='n', return_to_menu=False)
            nitro_gen_download(run_option='n', return_to_menu=False)
            server_checker_download(run_option='n', return_to_menu=False)
            token_info_checker_download(run_option='n', return_to_menu=False)
            input("Press Enter to return...")
            main()

        elif option == '2':
            ip_lookup_download(run_option='n', return_to_menu=False)
            ip_pinger_download(run_option='n', return_to_menu=False)
            site_delay_tracker_download(run_option='n', return_to_menu=False)
            input("Press Enter to return...")
            main()

        elif option == '3':
            username_lookup_download(run_option='n', return_to_menu=False)
            b64_download(run_option='n', return_to_menu=False)
            pwd_strength_checker_download(run_option='n', return_to_menu=False)
            url_shortener_download(run_option='n', return_to_menu=False)
            file_shredder_download(run_option='n', return_to_menu=False)
            input("Press Enter to return...")
            main()

        elif option == '4':
            install_all()

        elif option.lower().strip() == 't':
            tools_menu()

        elif option.lower().strip() == 'd':
            discord_tools_main()

        elif option.lower().strip() == 'u':
            utility_tools_main()

        elif option.lower().strip() == 'n':
            network_main()

        elif option == '100':
            update()

        elif option == '404':
            full_cleanup()

        elif option == '99':
            print("Peace Out gng...")
            time.sleep(0.5)
            sys.exit()

        else:
            print("Returning")
            time.sleep(0.5)
            main()

def utility_ascii():
    ascii_art = f""" {Fore.LIGHTRED_EX}
  _    _ _   _ _ _ _           _______          _     
 | |  | | | (_) (_) |         |__   __|        | |    
 | |  | | |_ _| |_| |_ _   _     | | ___   ___ | |___ 
 | |  | | __| | | | __| | | |    | |/ _ \ / _ \| / __|
 | |__| | |_| | | | |_| |_| |    | | (_) | (_) | \__ |
  \____/ \__|_|_|_|\__|\__, |    |_|\___/ \___/|_|___/
                        __/ |                         
                       |___/                          
                {Fore.LIGHTWHITE_EX}b{Fore.LIGHTRED_EX} - Return to main menu
"""
    print(ascii_art)

def utility_tools_main():
    clear()
    utility_ascii()
    print(f"                 {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} - Run Username Lookup")
    print(f"                 {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} - Run B64 Multitool")
    print(f"                 {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} - Run Password Strength Checker")
    print(f"                 {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} - Run File Shredder")
    print(f"                 {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}5{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} - Run Url Shortener")
    print(f"                 {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}6{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} - Get Your PC Info")
    raw_option = input("Option >> ")
    option = raw_option.lower().strip()
    if option == '1':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        username_lookup_download(run_option, download_option=False)

    elif option == '2':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        b64_download(run_option, download_option=False)

    elif option == '3':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        pwd_strength_checker_download(run_option, download_option=False)

    elif option == '4':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        file_shredder_download(run_option, download_option=False)

    elif option == '5':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        url_shortener_download(run_option, download_option=False)

    elif option == '6':
        get_pc_info()
        utility_tools_main()

    elif option == 'b':
        print("Taking you to main menu...")
        time.sleep(0.5)
        main()

    else:
        print("Invalid...")
        time.sleep(0.5)
        utility_tools_main()


def network_ascii():
    ascii_art = f""" {Fore.LIGHTBLUE_EX}

$$\   $$\            $$\                                       $$\             $$$$$$$$\                  $$\           
$$$\  $$ |           $$ |                                      $$ |            \__$$  __|                 $$ |          
$$$$\ $$ | $$$$$$\ $$$$$$\   $$\  $$\  $$\  $$$$$$\   $$$$$$\  $$ |  $$\          $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
$$ $$\$$ |$$  __$$\\_$$  _|  $$ | $$ | $$ |$$  __$$\ $$  __$$\ $$ | $$  |         $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
$$ \$$$$ |$$$$$$$$ | $$ |    $$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$$$$$  /          $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
$$ |\$$$ |$$   ____| $$ |$$\ $$ | $$ | $$ |$$ |  $$ |$$ |      $$  _$$<           $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
$$ | \$$ |\$$$$$$$\  \$$$$  |\$$$$$\$$$$  |\$$$$$$  |$$ |      $$ | \$$\          $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
\__|  \__| \_______|  \____/  \_____\____/  \______/ \__|      \__|  \__|         \__| \______/  \______/ \__|\_______/ 
                                                                                                                        
                                                                                                                        
                                                {Fore.LIGHTWHITE_EX}b{Fore.LIGHTBLUE_EX} - Return To Main Menu"""
    print(ascii_art)

def network_main():
    clear()
    network_ascii()
    print(f"                                     {Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}1{Fore.LIGHTWHITE_EX}]{Fore.LIGHTBLUE_EX} - Grap Your own IPs")
    print(f"                                     {Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}2{Fore.LIGHTWHITE_EX}]{Fore.LIGHTBLUE_EX} - Run IP Lookup")
    print(f"                                     {Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}3{Fore.LIGHTWHITE_EX}]{Fore.LIGHTBLUE_EX} - Run IP Pinger")
    print(f"                                     {Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}4{Fore.LIGHTWHITE_EX}]{Fore.LIGHTBLUE_EX} - Run Site Multitool")
    raw_option = input("Option >> ")
    option = raw_option.lower().strip()
    if option == '1':
        get_all_ips()
        input("Press Enter to return...")
        network_main()

    elif option == '2':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        ip_lookup_download(run_option, download_option=False)

    elif option == '3':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        ip_pinger_download(run_option, download_option=False)

    elif option == '4':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        site_delay_tracker_download(run_option, download_option=False)

    elif option == 'b':
        print("Taking you to main menu...")
        time.sleep(0.5)

    else:
        print("Invalid...")
        time.sleep(0.5)
        network_main()

def discord_ascii():
    discord_ascii_art = f""" {Fore.MAGENTA}
    
 *******   **                                      **       **********                    **        
/**////** //                                      /**      /////**///                    /**        
/**    /** **  ******  *****   ******  ******     /**          /**      ******   ******  /**  ******
/**    /**/** **////  **///** **////**//**//*  ******          /**     **////** **////** /** **//// 
/**    /**/**//***** /**  // /**   /** /** /  **///**          /**    /**   /**/**   /** /**//***** 
/**    ** /** /////**/**   **/**   /** /**   /**  /**          /**    /**   /**/**   /** /** /////**
/*******  /** ****** //***** //****** /***   //******          /**    //****** //******  *** ****** 
///////   // //////   /////   //////  ///     //////           //      //////   //////  /// //////  
                                        {Fore.LIGHTWHITE_EX}b{Fore.MAGENTA} - Return to main menu"""
    print(discord_ascii_art)

def discord_tools_main():
    clear()
    discord_ascii()
    print(f"                        {Fore.LIGHTWHITE_EX}[{Fore.MAGENTA}1{Fore.LIGHTWHITE_EX}[{Fore.MAGENTA} - Run Webhook Multitool")
    print(f"                        {Fore.LIGHTWHITE_EX}[{Fore.MAGENTA}2{Fore.LIGHTWHITE_EX}]{Fore.MAGENTA} - Run Token Validator")
    print(f"                        {Fore.LIGHTWHITE_EX}[{Fore.MAGENTA}3{Fore.LIGHTWHITE_EX}]{Fore.MAGENTA} - Run Nitro Generator")
    print(f"                        {Fore.LIGHTWHITE_EX}[{Fore.MAGENTA}4{Fore.LIGHTWHITE_EX}]{Fore.MAGENTA} - Run Server Info Checker")
    print(f"                        {Fore.LIGHTWHITE_EX}[{Fore.MAGENTA}5{Fore.LIGHTWHITE_EX}]{Fore.MAGENTA} - Run Token Info Checker")
    raw_option = input("Option >> ")
    option = raw_option.lower().strip()
    if option == '1':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        webhook_multitool_download(run_option, download_option=False, return_to_menu=False)

    elif option == '2':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        token_validator_download(run_option, download_option=False, return_to_menu=False)

    elif option == '3':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        nitro_gen_download(run_option, download_option=False, return_to_menu=False)

    elif option == '4':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        server_checker_download(run_option, download_option=False, return_to_menu=False)

    elif option == '5':
        run_raw = input("You wanna run the tool? [Y or N] >> ")
        run_option = run_raw.lower().strip()
        token_info_checker_download(run_option, download_option=False, return_to_menu=False)

    elif option.strip() == 'b':
        print("Taking you to main menu...")
        time.sleep(0.5)

    else:
        print("Invalid...")
        time.sleep(0.5)
        discord_tools_main()

main()
