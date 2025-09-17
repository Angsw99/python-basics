from skimage import io, color
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

# Load the image of the labrador
# From https://commons.wikimedia.org/wiki/File:Afra_013.jpg
#labrador = io.imread('Afra_013.jpg')
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


fig, ax = plt.subplots(2,2, figsize=(8,8))
ax[0][0].imshow(ants[:,:,0])
ax[0][0].set_title("Red channel")
ax[0][0].axis("off")

ax[0][1].imshow(ants[:,:,1])
ax[0][1].set_title("Green channel")
ax[0][1].axis("off")

ax[1][0].imshow(ants[:,:,2])
ax[1][0].set_title("Blue channel")
ax[1][0].axis("off")

ax[1][1].imshow(ants)
ax[1][1].set_title("Original image")
ax[1][1].axis("off")
plt.savefig("output/ants_channels.png", dpi=300)
plt.show()

#thresholding on gray scale image
gray_ants = color.rgb2gray(ants)
thresh = threshold_otsu(gray_ants)
binary_ants = gray_ants > thresh
plt.imshow(binary_ants, cmap='gray')
plt.axis("off")
plt.savefig("output/ants_binary.png", dpi=300)
plt.show()