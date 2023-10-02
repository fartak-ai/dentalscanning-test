import streamlit as st
from hydralit import HydraHeadApp
from streamlit_image_comparison import image_comparison
from PIL import Image

# import libraries
import cv2
import numpy as np
import json
from PIL import Image


# The `PredictApp` class is a subclass of `HydraHeadApp` that allows users to upload and display
# images for the purposes of predicting and displaying broken, repairing, and restored teeth.
class PredictApp(HydraHeadApp):

    def __init__(self, title = 'Loader Playground', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

        self.h = hamid()


    def run(self):
        """
        The function `run` creates a web application using the Streamlit library to upload and display
        images in three columns.
        """

        st.title("Image Compare")

        _, col, _ = st.columns([2, 4, 2])

        # path = r'C:\Users\hamidr.bd\Documents\Programming\Python\Jupyter\Projects\8- Dental Scanning\code\Third phase\docs'
        # my_file = path + '\home-video.mp4'
        imagePath1 = r"docs/broken.jpg"
        imagePath2 = r"docs/restored.jpg"

        image1 = Image.open(imagePath1)
        image2 = Image.open(imagePath2)

        with col:
            # render image-comparison
            image_comparison(
                img1=image1,
                img2=image2,
                label1="Broken Tooth",
                label2="Restored Tooth",
                width=500,
                starting_position=50,
                show_labels=True,
                make_responsive=True,
                in_memory=True,
            )

        st.write('###')

        col1, col2, col3 = st.columns(3)
        uploaded_images = [None, None, None]

        # First Column for broken tooth
        with col1:

            st.header("Broken Tooth")

            image_file1 = st.file_uploader("Upload broken tooth image", type=["jpg", "png", "jpeg"])

            if image_file1 is not None:
                image1 = Image.open(image_file1)

                if image1 is not None:
                    img_array1 = np.array(image1)
                
                    if img_array1 is not None:
                        b = self.h.main(img_array1, image_file1.name, False)

                        if image_file1 is not None:
                            uploaded_images[0] = b

                            if uploaded_images[0] is not None:
                                st.image(uploaded_images[0], use_column_width=True)

                            else:
                                # pass
                                st.write(1)
                        
                        else:
                            # pass
                            st.write(2)
                        

                    else:
                        # pass
                        st.write(3)
                
                else:
                    # pass
                    st.write(4)

            else:
                # pass
                st.write(5)


        # Second column for repairing tooth
        with col2:

            st.header("Repairing Tooth")

            if uploaded_images[0] is not None:
                # pass
                # st.image(uploaded_images[0], use_column_width=True)

                image_file2 = st.file_uploader("Upload repairing tooth image", type=["jpg", "png", "jpeg"])

                if image_file2 is not None:
                    image2 = Image.open(image_file2)
                    # st.write("read image.")

                    if image2 is not None:
                        img_array2 = np.array(image2)
                        # st.write("convert image to np.array.")

                        if img_array2 is not None:
                            # st.write("b2.")
                            b2 = self.h.main(img_array2, image_file2.name, True)      
                            # b2 = self.h.main(img_array1, image_file1.name, False)

                            if image_file2 is not None:
                                uploaded_images[1] = b2
                                # st.write("image_file2")

                                if uploaded_images[1] is not None:
                                    st.image(uploaded_images[1], use_column_width=True)
                                    # st.write("show image.")

                                else:
                                    st.write(1)

                            else:
                                st.write(2)

                        else:
                            st.write(3)

                    else:
                        st.write(4)

                else:
                    st.write(5)

            else:
                # st.write("col 1 is empty.")
                pass

        # Third column for restored tooth
        with col3:
            
            st.header("Restored Tooth")

            if uploaded_images[1] is not None:
                # pass
                # st.image(uploaded_images[1], use_column_width=True)

                image_file3 = st.file_uploader("Upload restored tooth image", type=["jpg", "png", "jpeg"])

                if image_file3 is not None:
                    image = Image.open(image_file3)

                
                    if image is not None:
                        img_array = np.array(image)

                        if img_array is not None:
                            b = self.h.main(img_array, image_file3.name, False)

                            if image_file3 is not None:
                                uploaded_images[2] = b

                                if uploaded_images[2] is not None:
                                    st.image(uploaded_images[2], use_column_width=True)

        st.write('###')
        
        _, col, _ = st.columns([2, 4, 2])
        with col:
            # render image-
            if uploaded_images[2] is not None:
                image_comparison(
                    img1=uploaded_images[0],
                    img2=uploaded_images[2],
                    label1="Broken Tooth",
                    label2="Restored Tooth",
                    width=800,
                    starting_position=50,
                    show_labels=True,
                    make_responsive=True,
                    in_memory=True,
                )

class hamid():

    # # import libraries
    # import cv2
    # import numpy as np
    # import os
    # import json

    def __init__(self) -> None:
        pass

    # function to return key for any value
    def get_key(self, dict, val) -> id:
        '''return key from value'''
        for key, value in dict.items():
            if val == value:
                return key

        return "key doesn't exist"

    # ====================================

    def get_value(self, dict, k) -> str:
        '''return value from key'''
        for key, value in dict.items():
            if k == key:
                return value

        return "value doesn't exist"

    # ==================================================================================

    def read_img(self, path) -> str:
        ''' Reading an image'''

        imageSize = (640, 640, 3)
        # image = cv2.imread(path)
        image = path

        if image.shape != imageSize:
            image = cv2.resize(image, (640, 640))

        return image

    # ==================================================================================

    def read_json_file(self, path) -> dict:
        # categories and images info that reading from json file
        authorized_user_data_master = list()
        with open(path, "r") as auth_json:
            authorized_users_data = json.load(auth_json)

            # categories info that read from json file
            # all of categories data
            catagoriesDict = list(authorized_users_data.values())[2]
            categoriesName = {}

            for i in range(len(catagoriesDict)):
                categoryID = list(catagoriesDict[i].values())[0]
                categoryValue = list(catagoriesDict[i].values())[1]
                categoriesName[categoryID] = categoryValue
            
            print(categoriesName)



            # image info that read from json file
            # all of images data
            imagesDict = list(authorized_users_data.values())[3]   
            imagesName = {}
            
            for i in range(len(imagesDict)):
                imageID = list(imagesDict[i].values())[0]
                imageName = list(imagesDict[i].values())[2]
                imagesName[imageID] = imageName
            
            print(imagesName)

        return categoriesName, imagesName

    # ==================================================================================

    def separate_list_in_pairs(self, input_list) -> list:
        # print(len(input_list))
        return [input_list[i:i + 2] for i in range(0, len(input_list), 2)]

    # ==================================================================================

    def annotations_info(self, path, image_id) -> list:
        lst = []

        with open(path, "r") as auth_json:
            authorized_users_data = json.load(auth_json)
            annotationsList = list(authorized_users_data.values())[4]

            segmentations = {}

            for i in range(len(annotationsList)):
                # all of annotations data
                annotationsDict = annotationsList[i] 

                # image_id
                annotationImageID = list(annotationsDict.values())[1]
                # print(f'annotationImageID is: ', annotationImageID)

                if annotationImageID == image_id:
                    # category_id
                    annotationCategoryID = list(annotationsDict.values())[2]

                    area = list(annotationsDict.values())[4]

                    segmentations = list(annotationsDict.values())[5]
                    # print(segmentations)
                    # segmentations = separate_list_in_pairs(segmentations[0])
                    segmentations = self.separate_list_in_pairs(segmentations)


                    lst.append([annotationCategoryID, segmentations, area])
                    # print(f'lst is: ',lst)

                else:
                    # print('annotationImageID not match with image_id')
                    pass

        return lst

    # ==================================================================================
    def middle_line(self, id, path) -> list:
        '''Returns the list of points below the midline.'''

        lst = []

        with open(path, "r") as auth_json:
            authorized_users_data = json.load(auth_json)
            annotationsList = list(authorized_users_data.values())[4]

            segmentations = {}

            for i in range(len(annotationsList)):

                # all of annotations data
                annotationsDict = annotationsList[i] 

                # image_id
                annotationImageID = list(annotationsDict.values())[1]
                categoryImageID = list(annotationsDict.values())[2]

                

                if annotationImageID == id:
                    if categoryImageID == 1:

                        segmentations = list(annotationsDict.values())[5]
                        
                        # segmentations = separate_list_in_pairs(segmentations)
                        segmentations = self.separate_list_in_pairs(segmentations[0])

                else:
                    # print('annotationImageID not match with image_id')
                    pass
        
        _points = np.array(segmentations, np.int32)

        # Calculate the middle point of the polygon
        middle_point = np.mean(_points, axis=0, dtype=int)

        # Create a list for points below the horizontal line
        points_below_line = []
        
        # Check which points are below the horizontal line
        for point in _points:
            if point[1] > middle_point[1]:
                points_below_line.append(point)


        # Connect and draw the points below the line
        # if len(points_below_line) > 1:
        #     cv2.polylines(image, [np.array(points_below_line)], isClosed=False, color=(0, 0, 255), thickness=2)
    
        return points_below_line

    def intersection_point(self, pts):
        polygon_points = np.array(pts, np.int32).reshape((-1, 1, 2))

        # Find the center of the polygon
        polygon_center = np.mean(polygon_points, axis=0, dtype=np.int32)[0]

        return polygon_center

    def draw_polygon1(self, before_image, annotations_info, categories_name, repairing_status) -> str:
        
        overlay = before_image.copy()
        overlay1 = before_image.copy()
        width, height = 640, 640

        # Polygon corner points coordinates
        # category id, segmentation
        polygonLst = []
        labelLst = []
        intersectionPointLst = []
        for i in range(len(annotations_info)):
            key = annotations_info[i][0]
            value = np.array(annotations_info[i][1], np.int32).reshape((-1, 1, 2))

            labels = self.get_value(categories_name, key)

            intersectionPoint = self.intersection_point(annotations_info[i][1]) 

            polygonLst.append([key, value])   
            labelLst.append(labels) 
            intersectionPointLst.append(intersectionPoint)


        # polygon colors
        gumColor = (255,192,203)
        brokenColor = (255, 0, 0)
        repairingColor = (255,255,100)
        restoredColor = (8, 143, 143)


        # Line thickness of 2 px
        thickness = 2

        # Points of any polygon that lie below the midline
        # damageMiddleLine = middle_line(annotations_info[1][1])
        # toothMiddleLine = middle_line(annotations_info[2][1], overlay1)
        

        # Draw polygons with thickness of 1 px
        isClosed = True
        for i in range(len(annotations_info)):
            if polygonLst[i][0] == 2:
                cv2.polylines(before_image, [polygonLst[i][1]], isClosed, gumColor, thickness)
                cv2.fillPoly(overlay, pts=[polygonLst[i][1]], color=(255, 0, 0))     

            elif polygonLst[i][0] == 1:
                cv2.polylines(before_image, [polygonLst[i][1]], isClosed, brokenColor, thickness) 
                cv2.fillPoly(overlay, pts=[polygonLst[i][1]], color=brokenColor)

            elif polygonLst[i][0] == 3:
                cv2.polylines(before_image, [polygonLst[i][1]], isClosed, repairingColor, thickness)  
                cv2.fillPoly(overlay, pts=[polygonLst[i][1]], color=repairingColor)

            elif polygonLst[i][0] == 4:
                cv2.polylines(before_image, [polygonLst[i][1]], isClosed, restoredColor, thickness) 
                cv2.fillPoly(overlay, pts=[polygonLst[i][1]], color=restoredColor)


            else:
                cv2.polylines(before_image, [polygonLst[i][1]], isClosed, gumColor, thickness)  
                cv2.fillPoly(overlay, pts=[polygonLst[i][1]], color=gumColor) 

            
            # cv2.fillPoly(overlay, pts=[polygonLst[i][1]], color=(255, 0, 0))
        # cv2.fillPoly(overlay, pts=[damagePts], color=(0, 255, 0))
        # cv2.fillPoly(overlay, pts=[toothPts], color=(0, 0, 255))


        # Transparency factor.
        alpha = 0.15  

        # Draw Midline for repairingTooth
        if repairing_status is not None:
            pass
            # st.write(repairing_status)
            # cv2.polylines(before_image, repairing_status, isClosed, damageColor, thickness)                

        # Following line overlays transparent rectangle over the image
        image_new = cv2.addWeighted(overlay, alpha, before_image, 1 - alpha, 0)


        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # org
        org = (150, 50)
        
        # fontScale
        fontScale = 1
 
        # Line thickness of 2 px
        thickness = 1

        # Using cv2.putText() method
        for i in range(len(annotations_info)):
            if polygonLst[i][0] == 2:
                cv2.putText(image_new, labelLst[i], intersectionPointLst[i], font, fontScale, gumColor, thickness, cv2.LINE_AA)

            elif polygonLst[i][0] == 1:
                cv2.putText(image_new, labelLst[i], intersectionPointLst[i], font, fontScale, brokenColor, thickness, cv2.LINE_AA)

            elif polygonLst[i][0] == 3:
                cv2.putText(image_new, labelLst[i], intersectionPointLst[i], font, fontScale, repairingColor, thickness, cv2.LINE_AA)

            elif polygonLst[i][0] == 4:
                cv2.putText(image_new, labelLst[i], intersectionPointLst[i], font, fontScale, restoredColor, thickness, cv2.LINE_AA)

            else:
                cv2.putText(image_new, labelLst[i], intersectionPointLst[i], font, fontScale, gumColor, thickness, cv2.LINE_AA)


        # cv2.fillPoly(before_image, pts=[pts3], color=(0, 0, 255),)
        # print(annotations_info[0][1])
        return image_new


    def put_text(self, ):
        pass
    # ==================================================================================

    def area_compare(self, img_area1, img_area2) -> bool:
        '''get two area from before and after image and compare value.'''
        if img_area1 == img_area2:
            return True
        
        else:
            return False

    # ==================================================================================

    def underline(self, ):
        pass

    # ==================================================================================

    def main(self, image, image_name, status: bool=False, ):


        # path
        # 1- broken tooth
        brokenToothPath = image
        brokenToothName = image_name        
        
        # Annotate Path 
        annotatePath = r"data/train3/_annotations.coco.json"

        # ==========================================================================

        categoriesName, imagesName = self.read_json_file(annotatePath)

        # find key from image name
        damageToothId1 = self.get_key(imagesName, brokenToothName)


        # annotations info that reading from json file
        annotationsInfo1 = self.annotations_info(annotatePath, damageToothId1)

        # read the images
        brokenToothImage = self.read_img(brokenToothPath)

        b = None
        if status:
            repairingID = int(damageToothId1) - 1
            # st.write(repairingID)
            b = self.middle_line(repairingID, annotatePath)
        
        # Displaying the image
        a = self.draw_polygon1(brokenToothImage, annotationsInfo1, categoriesName, b)
        
        

        return a
        



    # if __name__== '__main__':
    #     main()        


