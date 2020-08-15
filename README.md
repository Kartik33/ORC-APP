# ORC-APP

Structure :
app
  src
     helper
  ouptput
     image
     mask

src folder contains the ipython notebook<br>
***It can be see in the mask(left image) the model ignores the picture of the man and only captures the text.***
<p float="left">
  <img src="https://github.com/Kartik33/ORC-APP/blob/master/app/output/mask/IMG_20180104_142035.jpg" width="100" />
  <img src="https://github.com/Kartik33/ORC-APP/blob/master/app/output/img/IMG_20180104_142035.jpg" width="100" /> 
</p>

output contains two folders  
	image : contains raw images
	mask : contains the output mask of the image after processing from the model 
	
model can be downloaded here from the link given below 

https://drive.google.com/open?id=1jTGfbn8VTuU7UQqQRRDqDvqYRSitdbpm

Upload this model to the HED-keras model 

Change the input layer size to 512x512    
