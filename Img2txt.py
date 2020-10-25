import cv2
import numpy as np


def main(img):
    txt_dict = {255: 'A', 0: 'B'}
    h, w = img.shape
    txt = ""
    for j in range(h):
        for i in range(w):
            txt += txt_dict[img[j, i]]
        txt += "<br>\n"
    print(txt)


def img_loader():
    img_root = "C:\\Users\\coldj\\Pictures\\WW.png"
    return cv2.imread(img_root)


def letter2img():
    letter = "Hello CV"
    length = len(letter)
    sketch_img = np.zeros((15, 10*length), dtype=np.uint8)
    sketch_img = cv2.putText(sketch_img, letter, (0, 12), 1, 1, 255, 1)
    cv2.imshow("test", sketch_img)
    cv2.waitKey(0)
    return sketch_img


if __name__ == '__main__':
    image = letter2img()
    main(image)

