import time
import os
from typing import Dict
import streamlit as st
from hydralit import HydraHeadApp

import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit.components.v1 as components


# from .utils import check_usr_pass
# from .utils import load_lottieurl
# from .utils import check_valid_name
# from .utils import check_valid_email
# from .utils import check_unique_email
# from .utils import check_unique_usr
# from .utils import register_new_usr
# from .utils import check_email_exists
# from .utils import generate_random_passwd
# from .utils import send_passwd_in_email
# from .utils import change_passwd
# from .utils import check_current_passwd
# from .utils import create_connection
# from .utils import create_table
# from .utils import show_user_info

MENU_LAYOUT = [1,1,1,7,2]   



class ProfileApp(HydraHeadApp):
    
    def __init__(self, app, config, authenticator, title = '', **kwargs):
        
        self.app = app
        self.__dict__.update(kwargs)
        self.title = title
        self.config = config
        self.authenticator = authenticator
 

    def run(self) -> None:

        # from .Authenticator.hasher import Hasher
        from .Authenticator.authenticate import Authenticate
        # st.write(st.session_state['authentication_status'])


        # # Loading config file
        # with open('./data/Authenticator_config.yaml') as file:
        #     config = yaml.load(file, Loader=SafeLoader)

        # # Creating the authenticator object
        # authenticator = Authenticate(
        #     config['credentials'],
        #     config['cookie']['name'], 
        #     config['cookie']['key'], 
        #     config['cookie']['expiry_days'],
        #     config['preauthorized']
        # )

        # if 'authentication_status' not in st.session_state:
        #     st.session_state['authentication_status'] = None

        if st.session_state["authentication_status"] is None:
            self.set_access(1, 'guest')

            c1, c2, c3 = st.columns([1, 3, 1])
            tab1, tab2 = c2.tabs(["Login", "Sign up"])
            
            with tab1:
                # creating a login widget
                self.authenticator.login('Login', 'main')
                if st.session_state["authentication_status"] is False:
                    st.error('Username/password is incorrect')
                elif st.session_state["authentication_status"] is None:
                    pass
                    # st.warning('Please enter your username and password')

                # Creating a password reset widget
                # if st.session_state["authentication_status"]:
                #     try:
                #         if authenticator.reset_password(st.session_state["username"], 'Reset password'):
                #             st.success('Password modified successfully')
                #     except Exception as e:
                #         st.error(e)

                # Creating a forgot password widget
                if st.session_state["authentication_status"] is None:
                    if st.button(label="Forget password"):
                        try:
                            username_forgot_pw, email_forgot_password, random_password = self.authenticator.forgot_password('Forgot password')
                            if username_forgot_pw:
                                st.success('New password sent securely')
                                # Random password to be transferred to user securely
                            else:
                                st.error('Username not found')
                        except Exception as e:
                            st.error(e)

            with tab2:
            # Creating a new user registration widget
                try:
                    if self.authenticator.register_user('Register user', preauthorization=False):
                        st.success('User registered successfully')
                except Exception as e:
                    st.error(e)

                # # Creating a forgot username widget
                # try:
                #     username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
                #     if username_forgot_username:
                #         st.success('Username sent securely')
                #         # Username to be transferred to user securely
                #     else:
                #         st.error('Email not found')
                # except Exception as e:
                #     st.error(e)


                # Creating an update user details widget
                if st.session_state["authentication_status"]:
                    try:
                        if self.authenticator.update_user_details(st.session_state["username"], 'Update user details'):
                            st.success('Entries updated successfully')
                    except Exception as e:
                        st.error(e)


        elif st.session_state["authentication_status"]:
            # self.set_access(2, 'user')
            # self.do_redirect()

            # c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([2, 2, 2, 2, 2, 2, 2, 2])
            # pretty_btn = """
            # <style>
            # div[class="row-widget stButton"] > button {
            #     width: 100%;
            # }
            # </style>
            # <br><br>
            # """
            # c6.markdown(pretty_btn, unsafe_allow_html=True)

            # if c7.button('Supports'):
            #     pass


            # if c8.button('LogOut'):
            self.authenticator.logout('Logout', 'main')
            


            # st.write(f'Welcome *{st.session_state["name"]}*')
            # st.title('Some content')
            self.prof(self.config)



        # Saving config file
        # with open('./data/Authenticator_config.yaml', 'w') as file:
        #     yaml.dump(self.config, file, default_flow_style=False)

        with open('data/Authenticator_config.yaml', 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False)









        # st.markdown("<h1 style='text-align: center;'>Profile</h1>", unsafe_allow_html=True)
        
        # st.title("User Profile Page")

    def prof(self, config):
        

        user_access_level, username = self.app.check_access()

        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([2, 2, 2, 2, 2, 2, 2, 2])
        pretty_btn = """
        <style>
        div[class="row-widget stButton"] > button {
            width: 100%;
        }
        </style>
        <br><br>
        """
        c6.markdown(pretty_btn, unsafe_allow_html=True)


                

        # if user_access_level == 1:
        if st.session_state["authentication_status"] is False:
            try:

                st.write('###')

                _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
                col_logo.image(os.path.join(".","resources","profile.png"),width=200,)

                st.markdown('<br><br>', unsafe_allow_html=True)
                
                c1,c2,c3, c4, = st.columns([2, 2, 2, 2])
                # profile_form = c2.form(key="profile_form")

                c1.write(f'name:  ',)
                c3.write(f'last name:  ')

                c1.write('###')
                c3.write('###')

                c1.write(f'userName:  ')
                c3.write(f'age:  ')

                c1.write('###')
                c3.write('###')

                c1.write(f'Email:  ')
                c3.write(f'phone number:')

                c1.write('###')
                c3.write('###')

                # profile_form.form_submit_button('')

            except:
                st.warning('please ...')
     

         # if user_access_level > 1:


        if st.session_state["authentication_status"]:

            try:
                
                # if c6.button('Setting'):
                #     pass

                # if c7.button('Supports'):
                #     pass

                # if c8.button('Logouts'):
                #     pass
                
                # if col_header_text.button(''):
                #     self.do_redirect("https://hotstepper.readthedocs.io/index.html")

                # st.write('###')
                # st.write('###')
                st.write('###')

                _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
                col_logo.image(os.path.join(".","resources","profile.png"),width=200,)

                st.markdown('<br><br>', unsafe_allow_html=True)

                # c1,c2,c3, c4, = st.columns([2, 2, 2, 2])
                # # profile_form = c2.form(key="profile_form")

                # # st.write()
                # name = config['credentials']['usernames'][st.session_state["username"]]['name']

                # # c1.write(f'name:  ',)
                # c1.write(f'name: ')
                # c3.write(f'last name:  ')

                # c1.write('###')
                # c3.write('###')

                # c1.write(f'userName:   ')
                # c3.write(f'age:  ')

                # c1.write('###')
                # c3.write('###')

                # c1.write(f"Email: ")
                # c3.write(f'phone number:')

                # c1.write('###')
                # c3.write('###')

                c1,c2,c3, = st.columns([2,6,2])
                profile_form = c2.form(key="profile_form")

                c11, c22 = profile_form.columns([2, 2])

                c11.info(f'name: \t *{st.session_state["name"]}*')
                c22.info(f"last name: ")

                c11.write('###')
                c22.write('###')

                c11.info(f'userName:  *{st.session_state["username"]}*')
                c22.info(f"age: *{config['credentials']['usernames'][st.session_state['username']]['age']}*")

                c11.write('###')
                c22.write('###')

                c11.info(f"Email:  *{config['credentials']['usernames'][st.session_state['username']]['email']}*")
                c22.info(f"phone name: *{config['credentials']['usernames'][st.session_state['username']]['phoneNumber']}*")

                c11.write('###')
                c22.write('###')

                profile_form.form_submit_button('Edit Profile', disabled=True)

                

                _,_,col_logo, col_text, col_btn = st.columns(MENU_LAYOUT)
                # if col_text.button('Solar Mach ➡️'):
                #     self.do_redirect('Solar Mach')
                # col_logo.button('Broken Tooth',)
                # col_text.button('restored Tooth')

                col_text.write('###')
                col_text.write('###')
                col_text.write('###')
                col_text.write('###')
                col_text.write('###')

                col_header_logo_left_far, col_header_logo_left,col_header_text,col_header_logo_right,col_header_logo_right_far = st.columns([1,2,2,2,1])
                col_header_logo_left.button('Broken Tooth')
                col_header_text.button('repairing tooth')
                col_header_logo_right.button('restored Tooth')


            
            except Exception as e:
                st.image(os.path.join(".","resources","failure.png"),width=100,)
                st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
                st.error('Error details: {}'.format(e))

                

    def edit_profile(self):
        user_access_level, username = self.app.check_access()
        st.write(user_access_level)
        st.write(username)

        st.success("Profile updated successfully!")




