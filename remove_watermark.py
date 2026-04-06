import cv2
import numpy as np

img = cv2.imread('img_v3_0210b_ed2baebc-b944-4433-9518-08d7b0c5815g.png')
h, w, _ = img.shape

# The watermark is in the bottom right corner. Let's guess the region.
# We can create a mask. We might need to find the watermark area first.
# Let's just crop the bottom right and save it to see where it is, or we can use a heuristic.
# Usually it's around the last 200x200 pixels.
roi = img[h-200:h, w-300:w]
cv2.imwrite('roi.png', roi)
