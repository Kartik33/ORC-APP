import xml.etree.ElementTree as ET
from glob import glob
import cv2

#this is the path to cordinates which have not been edited 
tree_path = '../resources/Bill2/win_xml/IMG_20171112_190347.xml'
#path to cordinates which have been edited 
edited_tree_path = '../resources/Bill2/wintech_xml/IMG_20171112_190347.xml'

def get_cordinate(path):
    tree = ET.parse(path)
    root = tree.getroot()
    all_cordinates = []
    for obj in root.findall('object'):
        #print(obj.find('name').text)
        for bndbox in obj.findall('bndbox'):
            one_box_cordinates = []
            for b in bndbox:
                one_box_cordinates.append(b.text)
            all_cordinates.append(one_box_cordinates)
            
    return all_cordinates

def get_xml_list(tree_path , edited_tree_path):
    #all_orig_xml = []
    all_edited_tree = []
    for imgpath in glob(tree_path+'IMG*'):
        imgname = imgpath.split('/')[-1]

        etp = edited_tree_path+imgname

        #orig_xml = get_cordinate(imgpath)
        edited_tree = get_cordinate(etp)
        all_edited_tree.append(edited_tree)
        #all_orig_xml.append(orig_xml)
    return all_edited_tree 

def get_cordinates_list():    
    tree_path = '../resources/Bill2/win_xml/'
    edited_tree_path='../resources/Bill2/wintech_xml/'

    return get_xml_list(tree_path , edited_tree_path)

#call this mehotd to load the list of all cordinates in memory in format 
#[ [[xmin,ymin,xmax,ymax ] , [xmin,ymin,xmax,ymax]....]  , [  [xmin,ymin,xmax,ymax ] , [xmin,ymin,xmax,ymax]... ] 
all_edited_tree = get_cordinates_list()

#genrate mask here 
def gen_mask(all_edited_tree):
        return None
    

    
    