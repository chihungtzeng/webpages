# -*- coding: utf-8 -*-
import logging
import signal
import os
import sys
from gi.repository import Gtk, WebKit2


def __init_webview():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    uri = "file://{}".format(os.path.join(cur_dir, "countdown.html"))
    webview = WebKit2.WebView()
    logging.info("load %s", uri)
    webview.load_uri(uri)
    return webview


def __init_window():
    window = Gtk.Window()
    window.connect("destroy", lambda window: Gtk.main_quit())

    webview = __init_webview()
    window.add(webview)
    window.set_keep_above(True)
    window.stick()
    return window


def main():
    """
    Program entry.
    """
    window = __init_window()
    window.show_all()
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # make ctrl+c work
    Gtk.main()


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)-15s %(message)s",
                        level=logging.INFO)
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
