from PIL import Image, ImageDraw, ImageFont

def main():
	
	img_path = raw_input("Enter the path of the image to add watermark to ")
	image = Image.open(img_path)
	i_width, i_height = image.size

	draw = ImageDraw.Draw(image)
	text = raw_input("Enter text for watermark ")

	font = ImageFont.truetype('/home/gaurav/Solutions/Web/Roboto-Black.ttf', 12)
	t_width, t_height = draw.textsize(text, font)

	x = i_width - t_width - 10
	y = i_height - t_height - 10

	draw.text((x,y), text, font=font)

	if img_path.endswith('.png'):
		image.save('test_wm.png')
	elif img_path.endswith('.jpeg'):
		image.save('test_wm.jpeg')

if __name__ == '__main__':
	main()
