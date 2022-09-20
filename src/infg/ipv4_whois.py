#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    from requests import post
    import os
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


class IPv4Lookup:
    def __init__(self, ipv4_address: str):
        self.ipv4_address = ipv4_address

    def main(self):
        while True:
            if self.ipv4_address == 'x' or self.ipv4_address == 'exit':
                break

            time_start = dtt.now()
            print(f"\n{w}[{r}*{w}] Results{r}:")

            try:
                response = post("http://ip-api.com/batch", json=[{"query": self.ipv4_address}]).json()
                print("=" * 70)

                for lookup in response:
                    for k, j in lookup.items():
                        print(f"{w}[{g}+{w}] " + k, j)

                time_stop = dtt.now()
                time_result = time_stop - time_start
                print(f"{r}=" * 70)
                print(f"{w}[{r}*{w}] Scanner done in {time_result}!")
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except Exception as error:
                print(cld(str(error), "red"))
                input(f"{w}[{g}+{w}] Press enter key to continue")
                break
