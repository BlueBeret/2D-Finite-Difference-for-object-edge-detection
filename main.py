# python 3.9
# requirements bisa diinstall dengan pip install -r requirements.txt

from PIL import Image

# fungsi untuk menghitung L2 norm
def calculateL2Norm(dx, dy):
    return (dx ** 2 + dy ** 2) ** 0.5

# fungsi untuk menggabung 2 gambar
def combineImage(img1, img2):
    result = Image.new('RGB', (img1.width + img2.width, img1.height))
    result.paste(img1, (0, 0))
    result.paste(img2, (img1.width, 0))
    return result


# fungsi utama, img adalah gambar yang ingin diteteksi
# boundary adalah batas penentu good value percobaan
# yang saya lakukan adalah antara 5-20

def predictObjectEdge(img, boundary):
    # mengubah menjadi greyscale
    img_grey = img.convert('L')
    img_result = Image.new('L', img_grey.size)
    # main loop
    for x in range(1, img_grey.width-1):
        for y in range(1, img_grey.height-1):
            # mengambil pixel tengah dan sekitarnya
            currentpixel = img_grey.getpixel((x, y))
            leftpixel = img_grey.getpixel((x - 1, y))
            rightpixel = img_grey.getpixel((x + 1, y))
            toppixel = img_grey.getpixel((x, y - 1))
            bottompixel = img_grey.getpixel((x, y + 1))
            # menghitung dx,dy, dan L2 norm
            dx = (abs(leftpixel - currentpixel) + abs(rightpixel - currentpixel))/2
            dy = (abs(toppixel - currentpixel) + abs(bottompixel - currentpixel))/2
            norm = calculateL2Norm(dx, dy)

            # jika nilainya lebih dari boundary 
            # maka merupakan edge dan diberi warna putih
            # jika kurang maka bukan edge dan diberi warna hitam
            if norm > boundary :
                img_result.putpixel((x, y), 255)
            else:
                img_result.putpixel((x, y), 0)

    return img_result

if __name__ == '__main__':
    # sunflower object
    if (False):
        img = Image.open('./sample_sunflower.jpg')
        img_result = combineImage(img, predictObjectEdge(img, 20))
        img_result.show()
        img_result.save('./result/result_20.jpg')
        
        img_result = combineImage(img, predictObjectEdge(img, 15))
        img_result.show()
        img_result.save('./result/result_15.jpg')

        img_result = combineImage(img, predictObjectEdge(img, 10))
        img_result.show()
        img_result.save('./result/result_10.jpg')

        img_result = combineImage(img, predictObjectEdge(img, 5))
        img_result.show()
        img_result.save('./result/result_5.jpg')

    # alpaca object
    img = Image.open('./sample_alpaca.jpg')
    img_result = combineImage(img, predictObjectEdge(img, 20))
    img_result.show()
    img_result.save('./result/result_alpaca_20.jpg')

    img_result = combineImage(img, predictObjectEdge(img, 15))
    img_result.show()
    img_result.save('./result/result_alpaca_15.jpg')

    img_result = combineImage(img, predictObjectEdge(img, 10))
    img_result.show()
    img_result.save('./result/result_alpaca_10.jpg')

    img_result = combineImage(img, predictObjectEdge(img, 5))
    img_result.show()
    img_result.save('./result/result_alpaca_5.jpg')
