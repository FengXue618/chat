
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	allen_words_count = 0
	viki_words_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_images_count = 0
	viki_images_count = 0
	for line in lines:
		s =  line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				allen_sticker_count += 1
			elif s[2] == '貼圖':
				allen_images_count += 1
			else:
				for m in s[2:]:
					allen_words_count += len(m)
		elif name == 'Viki':
			if s[2] == '圖片':
				viki_sticker_count += 1
			elif s[2] == '貼圖':
				viki_images_count += 1
			else:
				for m in s[2:]:
					viki_words_count += len(m)
	print('allen说了', allen_words_count, '个字，传了', allen_sticker_count, '图片')		
	print('viki说了', viki_words_count, '个字，传了', viki_sticker_count, '图片')
	print('allen传了', allen_images_count, '个贴图')
	print('viki传了', viki_images_count, '个贴图')
	



def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()
