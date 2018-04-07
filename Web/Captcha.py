#http://code.activestate.com/recipes/440588/

import random
from PIL import Image, ImageFilter, ImageFont, ImageDraw

def gen_captcha(text, font, filename, fmt='JPEG'):
	f_color = random.randint(0,0xffff00)
	b_color = f_color ^ 0xffffff

	font = ImageFont.truetype(font, 24)

	dim = font.getsize(text)

	im = Image.new('RGB', (dim[0] + 5, dim[1] + 5), b_color)
	d = ImageDraw.Draw(im)
	x,y = im.size
	r = random.randint

	for num in range(100):
		d.rectangle((r(0,x),r(0,y),r(0,x),r(0,y)),fill=r(0,0xffffff))
	
	d.text((3,3), text, font=font, fill=f_color)
	im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
	
	im.save(filename, format=fmt)

def gen_random_word(wordLen=6):
    allowedChars = "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWZYZ0123456789"
    word = ""
    for i in range(0, wordLen):
        word = word + allowedChars[random.randint(0,0xffffff) % len(allowedChars)]
    return word

if __name__ == '__main__':
	word = gen_random_word()
	gen_captcha(word.strip(), 'Roboto-Black.ttf', "test.jpeg")