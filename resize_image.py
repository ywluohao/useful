from PIL import Image
import os


def verify_number():
    while True:
        try:
            v = int(input().strip())
        except:
            print("This is not an integer, please enter again: ")
            continue
        else:
            return v
            break


print('Please enter the path to the image')
image_file = input().strip()
while not os.path.isfile(image_file):
    print("This is not a valid file name, please enter again: ")
    image_file = input().strip()

print('Please enter the basewidth')
basewidth = verify_number()
img = Image.open(image_file)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save(image_file.split('.')[0] + '_width_' +
         str(basewidth) + '.' + image_file.split('.')[1])
