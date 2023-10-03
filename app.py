from hydralit import HydraApp
import hydralit_components as hc
import apps
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import os

from github import Github



#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='Dental scanning',page_icon="🐙",layout='wide',initial_sidebar_state='auto', )

if __name__ == '__main__':
    

    #---ONLY HERE TO SHOW OPTIONS WITH HYDRALIT - NOT REQUIRED, use Hydralit constructor parameters.
    # st.write('Some options to change the way our Hydralit application looks and feels')
    c1,c2,c3,c4,_ = st.columns([2,2,2,2,8])
    # hydralit_navbar = c1.checkbox('Use Hydralit Navbar',True)
    # sticky_navbar = c2.checkbox('Use Sticky Navbar',False)
    # animate_navbar = c3.checkbox('Use Animated Navbar',True)
    # hide_st = c4.checkbox('Hide Streamlit Markers',True)

    hydralit_navbar = True
    sticky_navbar = True
    animate_navbar = True
    hide_st = True

    over_theme = {'txc_inactive': '#FFFFFF'}
    #this is the host application, we add children to it and that's it!
    app = HydraApp(
        title='Dental scanning',
        favicon="🐙",
        # hide_streamlit_markers=hide_st,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        # use_banner_images=["./resources/hydra.png",None,{'header':"<h1 style='text-align:center;padding: 0px 0px;color:grey;font-size:200%;'>Dental scanning demo.</h1><br>"},None,"./resources/lock.png"], 
        use_banner_images=[None,{'header':"<h1 style='text-align:center;padding: 0px 0px;color:grey;font-size:200%;'>Dental Scanning demo</h1><br>"},None,],
        banner_spacing=[5,30,60,30,5],
        use_navbar=hydralit_navbar, 
        navbar_sticky=sticky_navbar,
        navbar_animation=animate_navbar,
        navbar_theme=over_theme
    )

    user_access_level, username = app.check_access()

        # apps.Authenticate() 

    # Loading config file
    with open('./data/Authenticator_config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)


    # Creating the authenticator object
    authenticator = apps.Authenticate(
        config['credentials'],
        config['cookie']['name'], 
        config['cookie']['key'], 
        config['cookie']['expiry_days'],
        config['preauthorized']
        )

    st.write("st.secrets is:")
    st.write(st.secrets[passwords])

    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(user_access_level, title='Home'), is_home=True)

    #add all your application classes here
    app.add_app("AI Predict", icon="🤖", app=apps.PredictApp(title="AI Predict")) 
    app.add_app("About Us", icon="ℹ️", app=apps.AboutUs(title="About Me"))

    #we have added a sign-up app to demonstrate the ability to run an unsecure app
    #only 1 unsecure app is allowed
    # app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    # app.add_app("profile", icon="📤", app=apps.LoginApp(title='Login'), is_login=True)

    # 
    app.add_app("profile", icon="🙋", app=apps.ProfileApp(app, config, authenticator, title='Login'))



     

    #specify a custom loading app for a custom transition between apps, this includes a nice custom spinner
    # app.add_loader_app(apps.MyLoadingApp(delay=0))

    #we can inject a method to be called everytime a user logs out
    #---------------------------------------------------------------------
    # @app.logout_callback
    # def mylogout_cb():
    #     print('I was called from Hydralit at logout!')
    #---------------------------------------------------------------------

    #we can inject a method to be called everytime a user logs in
    #---------------------------------------------------------------------
    # @app.login_callback
    # def mylogin_cb():
    #     print('I was called from Hydralit at login!')
    #---------------------------------------------------------------------

    #if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    app.enable_guest_access()


    
    
    

    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()


    # if 'authentication_status' in st.session_state:
    #         st.header(dict(st.session_state))

    # if st.session_state['authentication_status'] is None:
    #     st.header("hamidrezabad badr.   ")

    # if st.session_state['authentication_status'] :
    #     st.header("badr.")

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    if st.session_state['authentication_status']:
    # if user_access_level > 1:
        complex_nav = {
            'Home': ['Home'],
            'AI Predict': ['AI Predict'],
            'NLP': ["About Us"],
            'profile': ['profile']
        }

    elif st.session_state['authentication_status'] is None:
    # elif user_access_level == 1:
        complex_nav = {
            'Home': ['Home'],
            # 'ََAI Predict': ['ََAI Predict'],
            'NLP': ["About Us"],
            'profile': ['profile']
        }
    else:
        complex_nav = {
            'Home': ['Home'],
        }

    # if st.session_state["authentication_status"]:
    #     print('hamidreza')

  
    #and finally just the entire app and all the children.
    app.run(complex_nav)


    #print user movements and current login details used by Hydralit
    #---------------------------------------------------------------------
    # user_access_level, username = app.check_access()
    # prev_app, curr_app = app.get_nav_transition()
    # print(prev_app,'- >', curr_app)
    # print(int(user_access_level),'- >', username)
    # print('Other Nav after: ',app.session_state.other_nav_app)
    #---------------------------------------------------------------------

