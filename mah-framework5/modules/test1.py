info = "info 1"
desc = "açıklama 1"
options = {"opt1":["option açıklama1","value1"]}

def run(option):
	for i in option.keys():
		print(option[i][1])

