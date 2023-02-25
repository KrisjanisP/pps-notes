from PIL import Image
import os

def stitch(img1, img2, img3, img4):
    w = [img1.size[0], img2.size[0], img3.size[0], img4.size[0]]
    h = [img1.size[1], img2.size[1], img3.size[1], img4.size[1]]
    res_w = max(w[0],w[3])+max(w[1],w[2])
    res_h = max(h[0],h[1])+max(h[2],h[3])
    res = Image.new('RGB',(res_w,res_h))
    c_x, c_y = res_w//2, res_h//2
    res.paste(im=img1, box=(c_x-w[0],c_y-h[0]))
    res.paste(im=img2, box=(c_x,c_y-h[1]))
    res.paste(im=img3, box=(c_x,c_y))
    res.paste(im=img4, box=(c_x-w[3],c_y))
    return res

print(os.listdir("images"))
imgs = [Image.open(os.path.join("images",f))
            for f in os.listdir("images")]

for i in range(len(imgs)//4):
    res = stitch(imgs[i*4],imgs[i*4+1],imgs[i*4+2],imgs[i*4+3])
    res.save("result/"+str(i)+".jpg")
