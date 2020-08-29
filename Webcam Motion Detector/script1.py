import cv2
img=cv2.imread("img2.jpeg",-1)#the 2nd parameter specifies howu want to read the image in python
#1.if you want to read the image RBG then give the parameter as 1 i.e total 3 bands red,blue and green
#2.if you want to read the image as black n white (grayscale) as 0 only 1 band
#3.-1 means colored image but you also have alpha channel that means your image will have transparency capability
#print(type(img))
#numpy.ndarray numoy n-dimensional array
#print(img)
#print(img.shape)#this is image resolution
#SO PYTHON STORES IMAGE AS NUMPY ARRAY
#print(img.ndim)



resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#image is resized to fit it into the window
cv2.imwrite("resizedimg.jpg",resized_image)
cv2.imshow("Test Title",resized_image)
cv2.waitKey(0)
#cv2.destroyAllWindows()
