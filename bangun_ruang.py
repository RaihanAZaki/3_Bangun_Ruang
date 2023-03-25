print("\033c");
import matplotlib.pyplot as plt
from library import *

# // ******************************************** Lingkaran ************************************************* //
a = 400
b = 600
radiusMax = int(300)
batas1 = int(0.4 * radiusMax)
# // ***************************************** Function Lingkaran ******************************************* //
def Lingkaran():
    for i in range(0, row + 1):
        print('Loading...')
        for j in range(0, col + 1):
            if ((i - a) ** 2 + (j - b) ** 2) >= 0 and ((i - a) ** 2 + (j - b) ** 2) < batas1 ** 2:
                Gambar[i, j, 0] = 255


# // ******************************************************************************************************** //
# // ******************************************* Bangun SegiLima ******************************************** //
# // ******************************************************************************************************** //
y1_l = 550
x1_l = 550
y2_l = 551
x2_l = 550
# // ***************************************** Function SegiLima ******************************************* //
def SegiLima(Gambar, y1_l, x1_l, y2_l, x2_l, hd, hw, pr, pg, pb, lr, lg, lb):
    while y1_l < 650:
        y2_l += 1
        y1_l += 1
        x2_l += 1
        x1_l -= 1
        hasil = buat_garis(Gambar, y1_l, x1_l, y2_l, x2_l, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil

    while y1_l < 750:
        y2_l += 2
        y1_l += 2
        x2_l -= 1
        x1_l += 1
        hasil = buat_garis(Gambar, y1_l, x1_l, y2_l, x2_l, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil


# // ******************************************************************************************************** //
# // ******************************************* Bangun SegiEnam ******************************************** //
# // ******************************************************************************************************** //
y1_h = 400
x1_h = 285
y2_h = 400
x2_h = 400
# // ***************************************** Function SegiEnam ******************************************* //
def SegiEnam(Gambar, y1_h, x1_h, y2_h, x2_h, hd, hw, pr, pg, pb, lr, lg, lb):
    while y1_h < 500:
        y2_h += 2
        y1_h += 2
        x2_h += 1
        x1_h -= 1
        hasil = buat_garis(Gambar, y1_h, x1_h, y2_h, x2_h, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil

    while y1_h < 600:
        y2_h += 2
        y1_h += 2
        x2_h -= 1
        x1_h += 1
        hasil = buat_garis(Gambar, y1_h, x1_h, y2_h, x2_h, hd, hw, pr, pg, pb, lr, lg, lb)
        Gambar = hasil


# Penampung hasil dari masing-masing function
hasil = Lingkaran()
hasil = SegiLima(Gambar, y1_l, x1_l, y2_l, x2_l, hd2, hw, pr, pg, pb, lr, lg, lb)
hasil = SegiEnam(Gambar, y1_h, x1_h, y2_h, x2_h, hd2, hw, pr, pg, pb, lr, lg, lb)


plt.figure("UJIAN TENGAH SEMESTER")
plt.imshow(Gambar)
plt.show()