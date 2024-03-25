import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt
import matplotlib
from scipy import misc
from PIL import Image 

array=np.array([97, 0, 27, 18])
array.shape
array[3]
array.ndim

array_2d=np.array([[ 0, 4], [ 7, 5], [ 5, 97]])
array_2d.shape
array_2d.ndim
array_2d[2,1]

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

print(f"The ndim is {mystery_array.ndim} and the shape of the array is {mystery_array.shape}")
print(f"The number of mystery_array[2,1,3] in the given {mystery_array[:,:,0]}")

a=np.arange(10,30)

sliced_a=a[3:5]#The difference between first and the second value 5-3=2
print(sliced_a) #[13,14] two values are printed 

np.flip(a)
np.nonzero(a)

b=random((3,3,3))
print(b)

c=np.linspace(start=1,stop=13,num=8,dtype=int)
d=np.linspace(start=1,stop=24,num=8,dtype=int)
plt.plot(c,d)
plt.show()

noise=random((123,125,3))
plt.imshow(noise)

v1=np.array([[1,2,3,4],[4,2,3,2]])
v2=np.array([[1,4,6,8],[4,7,2,1]])

img=misc.face()
img
type(img)
img.shape
sRGB=img/255
flipped_array=np.flip(sRGB)
flipped_array
grey_values=np.array([0.2126,0.7152,0.0722])
b_w=sRGB@grey_values
b_w
plt.imshow(b_w,cmap='gray')
plt.imshow(255-img)
plt.imshow(flipped_array)
plt.imshow(np.rot90(sRGB))

