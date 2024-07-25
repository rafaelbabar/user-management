import streamlit as st
import pandas as pd
import datetime
#D:\OneDrive\Desktop\Projects>streamlit run login-app-files.py
def login():
    st.title("Login")
    st.write("This app allows you to administer users")
    st.write("Please try it out, remember to click Check User")
    st.write("username = Dave")
    st.write("password = p1")
    enterusername = st.text_input("Please enter username to update system")
    enterpassword = st.text_input("Please enter password", type="password")
    if st.button("Check User"):
        file = open("userlist.csv", "r", encoding="utf-8-sig")
        user_found = False
        for line in file:
            lines = line.strip().split(",")

            username = lines[0]
            password = lines[1]
            if enterusername == username and enterpassword == password:
                with open("userlog.csv", "a", newline='') as file:
                    file.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n")                
                    st.session_state.logged_in = True
                    st.success("Login Successful")
                    user_found = True
                    break
        if not user_found:
            st.error("Invalid username or password")
        file.close()

def dashboard():
    st.write("Welcome Admin")
    if st.button("Sign Out"):
        st.session_state.logged_in = False
    st.title("User Management and Login Record")
    choice = st.sidebar.radio("Please select add or remove",
    [":rainbow[Add]", ":rainbow[Remove]", ":rainbow[View]"])
    if choice == ":rainbow[Add]":
        username = st.text_input("Please enter username to add")
        password = st.text_input("Please enter password", type="password")
        if st.button("Add User"):
            with open("userlist.csv", "a", newline='') as file:
                file.write(username + "," + password + "\n")
    elif choice == ":rainbow[Remove]":
        username = st.text_input("Please enter username to remove")
        if st.button("Remove User"):
            df = pd.read_csv("userlist.csv")
            if username in df["username"].values:
                df = df[df["username"] != username]
                df.to_csv("userlist.csv", index=False)
                st.success(f"User {username} removed successfully.")
            else:
                st.error(f"Username {username} not found in the data.")          
    else:
        df = pd.read_csv("userlist.csv")
        st.dataframe(df)
        df = pd.read_csv("userlog.csv")
        st.dataframe(df)
        
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if st.session_state.logged_in:
    dashboard()
else:
    login()
#Before coding - pip install streamlit
#After coding - Run, cmd browse to file directory
#Then streamlit run nameoffile.py

