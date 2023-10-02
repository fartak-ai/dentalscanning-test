import os
import streamlit as st
from hydralit import HydraHeadApp



MENU_LAYOUT = [1,1,1,7,2]

class AboutUs(HydraHeadApp):


    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        try:
            st.markdown("<br></br>",unsafe_allow_html=True)    

                    
            c1,c2,c3, = st.columns([2,6,2])
            profile_form = c2.form(key="profile_form")

            profile_form.header('Request for consult', )

            c11, c22 = profile_form.columns([2, 2])

            c11.text_input(label='', placeholder='Enter your Name.')
            c22.text_input(label='', placeholder='Enter your Email Address.')

            c11.text_input(label='', placeholder='Enter your Phone Number.')
            c22.text_input(label='', placeholder='Enter Subject.')

            profile_form.text_area(label='', placeholder='Description', )

            profile_form.form_submit_button('Send', use_container_width=True)
            


            st.write('###')
            st.write('###')
            st.write('###')

            st.header("Team Info:")

            st.markdown('<br><br>',unsafe_allow_html=True)


            _,_,col_logo, col_text, col_btn = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","profile.png"),width=60,)
            col_text.info("")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","profile.png"),width=60,)
            col_text.info("")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","profile.png"),width=60)
            col_text.info("")


            

            

                     
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))





