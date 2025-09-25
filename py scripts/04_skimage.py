from skimage import io, color
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

# Load the image of the labrador
# From https://commons.wikimedia.org/wiki/File:Afra_013.jpg
# Using relative path, root base is python-basics\python-basics folder
labrador = io.imread("input/Afra_013.jpg")
# Convert the image to grayscale
gray_labrador = color.rgb2gray(labrador)
# Display the grayscale image
plt.axis("off") # turn off axis
plt.imshow(gray_labrador, cmap='gray')
plt.savefig("output/labrador_gray.png", dpi=300)  # save figure
plt.show()

# Load image of ants
# From https://commons.wikimedia.org/wiki/File:Ants_on_a_dandelion.jpg
ants = io.imread("input/Ants_on_a_dandelion.jpg")
print(ants.shape)  # (height, width, channels)

# Display the three color channels separately
fig, ax = plt.subplots(2,2, figsize=(8,8))
red_ch = ax[0][0].imshow(ants[:,:,0], cmap="Reds")
ax[0][0].set_title("Red channel")
ax[0][0].axis("off")
plt.colorbar(red_ch, ax=ax[0][0], fraction=0.046, pad=0.04)

green_ch = ax[0][1].imshow(ants[:,:,1], cmap="Greens")
ax[0][1].set_title("Green channel")
ax[0][1].axis("off")
plt.colorbar(green_ch, ax=ax[0][1], fraction=0.046, pad=0.04)

blue_ch = ax[1][0].imshow(ants[:,:,2], cmap="Blues")
ax[1][0].set_title("Blue channel")
ax[1][0].axis("off")
plt.colorbar(blue_ch, ax=ax[1][0], fraction=0.046, pad=0.04)

# Original rgb image
ax[1][1].imshow(ants)
ax[1][1].set_title("Original image")
ax[1][1].axis("off")
plt.savefig("output/ants_channels.png", dpi=300)
plt.show()

# Thresholding on gray scale image
gray_ants = color.rgb2gray(ants)
thresh = threshold_otsu(gray_ants)
binary_ants = gray_ants > thresh
plt.imshow(binary_ants, cmap='gray')
plt.axis("off")
plt.savefig("output/ants_binary.png", dpi=300)
plt.show()