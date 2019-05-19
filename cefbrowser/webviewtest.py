from cefpython3 import cefpython as cef
import platform
import sys
from configparser import ConfigParser


def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()

    conf = ConfigParser()
    conf.read("config.ini",'utf-8')
    siteUrl = conf.get("main","url");
    title = conf.get("main","title");
    print(siteUrl)
    print(title)
    cef.CreateBrowserSync(url=siteUrl,
                          window_title=title)
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"


if __name__ == '__main__':
    main()