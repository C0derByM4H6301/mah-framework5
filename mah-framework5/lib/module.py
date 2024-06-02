
def listModule(direc="modules"):
	import os
	modules = []
	for i in os.listdir(direc):
		modules.append(i)
	return modules
def fazlalari_sil(string_listesi):
	gorulmus = set()
	benzersiz_liste = []
	for string in string_listesi:
		if string not in gorulmus:
			benzersiz_liste.append(string)
			gorulmus.add(string)
	return benzersiz_liste


def listModule_with_os_walk(direc="modules"):
	import os
	dosyalar = []
	for dir, subdir, file_list in os.walk(direc):
		for file in file_list:
			if file.endswith(".py"):
				file_path = os.path.join(dir, file)
				dosyalar.append(file_path)
	return dosyalar

def get_module_info(module_dir):
	with open(module_dir) as f:
		code = f.read()
	lv = {}
	exec(code, {}, lv)
	return lv["info"]


def get_module_desc(module_dir):
	with open(module_dir) as f:
		code = f.read()
	lv = {}
	exec(code, {}, lv)
	return lv["desc"]

def get_module_run(module_dir):
	with open(module_dir) as f:
		code = f.read()
	lv = {}
	exec(code, {}, lv)
	return lv["run"]

def get_module_options(module_dir):
	with open(module_dir) as f:
		code = f.read()
	lv = {}
	exec(code, {}, lv)
	return lv["options"]
