
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = et.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def cmn_xml(folder_name , img_name , path, img_size):

    top = et.Element('annotation')

    comment = et.Comment('contours')
    top.append(comment)

    folder = SubElement(top, 'folder')
    folder.text = folder_name

    filename = SubElement(top, 'filename')
    filename.text = img_name
    
    path_tag = SubElement(top, 'path')
    path_tag.text = path
    
    src = SubElement(top , 'source')
    db = SubElement(src , 'database')
    db.text = 'Unknown'
    
    size = SubElement(top , 'size')
    width = SubElement(size , 'width')
    width.text = str(img_size[1])
    height = SubElement(size , 'height')
    height.text = str(img_size[0])
    depth = SubElement( size ,'depth')
    depth.text = str(img_size[2])
    return top

def xml_object(top , i , contour):
    
    obj = SubElement(top , 'object')
    name_tag = SubElement(obj , 'name')
    name_tag.text = str(i)
    pose_tag = SubElement(obj , 'pose')
    pose_tag.text = 'Unspecified'
    truncated_tag = SubElement(obj , 'truncated')
    truncated_tag.text = str(0)
    difficult_tag = SubElement(obj , 'difficult')
    difficult_tag.text = str(0)
    box = SubElement(obj , 'bndbox')
    xmin = SubElement(box , 'xmin')
    xmin.text = str(contour[0])
    ymin = SubElement(box , 'ymin')
    ymin.text = str(contour[1])
    xmax = SubElement(box , 'xmax')
    xmax.text = str(contour[2])
    ymax = SubElement(box , 'ymax')
    ymax.text = str(contour[3])
    
    return top

def gen_xml(contours ,folder, img_name , file_path , img_size):
    top = cmn_xml(folder , img_name , file_path ,img_size)
    i = 0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        a = (x,y,x+w,y+h)
        
        obj = xml_object(top , i , a)
        top = obj
        i = i+1
        
    return top 