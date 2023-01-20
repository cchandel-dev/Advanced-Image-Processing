import cv2, sys
def get_kp(image, top):
    # Converting image to grayscale
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Applying SIFT detector
    sift = cv2.xfeatures2d.SIFT_create() 
    kp = sift.detect(gray, None)

    # To return a new list, use the sorted() built-in function - tuples are immutable...
    kp = sorted(kp, key=lambda x: x.response, reverse=True)

    #only want the top 10 keypoints
    kp = kp[:top]
    
    # Marking the keypoint on the image using circles
    image = cv2.drawKeypoints(gray ,
                        kp ,
                        image ,
                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    cv2.imwrite('output/train-tracks-with-keypoints.jpg', image)
    return kp