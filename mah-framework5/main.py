import rich
from rich import print as rich_print
from lib.module import * #local kütüphane 1
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.formatted_text import HTML
from rich.traceback import install
install()
import os
import platform
from lib.db import * #local kütüphane 2
from asciistuff import Banner, Lolcat
from prompt_toolkit.history import FileHistory, History
from rich.table import Table
from lib.console_func import * # ozel_print, 

history_file = '.mah_framework5_history'
historyim = FileHistory(history_file)


modules = set()
for i in listModule():
	modules.add("modules/"+i)
completer = NestedCompleter.from_nested_dict({
	"search":None,
	"exit":None,
	"show":{"modules","info"}, #options belki gelebilir
	"use":modules,
	"info":modules,
	"clear":None,
	"exec":set(os.listdir("/usr/bin/")),
	"help":{"search","exit","help","show","use","info","clear","exec","banner"},
	"banner":None,

})

def use_prompt(module):
	completerim = NestedCompleter.from_nested_dict({
		"back":None,
		"show":{"info","options"},
		"set":set(get_module_options(module).keys()),
		"help":{"help","back","show","set","run"},
		"run":None
		})
	history_file = '.mah_framework5_module_history'
	history2 = FileHistory(history_file)
	my_option = get_module_options(module)
	while True:
		promptum = prompt(HTML(f"mah (<ansired>{module}</ansired>) > "), completer=completerim, history=history2)
		ate = promptum.split()
		if len(ate)>0:
			if ate[0] == "back":
				break
			if ate[0] == "show":
				if len(ate) > 1:
					if ate[1] == "info":
						ozel_print.bilgi("info:\n"+get_module_info(module))
					if ate[1] == "options":
						table = Table(title="Opsiyonlar Tablosu", header_style="bold blue")
						table.add_column("Opsiyon", style="cyan")
						table.add_column("Açıklama")
						table.add_column("Değer", style="magenta")
						for i in my_option.keys():
							table.add_row(i,my_option[i][0],my_option[i][1])
						rich_print(table)
					else:
						ozel_print.hata("Paramere belirtin. options - info")
				else:
					ozel_print.yaz("Örnek kullanım:\n show info - show options")
					ozel_print.yaz("Lütfen komutu böyle kullanın.")

			if ate[0] == "set":
				if len(ate) > 1:
					if ate[1] in my_option.keys():
						if len(ate) > 2:
							my_option[ate[1]][1] = ate[2]
							ozel_print.bilgi(ate[1] + " => "+ate[2])
						else:
							ozel_print.basarisiz("Bir değer giriniz.")
					else:
						ozel_print.hata("Opsiyon bulunamadı")
						ozel_print.bilgi("Örnek kullanım:\nset option value")
			if ate[0] == "run":
				runny = get_module_run(module)
				runny(my_option)
			if ate[0] == "help":
				if len(ate) > 1:
					table = Table(title="Komut Tablosu", header_style="bold blue")
					table.add_column("Komut", style="cyan")
					table.add_column("Açıklama", style="green")
					if ate[1] == "help":
						table.add_row("help", "Yardım komutu, komutların dökümansıyonunu sağlar")
						rich_print(table)
					if ate[1] == "back":
						table.add_row("back", "Modülü kullandığın promptu sonlandırıp ana prompta geçmeni sağlar")
						rich_print(table)
					if ate[1] == "run":
						table.add_row("run", "Modülü çalıştırır. (Modülün options verisini run fonksiyona vererek çalıştırır)")
						rich_print(table)
					if ate[1] == "set":
						table.add_row("set", "Modülün opsiyonlarını değiştirmeni sağlar. (set option value)")
						rich_print(table)
					if ate[1] == "show":
						table.add_row("show", "info, modül bilgisini ekrana basar.(show info) options, opsiyonları listeler. (show options)")
						rich_print(table)


				else:
					table = Table(title="Komut Tablosu", header_style="bold blue")
					table.add_column("Komut", style="cyan")
					table.add_column("Açıklama", style="green")
					table.add_row("help", "Yardım komutu, komutların dökümansıyonunu sağlar")
					table.add_row("back", "Modülü kullandığın promptu sonlandırıp ana prompta geçmeni sağlar")
					table.add_row("run", "Modülü çalıştırır. (Modülün options verisini run fonksiyonuna vererek çalıştırır)")
					table.add_row("set", "Modülün opsiyonlarını değiştirmeni sağlar. (set option value)")
					table.add_row("show", "info, modül bilgisini ekrana basar.(show info) options, opsiyonları listeler. (show options)")
					rich_print(table)

