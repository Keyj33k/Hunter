#!/usr/bin/env python3

try:
    from termcolor import colored as cld
    import urllib3
    from time import sleep
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"


class RemoteServerStatusCode:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def get_code(self):
        while True:
            try:
                send_request = urllib3.PoolManager().request("GET", self.uniformresourcelocator)
                print(f"\n{w}Result:\n{r}{'=' * 70}\n"
                      f"{w}[{g}+{w}] {self.uniformresourcelocator} status code {r}->{w} {send_request.status}")
                input(f"{r}{'=' * 70}\n{chr(0xa)}\n{w}[{r}*{w}] Press enter key to continue")
                break
            except KeyboardInterrupt:
                print(f"\n{w}[{r}*{w}] You pressed Ctrl+C{r}.{w} Exit{r}.")
                break
            except Exception as excerr:
                print(cld(str(excerr), "red"))
                break
