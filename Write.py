import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scio

input_layer_size = 400  # 20x20 像素矩阵
num_labels = 10     # 手写数字 0,1,2,3,4,5,6,7,8,9

data = scio.loadmat('ex3data1.mat')
X = data['X']
y = data['y'].flatten()
m = y.size

def display_data(x):
 (m, n) = x.shape
 # m = 100
 # n = 400

 # 设置每个数字的宽度与高度(像素)
 example_width = np.round(np.sqrt(n)).astype(int)# example_width=20
 example_height = (n / example_width).astype(int) #example_height=20

 # 计算显示的行数与列数
 display_rows = np.floor(np.sqrt(m)).astype(int) #display_rows=10
 display_cols = np.ceil(m / display_rows).astype(int)#display_rows=10

 # 单个图像之间的间隔
 pad = 1

 # 设置并初始化显示像素矩阵的大小211*211 ,1+(10*20+1)
 display_array = - np.ones((pad + display_rows * (example_height + pad),
                           pad + display_rows * (example_height + pad)))

 # 将每个训练样本显示在矩阵中
 curr_ex = 0 
 for j in range(display_rows):
     for i in range(display_cols):
         if curr_ex > m:
             break

         # 每次每行和每列读取一个20*20像素的数字，矩阵大小加21
         # 实际上矩阵形式可以认为 10*10*400(20*20像素)
         max_val = np.max(np.abs(x[curr_ex]))
         display_array[pad + j * (example_height + pad) + np.arange(example_height),
                       pad + i * (example_width + pad) + np.arange(example_width)[:, np.newaxis]] = \
                       x[curr_ex].reshape((example_height, example_width)) / max_val
         curr_ex += 1

     if curr_ex > m:
         break

 # Display image
 plt.figure()
 plt.imshow(display_array, cmap='gray', extent=[-1, 1, -1, 1])
 plt.axis('off')  
  
  
