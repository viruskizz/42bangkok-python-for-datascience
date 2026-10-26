import matplotlib.pyplot as plt
from load_image import ft_load

img = ft_load("landscape.jpg")
plt.imshow(img)  # Render the image data on the current axes
plt.axis("on")   # Display the x-axis and y-axis around the image
plt.show()       # Open and display the prepared figure