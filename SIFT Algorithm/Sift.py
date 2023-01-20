import cv2, sys
  
# Loading the image
img = 0
if len(sys.argv)>1:
    img = cv2.imread('input/train-tracks{}.jpg'.format(sys.argv[1]))
else:
    img = cv2.imread('input/train-tracks.jpg')
 # Converting image to grayscale
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  
# Applying SIFT detector
sift = cv2.xfeatures2d.SIFT_create() 
kp = sift.detect(gray, None)

# To return a new list, use the sorted() built-in function - tuples are immutable...
kp = sorted(kp, key=lambda x: x.response, reverse=True)

#only want the top 10 keypoints
kp = kp[:30]

# Marking the keypoint on the image using circles
img=cv2.drawKeypoints(gray ,
                      kp ,
                      img ,
                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
  
cv2.imwrite('output/train-tracks-with-keypoints.jpg', img)