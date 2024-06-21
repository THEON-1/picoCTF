#!/home/maxime/.pyvenv/bin/python3
from PIL import Image
import numpy as np

p = Image.open("scrambled1.png")
q = Image.open("scrambled2.png")

p = np.array(p)
q = np.array(q)

print(p.shape)

r = Image.fromarray(p + q)
r.save("out.png")

