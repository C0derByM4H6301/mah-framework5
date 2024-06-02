from .module import listModule
from .module import get_module_info
from .module import get_module_desc
from .module import get_module_run
from .module import get_module_options
from .module import listModule_with_os_walk
import re
from rich.table import Table
from rich.console import Console


module_info_pack_set = []
def str_search(liste, terim):
	eslesenler = []
	regex = re.compile(terim)
	for string in liste:
		if regex.search(string):
			eslesenler.append(string)
	if eslesenler:
		for string in eslesenler:
			print(string)
	else:
		print("Bulunamadı")

def info_pack(dir,info,desc):
	return [dir,info,desc]

def generate_info_pack():
	for i in listModule_with_os_walk():
		module_info_pack_set.append(info_pack(i, get_module_info(i), get_module_desc(i)))
	return module_info_pack_set

def table_of_modules(listim):
	listim = fazlalari_sil(listim)
	konsol = Console()
	tablo = Table(title="Modül listesi")
	tablo.add_column("Yol",justify="left")
	tablo.add_column("Bilgi", justify="left")
	tablo.add_column("Açıklama", justify="left")
	for veri in listim:
		tablo.add_row(*veri)
	konsol.print(tablo)

def fazlalari_sil(liste):
	gorulmus = []
	bensersiz_liste = []
	for alt_liste in liste:
		if alt_liste not in gorulmus:
			bensersiz_liste.append(alt_liste)
			gorulmus.append(alt_liste)
	return bensersiz_liste


