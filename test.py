import cv2
# read image
image = cv2.imread('/Users/nilefahmy/PycharmProjects/fingerspell/c.gif')
# show the image, provide window name first
cv2.imshow('c.gif', image)
# add wait key. window waits until user presses a key
cv2.waitKey(0)
# and finally destroy/close all open windows
cv2.destroyAllWindows()