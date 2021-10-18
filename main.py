from shutil import which
from tkinter import *
import subprocess

# import messagebox from tkinter module
import tkinter.messagebox

# create a tkinter root window
root = tkinter.Tk()

# root window title and dimension
root.title("Software Check")
root.geometry('400x100')


def onClick():

    if which("docker"):
        docker_install = "✔ SUCCESS"
    else:
        docker_install = "❌ NOT INSTALLED!!!"
    if which("wsl"):
        ret = subprocess.run(["wsl", "test", "-f", "/etc/os-release"])
        if ret.returncode != 0:
            wsl_install = "❌ NOT INSTALLED!!!"
        else:
            wsl_install = "✔ SUCCESS"
    else:
        wsl_install = "❌ NOT INSTALLED!!!"
    # ubuntu check
    check_ubuntu = subprocess.Popen(["powershell.exe", ".\check_ubuntu.ps1"], stdout=subprocess.PIPE,
                                    stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    check_ubuntu = check_ubuntu.stdout.read().decode("utf-8")
    check_ubuntu = check_ubuntu.strip()
    if check_ubuntu == "INSTALLED":
        ubuntu_install = "✔ SUCCESS"
    else:
        ubuntu_install = "❌ NOT INSTALLED!!!"
    message = ["Docker: " + docker_install, "Wsl: " + wsl_install, "Ubuntu: " + ubuntu_install]
    tkinter.messagebox.showinfo("Results", "\n".join(message))


if __name__ == '__main__':
    l = Label(root, text="Active Buildings Software Dependency \n" "Installation Check.", font=("Arial", 15))
    l.pack()
    # Create a Button
    button = Button(root, text="Check", command=onClick, height=2, width=12)

    # Set the position of button on the top of window.
    button.pack(side='bottom')
    root.mainloop()

