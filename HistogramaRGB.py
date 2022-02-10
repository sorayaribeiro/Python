import cv2 as cv
from matplotlib import pyplot as plt

im = cv.imread("God2-Sistine_Chapel.png")

r, g, b = cv.split(im)
cv.imshow("im", im)

def histograma():
    plt.hist(r.ravel(), 256, [0, 256])
    plt.hist(g.ravel(), 256, [0, 256])
    plt.hist(b.ravel(), 256, [0, 256])
    hist = cv.calcHist([im], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.show()


if __name__ == '__main__':
    histograma()
