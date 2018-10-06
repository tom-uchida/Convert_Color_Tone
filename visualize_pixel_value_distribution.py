# ==============================================
#       Visualize Pixel Value Distribution
# ==============================================



import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')



# -----------------------------
# ----- Placement setting -----
# -----------------------------
#plt.figure(figsize=(10, 8))
fig, ax = plt.subplots(4, figsize=(10, 7)) # figsize(width, height)
ax[0] = plt.subplot2grid((2,2), (0,0))
ax[1] = plt.subplot2grid((2,2), (0,1))
ax[2] = plt.subplot2grid((2,2), (1,0))
ax[3] = plt.subplot2grid((2,2), (1,1))
#ax[2] = plt.subplot2grid((2,2), (1,0), colspan=2)



# -------------------------------
# ----- Select input image  -----
# -------------------------------
image_name = 'images/2018-09-30/out_gaussian_RL100.jpg'
#image_name = 'images/2018-09-30/out_poisson_RL100.jpg'
#image_name = 'images/2018-09-30/out_spike_RL100.jpg'
#image_name = 'images/2018-10-03/plane_10M_RL100.jpg'
#image_name = 'images/2018-10-03/plane_noised_10M_RL100.jpg'
r_param, g_param, b_param = 3,3,3



# ----------------------------
# ----- Read input image -----
# ----------------------------
def read_img(_img_name):
  # read input image
  img_BGR = cv2.imread(_img_name)

  # convert color (BGR → RGB)
  img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

  return img_RGB

img_in_RGB = read_img(image_name)
print("Input image(RGB) : ", img_in_RGB.shape) # （height × width × 色数）



# ------------------------------
# ----- Change color tone -----
# ------------------------------
def change_color_tone(_rgb_img, _r_param, _g_param, _b_param):
  # Red
  red   = cv2.multiply(_rgb_img[:, :, 0], _r_param)

  # Green
  green = cv2.multiply(_rgb_img[:, :, 1], _g_param)

  # Blue
  blue  = cv2.multiply(_rgb_img[:, :, 2], _b_param)

  # Apply change
  revised_img_RGB = np.empty((_rgb_img.shape[0], _rgb_img.shape[1], 3), dtype=np.uint8)
  revised_img_RGB[:, :, 0] = red
  revised_img_RGB[:, :, 1] = green
  revised_img_RGB[:, :, 2] = blue

  return revised_img_RGB

# ===============================================
#      It is required to adjust parameters.
# ===============================================
img_out_RGB = change_color_tone(img_in_RGB, r_param, g_param, b_param)
print("\nOutput Image (RGB)")
print('R Max:',np.max(img_out_RGB[:, :, 0]),' Min:',np.min(img_out_RGB[:, :, 0]))
print('G Max:',np.max(img_out_RGB[:, :, 1]),' Min:',np.min(img_out_RGB[:, :, 1]))
print('B Max:',np.max(img_out_RGB[:, :, 2]),' Min:',np.min(img_out_RGB[:, :, 2]))
print("\n")



# -------------------------------
# ----- Convert RGB to Gray -----
# -------------------------------
img_in_Gray  = cv2.cvtColor(img_in_RGB,  cv2.COLOR_RGB2GRAY)
img_out_Gray = cv2.cvtColor(img_out_RGB, cv2.COLOR_RGB2GRAY)



# -----------------------------------------------
# ----- Get statistical data of pixel value -----
# -----------------------------------------------
def get_data_of_pixel_value(_img_gray, _img_name):
  print("===== Statistical Data of", _img_name, "(Gray) =====")
  print("Num of pixel values (== 255) :", np.sum(_img_gray == 255))
  print("Num of pixel values (== 0)   :", np.sum(_img_gray == 0) )
  print("\nMax :", np.max(_img_gray))
  print("Min :", np.min(_img_gray))
  print("\nAverage :", np.mean(_img_gray))
  print("Median  :", np.median(_img_gray))
  print("\n")
  return 

get_data_of_pixel_value(img_in_Gray, "Input Image")
get_data_of_pixel_value(img_out_Gray, "Output Image")



# -----------------------
# ----- Show images -----
# -----------------------
def show_img(_i, _img, _img_name):
  #plt.subplot(2, 2, _i)
  
  # image title
  ax[_i].set_title(_img_name)
  #plt.title(_img_name)

  # show image
  ax[_i].imshow(_img)
  #plt.imshow(_img)

  # off scale
  ax[_i].axis('off')

  return



# --------------------------------------
# ----- Display Input/Output Image -----
# --------------------------------------
show_img(0, img_in_RGB,  "Input Image")
show_img(1, img_out_RGB, "Output Image")
# show_img(2, img_in_Gray,  "Input Image(Gray)")
# show_img(3, img_out_Gray, "Output Image(Gray)")



# ----------------------------------------------
# ----- Visualize Pixel Value Distribution -----
# ----------------------------------------------
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Input Image
ax[2].set_title("Input Image")
img3 = ax[2].imshow(img_in_Gray, clim=[0,255], cmap='viridis')
ax[2].axis("image")
divider = make_axes_locatable(ax[2])
ax2_cb = divider.new_horizontal(size="4.5%", pad=0.1)
fig.add_axes(ax2_cb)
plt.colorbar(img3, cax=ax2_cb)
ax[2].axis('off')

# Output Image
ax[3].set_title("Output Image")
img4 = ax[3].imshow(img_out_Gray, clim=[0,255], cmap='viridis')
ax[3].axis("image")
divider = make_axes_locatable(ax[3])
ax3_cb = divider.new_horizontal(size="4.5%", pad=0.1)
fig.add_axes(ax3_cb)
plt.colorbar(img4, cax=ax3_cb)
ax[3].axis('off')

# plt.subplot(2, 2, 3)
# plt.imshow(img_in_Gray, cmap='viridis')
# plt.colorbar()
# plt.clim(0, 255)

# plt.subplot(2, 2, 4)
# plt.imshow(img_out_Gray, cmap='viridis')
# plt.colorbar()
# plt.clim(0, 255)


plt.show()



# ----------------------
# ----- Save image -----
# ----------------------
# img_out_BGR = cv2.cvtColor(img_out_RGB, cv2.COLOR_RGB2BGR)
# cv2.imwrite('images/out.jpg', img_out_BGR)