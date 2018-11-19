
def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Frank':
			person = 'Frank'
			continue
		elif line == 'Allen':
			person = 'Allen'
			continue
		if person:
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
"""
['Frank\n', '哈啰\n', '你好\n', 'Allen\n', 
'你好\n', '你想喝点什么？\n', 'Frank\n', '嗯\n', 
'来一杯红茶好了\t']
增加 strip() 后：
['Frank', '哈啰', '你好', 'Allen', 
'你好', '你想喝点什么？', 'Frank', '嗯', 
'来一杯红茶好了']

['Frank', '哈啰', '你好', 'Allen', '你好', '你想喝点
什么？', 'Frank', '嗯', '来一杯红茶好了', 'Allen', '好
嘞！', '很快就送到']
"""