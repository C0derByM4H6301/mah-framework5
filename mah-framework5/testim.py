from lib.module import listModule
from lib.module import get_module_info
from lib.module import get_module_desc
from lib.module import get_module_run
from lib.module import get_module_options
from lib.module import listModule_with_os_walk, fazlalari_sil
from lib.db import str_search, generate_info_pack,table_of_modules
from lib.console_func import *
for i in listModule():
	print("module - "+i)
	print(i+" info=",get_module_info("modules/"+i))
	print(i+" desc=",get_module_desc("modules/"+i))
	print(i+" options=",get_module_options("modules/"+i))
	print(i+" run=", get_module_run("modules/"+i))
	runy = get_module_run("modules/"+i)
	runy(get_module_options("modules/"+i))

for i in fazlalari_sil(listModule_with_os_walk()):
	print(i)
	print("module - "+i)
	print(i+" info=",get_module_info(i))
	print(i+" desc=",get_module_desc(i))
	print(i+" options=",get_module_options(i))
	print(i+" run=", get_module_run(i))
	runy = get_module_run(i)
	runy(get_module_options(i))
print(generate_info_pack())
listim =[]
for isi in generate_info_pack():
	listim.append(isi[0])
print(listim)
str_search(listim, "test")

table_of_modules(generate_info_pack())
ozel_print.bilgi("test yazı 1")
ozel_print.statu("test yazı 2")
ozel_print.hata("test yazı 3")
ozel_print.basarili("test yazı 4")
ozel_print.basarisiz("test yazı 5")

