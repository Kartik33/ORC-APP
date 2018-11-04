def apply_kernel(name,img,params):
    if name == 'gauss':
        return cv2.GaussianBlur(img,*params) 
    if name == 'median':
        return cv2.medianBlur(img,*params)
    if name == 'filter2d':
        return cv2.filter2D(img,*params)
    if name == 'bilateral':
        return cv2.bilateralFilter(img,*params) # keep edges sharp
    if name == 'erod':
        return cv2.erode(img,*params)
    if name == 'dilate':
        return cv2.dilate(img,*params)
    if name == 'closing':
        return cv2.morphologyEx(img,*params)
    if name == 'opening':
        return cv2.morphologyEx(img,*params)
    if name == 'tophat':
        return cv2.morphologyEx(img,*params)
    if name == 'adaptthgauss':
        return cv2.adaptiveThreshold(img,*params)