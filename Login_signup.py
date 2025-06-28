import streamlit as st
import snowflake.connector
import pandas as pd
conn = snowflake.connector.connect(
    user='PRA123',
    password='787244@Ps',
    
    account='nw95332.central-india.azure',
    database='CHANDIGARH_UNIVERSITY'

)
student_details_query = "select phone_number, email_id, password from student_details;"
student_details =pd.read_sql(student_details_query,conn)
student_details = student_details.applymap(lambda x: x.lower() if isinstance(x, str) else x)
snowflake_email =[item.lower() for item in  student_details['EMAIL_ID'] ]
snowflake_phone =[item for item in  student_details['PHONE_NUMBER'] ]
snowflake_password =[item.lower() for item in student_details['PASSWORD']]


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'login' 

def login():
    st.title("Login")

    with st.form(key='login_form'):
        username = st.text_input("Username",placeholder="Enter your email id")
        password = st.text_input("Password", type="password",placeholder="Enter your Password")
        login_submit = st.form_submit_button(label='Login')

    if login_submit:
        if username=='':
            st.error("Enter your username name")
        elif password=='':
            st.error("Enter your Password name")
        else:
            if password in snowflake_password and username in snowflake_email:
                st.success("Successfully logged in")
                st.sidebar.write(f"Welcome {username}")
                
            else:
                st.warning("Invalid Username and Password")

    st.button("Go to Signup", on_click=lambda: switch_view('signup'))

def signup():
    st.title("Signup")

    with st.form(key='signup_form'):
        fname = st.text_input("First Name",placeholder="Enter First Name")
        lname = st.text_input("Last Name",placeholder="Enter Last Name")
        emailid = st.text_input("Email Address",placeholder="Enter Email id")
        phone_no = st.text_input("Phone Number",placeholder="Enter Phone")
        new_password = st.text_input("New Password", type="password",placeholder="Enter Pasword")
        confirm_pass = st.text_input("Confirm Password", type="password",placeholder="Confirm your")
        signup_submit = st.form_submit_button(label='Signup')

    if signup_submit:
        if fname =='':
            st.error("Enter First Name")
        elif lname=='':
            st.error("Enter last name")
        elif emailid=='':
            st.error("Enter valid email ")
        elif phone_no=='':
            st.error("Enter valid phone numner ")
        elif new_password=='':
            st.error("Enter Password")
        elif  new_password !=confirm_pass:
            st.error("Check Password and Confirm password")
        else:
            

            
            
            

            if student_details.empty ==False:

                if emailid.lower() in  snowflake_email or phone_no in snowflake_phone:
                    st.warning("User Already Registered")
                else:
                    query  =f"""INSERT INTO  student_details (first_name, last_name, email_id, phone_number, password)
                    VALUES ('{fname}', '{lname}', '{emailid}', '{phone_no}', '{new_password}');
                    """

                    try:
                        response =pd.read_sql(query,conn)
                        
                        print("inserted successfully")
                        st.success("Signup successfull!")
                    except Exception as e:
                  
                  
                        st.error(e)
            else:
                query  =f"""INSERT INTO  student_details (first_name, last_name, email_id, phone_number, password)
                    VALUES ('{fname}', '{lname}', '{emailid}', '{phone_no}', '{new_password}');
                    """

                try:
                    response =pd.read_sql(query,conn)
                   
                    print("inserted successfully")
                    st.success("Signup successfull!")
                except Exception as e:
                
                
                    st.error(e)


    st.button("Go to Login", on_click=lambda: switch_view('login'))
    

def switch_view(view_name):
    st.session_state.current_view = view_name

def home():
    st.title("Home")
    st.write("Welcome to the Home Page!")
    st.button("Logout", on_click=lambda: logout())

def logout():
    st.session_state.logged_in = False
    st.session_state.current_view = 'login'

if st.session_state.logged_in:
    home()
elif st.session_state.current_view == 'login':
    login()
elif st.session_state.current_view == 'signup':
    signup()
