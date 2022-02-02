import time, keyboard, os, sys
import win32gui, win32con
from pygame import mixer

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,300,500,0)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def main():
    mixer.init()
    mixer.music.load('sounds.mp3')

    def mainMenu():
        os.system('cls')
        print('+============================+')
        print('|         Main Menu          |')
        print('+============================+')
        print('| 1) Start                   |')
        print('| 0) Exit                    |')
        print('+============================+')
        inpt = input('Input number : ')
        if inpt == '1':
            time.sleep(0)
        elif inpt == '0':
            exit(0)
        else:
            print('\n')
            print('Wront Input !...')
            time.sleep(2)
            sys.stdout.flush()
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    mainMenu()

    def firstStep():
        os.system('cls')
        print('+============================+')
        print('|        First Steps         |')
        print('+============================+')
        try:
            loopInput = input('[+] How much you want loop : ')  
            firstStep.loopInput = int(loopInput)
            firstStep.loopSys = 0
            delays = input('[+] add delay seconds : ')
            firstStep.delays = int(delays)
        except KeyboardInterrupt:
            print('\n')
            print('Wront Input !...')
            time.sleep(2)
            sys.stdout.flush()
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    firstStep()

    def options():
        os.system('cls')
        print('+========================+')
        print('| Options                |')
        print('+========================+')
        print('| 1) Turn off after done |')
        print('| 2) Keep MyPC alive     |')
        print('| 0) Exit                |')
        print('+========================+')
        try:
            options.option = input('Input number : ')
            if options.option == '0':
                sys.stdout.flush()
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        except KeyboardInterrupt:
            print('\n')
            print('Wront Input !...')
            time.sleep(2)
            sys.stdout.flush()
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    options()

    def endWithShutdownD(delay, loop):
        time.sleep(delay)
        print('+========================+')
        print('[!] Finished with : ', loop, 'Loop')
        os.system("shutdown /s /t 1")
    
    def endWithShutdownND(loop):
        print('+========================+')
        print('[!] Finished with : ', loop, 'Loop')
        os.system("shutdown /s /t 1")

    def endNoShutdownD(delay, loop):
        time.sleep(delay)
        print('+========================+')
        print('[!] Finished with : ', loop, 'Loop')
        mixer.music.play()
        input('Press ENTER to stop...')
        mixer.music.stop()
        x = input('Do you want exit[y/n]: ')
        if x == 'y':
            exit(0)
        else:
            sys.stdout.flush()
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    
    def endNoShutdownND(loop):
        print('+========================+')
        print('[!] Finished with : ', loop, 'Loop')
        mixer.music.play()
        input('Press ENTER to stop...')
        mixer.music.stop()
        x = input('Do you want exit[y/n]: ')
        if x == 'y':
            exit(0)
        else:
            sys.stdout.flush()
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

    def firstProcess():
        os.system('cls')
        print('+========================+')
        print('|        Running         |')
        print('+========================+')
        print('[!] Loop :',firstStep.loopInput,'Loop')
        print('[!] Delay :',firstStep.delays,'Seconds')
        print('+========================+')
        try:
            time.sleep(2)
            print('[System] : First Click..')
            keyboard.press_and_release('end')
        except KeyboardInterrupt:
            endNoShutdownND(firstStep.loopSys)
    firstProcess()

    while True:
        if firstStep.loopSys == firstStep.loopInput:
            if options.option == '1':
                try:
                    endWithShutdownD(firstStep.delays, firstStep.loopSys)
                except KeyboardInterrupt:
                    endWithShutdownND(firstStep.loopSys)
            elif options.option == '2':
                try:
                    endNoShutdownD(firstStep.delays, firstStep.loopSys)
                except KeyboardInterrupt:
                    endNoShutdownND(firstStep.loopSys)
            else:
                try:
                    endNoShutdownD(firstStep.delays, firstStep.loopSys)
                except KeyboardInterrupt:
                    endNoShutdownND(firstStep.loopSys)
        try:  
            time.sleep(firstStep.delays)
            firstStep.loopSys+=1
            keyboard.press_and_release('end')
            print('[',firstStep.loopSys,']',"Re-Click...")
        except KeyboardInterrupt:
            endNoShutdownND(firstStep.loopSys)

if __name__ == '__main__':
    main()
