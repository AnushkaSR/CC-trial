import mysql.connector
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Function",
    page_icon="👤",
)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="smdbms"
)
c = mydb.cursor()

menu = ["No. of comments per post","No. of posts per user"]
st.header("Functions")
op = st.selectbox("Function to be executed:",menu)

if op=="No. of comments per post":
    st.write("Display Number of comments for all posts")
    c.execute("SELECT POST_ID,NOC(POST_ID) FROM POSTS ORDER BY POST_ID ASC")
    df = pd.DataFrame(c.fetchall(), columns=["POST_ID","No. of Comments"])
    st.dataframe(df)

else:
    st.write("Display Number of Posts by each user")
    c.execute("SELECT DISTINCT POSTED_USER_ID,NOP(POSTED_USER_ID) FROM POSTS ORDER BY POSTED_USER_ID")
    df = pd.DataFrame(c.fetchall(), columns=["POSTED_USER_ID","No. of Posts"])
    st.dataframe(df)