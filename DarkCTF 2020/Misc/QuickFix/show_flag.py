# This shows the flag


from PIL import Image

flag = Image.new('RGB', (20*100, 20*100))
for i in range(100):
    for j in range(100):
        f = "fixed_"+str(i)+"_"+str(j)+".jpg"
        im = Image.open(f)
        flag.paste(im, (20*j, 20*i))

flag.show()