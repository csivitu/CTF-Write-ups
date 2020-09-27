# This fixes all pngs

png_magic = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

for i in range(100):
    for j in range(100):
        f = "flag_"+str(i)+"_"+str(j)+".jpg"
        content = open(f, 'rb').read()
        patched = png_magic + content[len(png_magic)+2:]
        open("fixed_"+str(i)+"_"+str(j)+".jpg", 'wb').write(patched)

