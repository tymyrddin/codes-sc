import ctypes
import platform


def is_admin():
    if platform.system() == "Windows":
        return ctypes.windll.shell32.IsUserAnAdmin()
    else:
        return 1


print(is_admin())
