class Gen_mask_and_contours:
    v_kernel=[]
    h_kernel=[]
    def __init__(self):
        self.v_kernel.append(('dilate',[cv2.getStructuringElement(cv2.MORPH_RECT, (1,50)),1]))
        self.v_kernel.append(('erod',[cv2.getStructuringElement(cv2.MORPH_RECT, (1,70)),2]))
        
        self.h_kernel.append(('dilate',[cv2.getStructuringElement(cv2.MORPH_RECT, (50,1)),1]))
        self.h_kernel.append(('erod',[cv2.getStructuringElement(cv2.MORPH_RECT, (70,1)),2]))

    def find_contours_on_cropped_img_printedbills(self,fpath,contour_outfilepath = None,
                                                  mask_outfilepath = None,
                                                  debug = 0):
        '''
            Finds horizontal and vertical lines and generates
            mask and contour image
        '''
        img = None
        if fpath.split('/')[-1].split('.')[1]=='tiff':
            c_img = tiff.imread(fpath)
            img = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY)
        else:
            c_img = cv2.imread(fpath)
            img = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY)
    
        v_img=img.copy()
        for name,params in self.v_kernel:
            v_img=apply_kernel(name,v_img,params)
            if debugLvl > 0:
                print('Applying kernel : '+name)
                showimg(v_img)

        h_img=img.copy()
        for name,params in self.h_kernel:
            img=apply_kernel(name,h_img,params)
            if debugLvl > 0:
                print('Applying kernel : '+name)
                showimg(h_img)

        img_mask = cv2.add(cv2.bitwise_not(v_img) , cv2.bitwise_not(h_img))

        im2, contours, hierarchy = cv2.findContours(img_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            i = cv2.rectangle(c_img,(x,y),(x+w,y+h),(0,255,0),2)
        if debug > 0 :
            plt.imshow(img_mask,cmap='gray')
            plt.show()
            plt.imshow(c_img , cmap='gray')
            plt.show()
        else:
            if contour_outfilepath != None and mask_outfilepath != None:
                cv2.imwrite(mask_outfilepath , img_mask)
                x = cv2.imwrite(contour_outfilepath ,c_img)
            else:
                print('Please speciy path to save mask and image with contours ...Thank you ;p')
        #return orig,orig_area,contours,hierarchy

    def get_contours_hierarchy(self,fpath,debug=0):
        '''
            Returns img,img_mask,contours,hierarchy
        '''
        img = None
        if fpath.split('/')[-1].split('.')[1]=='tiff':
            c_img = tiff.imread(fpath)
            img = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY)
        else:
            c_img = cv2.imread(fpath)
            img = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY)
    
        v_img=img.copy()
        for name,params in self.v_kernel:
            v_img=apply_kernel(name,v_img,params)
            if debugLvl > 0:
                print('Applying kernel : '+name)
                showimg(v_img)

        h_img=img.copy()
        for name,params in self.h_kernel:
            img=apply_kernel(name,h_img,params)
            if debugLvl > 0:
                print('Applying kernel : '+name)
                showimg(h_img)

        img_mask = cv2.add(cv2.bitwise_not(v_img) , cv2.bitwise_not(h_img))
        im2, contours, hierarchy = cv2.findContours(img_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        return img,img_mask,contours,hierarchy
    
    def find_contour_on_all(self,input_dir,contour_outdir,mask_outdir):
        '''
            Find contours on all images in input folder
            Outputs masks in mask_outdir, contours in contour_outdir
            
            @arguments
            input_dir ... input directory containing all images
            contour_dir .. output directory to store contours
            mask_outdir .. output directory to store masks
        '''
        counter = 0
        imgpaths=glob(input_dir+'*.tif')+glob(input_dir+'*.jpg')+glob(input_dir+'*.png')+glob(input_dir+'*.jpeg')
        
        for imgpath in imgpaths:
            imgname = imgpath.split('/')[-1]
            contour_outfilepath = contour_outdir+imgname
            mask_outfilepath = mask_outdir + imgname
            find_contours_on_cropped_img_printedbills(fpath=imgpath,
                                                      contour_outfilepath=contour_outfilepath,
                                                      mask_outfilepath = mask_outfilepath,
                                                      debug=0)
            print(counter , 'processed ...'+imgname)
            counter = counter +1

    def find_contour_on_one(self,imgpath , debug = 0):
        find_contours_on_cropped_img_printedbills(fpath=imgpath,debug=1)