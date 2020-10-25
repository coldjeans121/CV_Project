import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def main(img, c0='ㄱ', c1='ㄴ'):
    txt_dict = {255: c0, 0: c1}
    h, w = img.shape
    txt = ""
    for j in range(h):
        for i in range(w):
            txt += txt_dict[img[j, i]]
        txt += "\n"
    print(txt)


def img_loader():
    img_root = "C:\\Users\\coldj\\Pictures\\WW.png"
    return cv2.imread(img_root)


def letter2img(height=15):
    letter = "테스트? Test!"
    length = len(letter)
    sketch_img = np.zeros((20, 20*length), dtype=np.uint8)
    # sketch_img = cv2.putText(sketch_img, letter, (0, 12), 1, 1, 255, 1)

    # put text in null image
    img_pil = Image.fromarray(sketch_img)
    draw = ImageDraw.Draw(img_pil)
    fontpath = "fonts/gulim.ttc"
    font = ImageFont.truetype(fontpath, 20)
    draw.text((0, 0), letter, font=font, fill=255)
    sketch_img = np.array(img_pil)

    cv2.imshow("test1", sketch_img)
    # height resize
    sketch_img = cv2.resize(sketch_img, (20*length, height))
    # margin cut resize
    for i in range(1, 20*length):
        if np.sum(sketch_img[:, -i]):
            sketch_img = sketch_img[:, :-i+2]
            break
    # binarization

    cv2.imshow("test2", sketch_img)
    sketch_img[sketch_img >= 100] = 255
    sketch_img[sketch_img < 100] = 0

    cv2.imshow("test", sketch_img)
    cv2.waitKey(0)
    return sketch_img


if __name__ == '__main__':
    image = letter2img()
    main(image)

