# import streamlit as st
# from controllers.auth_controller import handle_login

# def render():
#     st.title("Login")

#     with st.form("login_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         submitted = st.form_submit_button("Login")

#         if submitted:
#             if handle_login(username, password):
#                 st.success("Login successful!")
#                 st.rerun()




# views/login.py
import streamlit as st
from controllers.auth_controller import handle_login
def render():
    # Use a custom HTML container for better styling with CSS
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
    st.markdown("<h1>Login to HealthMate</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Welcome back! Please enter your credentials.</p>", unsafe_allow_html=True)
    
    # Use a Streamlit form to group inputs and the button
    with st.form("login_form"):
         username = st.text_input("Username", key="username_input")
         password = st.text_input("Password", type="password", key="password_input")
        
         # The submit button for the form
         submitted = st.form_submit_button("Login")
    
     # Handle the form submission and display feedback
    if submitted:
         if handle_login(username, password):
             st.success("Login successful! Redirecting...")
             # Store the username and login status in the session state
             st.session_state.logged_in = True
             st.session_state.username = username  # This is the added line
             st.session_state.page = "Feedback"
             st.rerun()
         else:
             st.error("Invalid username or password. Please try again.")
 
     # A link to the sign-up page for new users
    st.markdown(
         "<p style='text-align: center; margin-top: 20px;'>Don't have an account? <a href='#'>Sign up here</a></p>",
         unsafe_allow_html=True
     )
    
     # Close the custom HTML container
    st.markdown("</div>", unsafe_allow_html=True)

