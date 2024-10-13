from colorama import Fore
import colorama
import sounddevice as sd
import soundfile as sf


def startup():
    startup = 'startup.wav'
    # Extract data and sampling rate from file
    dataST, fsST = sf.read(startup, dtype='float32')
    sd.play(dataST, fsST)
    sd.wait()

    colorama.init(autoreset=True)



print(Fore.CYAN +
    """
    _____                                                                                                                  _____ 
   ( ___ )                                                                                                                ( ___ )
    |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
    |   |                                                                                                                  |   | 
    |   |                                                                                                                  |   | 
    |   |                                                                                                                  |   | 
    |   |       _____      _      _____   ____      __  __   _       _____   ____       _      ____    _____   ____        |   | 
    |   |      | ____|    / \    |_   _| / ___|    |  \/  | | |     |_   _| |  _ \     / \    |  _ \  | ____| |  _ \       |   | 
    |   |      |  _|     / _ \     | |   \___ \    | |\/| | | |       | |   | |_) |   / _ \   | | | | |  _|   | |_) |      |   | 
    |   |      | |___   / ___ \    | |    ___) |   | |  | | | |___    | |   |  _ <   / ___ \  | |_| | | |___  |  _ <       |   | 
    |   |      |_____| /_/   \_\   |_|   |____/    |_|  |_| |_____|   |_|   |_| \_\ /_/   \_\ |____/  |_____| |_| \_\      |   | 
    |   |                                                                                                                  |   | 
    |   |                                         _____       ____         ___                                             |   | 
    |   |                            __   __     |___ /      |___ \       / _ \                                            |   | 
    |   |                            \ \ / /       |_ \        __) |     | (_) |                                           |   | 
    |   |                             \ V /   _   ___) |  _   / __/   _   \__, |                                           |   | 
    |   |                              \_/   (_) |____/  (_) |_____| (_)    /_/                                            |   | 
    |   |                                                                                                                  |   | 
    |   |                                                                                                                  |   | 
    |   |                                                                                                                  |   | 
    |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
   (_____)                                                                                                                (_____)
    
    """) 