def bannerim():
	print(Lolcat(Banner("Mah Framework"), spread = 1))
	ozel_print.statu("Mahmut Paşa size yazılımını kullandığınız için teşekkür ediyor.")
	print("Mevcut modül sayısı: "+str(len(os.listdir("modules"))))
	print()
bannerim()

exitim= 0
while exitim!=1:
	text = prompt(HTML("<ansicyan>mah</ansicyan> > "), completer=completer, history=historyim)
	atext = text.split()
	if len(atext) > 0:
		if atext[0] == "exit":
			exitim = 1

		if atext[0] == "use":
			if len(atext) > 1:
				if atext[1] in modules:
					use_prompt(atext[1])
				else:
					ozel_print.basarisiz("Modül tespit edilemedi")

			else:
				ozel_print.bilgi("Örnek kullanım:\nuse modules/module.py")

		if atext[0] == "clear":
			os.system("clear")

		if atext[0] == "info":
			if len(atext) > 1:
				ozel_print.bilgi("info:\n"+get_module_info(atext[1]))
			else:
				ozel_print.bilgi("Örnek kullanım:\ninfo modules/module.py")


		if atext[0] == "show":
			if len(atext) > 1:
				if atext[1] == "modules":
					table_of_modules(generate_info_pack())

				if atext[1] == "info":
					print("Mah Framework 5 - Mahmut(Paşa) tarafından kodlandı.\nMah Framwork benim Metasploit Framework gibi 3 taraf modül destekleyen bir platform kodlama hayalim sonucu kodlanan bir projedir.\nMah Framework 5 ile 3. taraf modül desteği gelmiştir, kendi modüllerini 'modules' dizinine atarak Mah Framework üzerinden kullanabilirsiniz. Modül şartları:\n1.info(string) değişkeni olacak.\n2.options(dict) değişkeni olacak.\n3.run(func) fonksiyonu olacak ve options değişkenine uygun olacak.\nRahmetli Babam Mehmet P. anısına.")
			else:
				ozel_print.bilgi("Şu parametleri kullanabilirsin: modules - info")

		if atext[0] == "banner":
			bannerim()

		if atext[0] == "search":
			if len(atext) > 1:
				str_search(modules, atext[1])
			else:
				ozel_print.bilgi("Örnek kullanım:\nsearch string")


		if atext[0] == "help":
			if len(atext)> 1:
				komutlar = {
						"help": "Komutlar için yardım tablosunu ekrana basar",
						"exit": "Promptu sonlandırır ve kullanıcı çıkışını sağlar",
						"exec": "Linux terminal komutlarını çalıştırmaya yarar",
						"search": "Verilen argüman üzerinden modül arar",
						"show": "modules - info, parametreleri ile kullanın",
						"info": "Modül parametresi alır ve bilgi sağlar",
						"use": "Modülleri kullanmanızı sağlar",
						"clear": "Terminali temizler",
						"banner": "Bannerı ekrana basar"
					}
				if atext[1] in komutlar.keys():
					table = Table(title="Komut listesi", header_style= "bold cyan")
					table.add_column("Komut", style="cyan")
					table.add_column("Komut açıklaması", style = "green")
					table.add_row(atext[1], komutlar[atext[1]])
					rich_print(table)


				else:
					ozel_print.hata("Komut bulunamadı")
			else:
				table = Table(title="Komut listesi", header_style= "bold cyan")
				table.add_column("Komut", style="cyan")
				table.add_column("Komut açıklaması", style = "green")
				table.add_row("help", "Komutlar için yardım tablosunu ekrana basar")
				table.add_row("exit", "Promptu sonlandırır ve kullanıcı çıkışını sağlar")
				table.add_row("exec", "Linux terminal komutlarını çalıştırmaya yarar")
				table.add_row("search", "Verilen argüman üzerinden modül arar")
				table.add_row("show", "modules - info, parametreleri ile kullanın")
				table.add_row("info", "Modül parametresi alır ve bilgi sağlar")
				table.add_row("use", "Modülleri kullanmanızı sağlar")
				table.add_row("clear", "Terminali temizler")
				table.add_row("banner", "Bannerı ekrana basar")
				rich_print(table)

		if atext[0] == "exec":
			if len(atext) > 1:
				komutum = ""
				for i in atext[1:]:
					komutum = komutum + " " + i
				os.system(komutum)
			else:
				ozel_print.bilgi("Örnek kullanım:\nexec commands args")
