import numpy as np

# Membuat Canvas
row = int(1000)
col = int(1000)
print('col, row =', col, ',', row)

# Untuk memberikan warna pada point
pd2 = int(1); #untuk memberikan ketebalan pada point diameter function garis2
pr = 255;
pg = 255;
pb = 255
hd2 = int(pd2 / 2)  # Kalkulasi setengah poin diameter

# Untuk memberikan warna pada garis
lw = int(10);
lr = 0;
lg = 0;
lb = 255
hw = int(lw / 2)

Gambar = np.zeros(shape=(row+1, col+1, 3), dtype=np.uint8)  # memberikan latar hitam

# Function buat_garis
def buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
    # draw the first point
    for i in range(x1 - hd2, x1 + hd2):
        for j in range(y1 - hd2, y1 + hd2):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd2 ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb
    # draw the second point
    for i in range(x2 - hd2, x2 + hd2):
        for j in range(y2 - hd2, y2 + hd2):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd2 ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1
    # draw the horizontal line
    if dy <= dx:
        my = dy / dx
        for j in range(x1, x2):
            i = int(my * (j - x1) + y1)
            x = j
            y = i
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    # draw the vertical line
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    return Gambar

