#Run-Length Encoding

test = "AAAAAAAAAAAAAAABBCCCCDD"

def runLengthEncoding(string):
	finished = False
	idx, encoding = 0, ""
	while True:
		letter, count, finished = get_run(string)
		encoding += get_representation(letter, count)
		if not finished:
			string = string[count:]
			print(string, letter, count, finished)
		else:
			break
	return encoding

    pass

def get_run(string):
	if len(set(string)) == 1:
		return string[0], len(string), True
	else:
		start = string[0]
		idx = 0
		while start == string[idx]:
			idx+=1
		return start, idx, False

def get_representation(letter, count):
	if count == 9: #Check in order to avoid scenarion 9A0A
		return  ("9" + letter ) 
	else:
		return ("9" + letter ) * (count // 9) + (str(count % 9) + letter)




runLengthEncoding(test)
