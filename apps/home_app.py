import os
import streamlit as st
from hydralit import HydraHeadApp



MENU_LAYOUT = [1,1,1,7,2]

class HomeApp(HydraHeadApp):


    def __init__(self, access_level, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.accessLevel = access_level


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        try:
            
            
            # c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([2, 2, 2, 2, 2, 2, 2, 2])
            # if self.accessLevel == 1:
            #     if c7.button('Creat Account'):
            #         pass

            #     elif c8.button('Login'):
            #         pass

            # else:
            #     c8.button('Logout')



            _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
            # col_logo.image(os.path.join(".","resources","data.png"),width=80,)
            col_text.subheader("When a person needs to fill a tooth and goes to the dentist, an advanced method is used to diagnose and check the condition of the teeth. In this procedure, a special camera, known as an intraoral camera, is placed in the person's mouth. This camera with high accuracy and zooming ability provides the doctor with video images and still images of the teeth and the condition of the mouth.")

            st.markdown('<br><br>',unsafe_allow_html=True)

            # path = os.path.dirname(__file__)
            # path = r'C:\Users\hamidr.bd\Documents\Programming\Python\Jupyter\Projects\8- Dental Scanning\code\Third phase\docs'
            # my_file = path + '\home-video.mp4'
            my_file = r'docs/home-video.mp4'

            c1, c2, c3 = st.columns([2, 3, 2])
            video_file = open(my_file, 'rb')
            with c2:
                if video_file is not None:
                    video_bytes = video_file.read()

                else:
                    st.error('Error details: [Errno 2] No such file or directory', icon="🚨")
                    


                if video_bytes is not None:
                    st.video(video_bytes)
                


            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Cheat Sheet ➡️'):
            #     self.do_redirect('Cheat Sheet')
            # col_logo.image(os.path.join(".","resources","classroom.png"),width=50,)
            col_text.info("Before filling the tooth, the doctor uses an intraoral camera to carefully examine the tooth that needs to be filled. This step is of particular importance because through images and videos, the doctor can see the exact details of the condition of the desired tooth and identify the filling needs well.")

            #The sample content in a sub-section with jump to format.
            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Sequency Denoising ➡️'):
            #     self.do_redirect('Sequency Denoising')
                
            # col_logo.image(os.path.join(".","resources","denoise.png"),width=50,)
            col_text.info("After filling the tooth, the doctor uses the intraoral camera again to take new pictures of the filled tooth. Then, he compares the images before and after filling the tooth. This comparison allows him to properly evaluate the changes and improvements made by dental fillings.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Solar Mach ➡️'):
            #     self.do_redirect('Solar Mach')
            # col_logo.image(os.path.join(".","resources","satellite.png"),width=50,)
            col_text.info("Also, this method allows the doctor to check the alignment of the person's upper and lower teeth. By comparing the images before and after tooth filling, as well as considering the full mouth images, the doctor can accurately assess the match between the teeth and detect any cavities.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Spacy NLP ➡️'):
            #     self.do_redirect('Spacy NLP')
            # col_logo.image(os.path.join(".","resources","belgium.png"),width=50,)
            col_text.info("Finally, this method of images and videos is used as a powerful tool to diagnose, investigate and solve dental problems and provides the doctor with more detailed information about the condition of a person's mouth.")

            # _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # # if col_text.button('Uber Pickups ➡️'):
            # #     self.do_redirect('Uber Pickups')
            # col_logo.image(os.path.join(".","resources","taxi.png"),width=50,)
            # col_text.info("This application is all credit to [demo-uber-nyc-pickups](https://github.com/streamlit/demo-uber-nyc-pickups), this is an example of how quickly an existing application can be wrapped in a HydraHeadAPP class and used in Hydralit.")

        
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))





