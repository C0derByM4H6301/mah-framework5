from rich.console import Console
import os
import sys
import rich
from colorama import Fore, init
init(autoreset=True)



class ozel_print:
	def bilgi(text):
		print(f"[{Fore.BLUE}i{Fore.RESET}] "+text)

	def statu(text):
		print(f"[{Fore.LIGHTGREEN_EX}s{Fore.RESET}] "+text)

	def hata(text):
		print(f"[{Fore.RED}e{Fore.RESET}] "+text)

	def basarili(text):
		print(f"[{Fore.GREEN}+{Fore.RESET}] "+text)

	def basarisiz(text):
		print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] "+text)

	def yaz(text):
		print(f"[{Fore.CYAN}*{Fore.RESET}] "+text)
