import requests
import sys
from time import sleep
import colorama
import cfonts

colorama.init()
print(cfonts.render("admin panel finder" , colors=['red' , 'yellow']))
print(colorama.Fore.GREEN+"github.com/mazdakpak/admin-panel-finder 💻")
def main():
    print(colorama.Fore.YELLOW+" ⚠️ Warning: Enter your target address such http://example.com  ⚠️")
    url = input("🔗 Enter your taget url :")
    start = colorama.Fore.GREEN+"Start Scaning ... \n"
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        sleep(0.1)
    file = open("admin_panels.txt" , "r")
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print(colorama.Fore.RED+"*"* 15)
                print(colorama.Fore.GREEN+"Admin panel found ✔️ ==> {}".format(curl))
                print(colorama.Fore.RED+"*" * 15)
            else:
                print(colorama.Fore.RED+"Not found ❌ ==> {}".format(curl))

    except KeyboardInterrupt:
        print("\033[91m Shutdown Request! \033[0m")
    except Exception as ex:
        print(str(ex))
    file.close()


if __name__ == "__main__":
    main()
