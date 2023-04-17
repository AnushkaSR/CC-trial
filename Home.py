import streamlit as st
from PIL import Image

image = Image.open('User-ER-Diagram.png')

st.set_page_config(
    page_title="Social Media DBMS Project",
    page_icon="#️⃣",
)

st.title("SOCIAL MEDIA DATABASE MANAGEMENT APP")
st.subheader("Project done by Anushka Siri Raghunandan(PES1UG20CS073)")

st.sidebar.success("Select the page")

st.header("ER DIAGRAM")
st.image(image,caption="ER Diagram")