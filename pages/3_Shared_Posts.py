import mysql.connector
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Social Media DBMS Project",
    page_icon="💬",
)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="smdbms"
)
c = mydb.cursor()

def view():
    c.execute('select * from shared_posts')
    return c.fetchall()

def view_user():
    c.execute('select * from users')
    return c.fetchall()
def view_post():
    c.execute('select * from posts')
    return c.fetchall()

def delete_record(Shared_User_ID,Post_id):
    c.execute(f'delete from shared_posts where Post_ID = "{Post_id}" and Shared_User_ID ="{Shared_User_ID}" ')
    mydb.commit()

def update(choice,post_id,Shared_User_ID):
    c.execute(f'update shared_posts SET Post_ID = "{post_id}" where Post_ID = {choice} and Shared_User_ID="{Shared_User_ID}"')
    mydb.commit()
    
def add_data(table_name,Shared_User_ID,Post_ID):
    c.execute(f'INSERT INTO {table_name} (Shared_User_ID,Post_ID) VALUES ("{Shared_User_ID}","{Post_ID}")')
    mydb.commit()

def get_post(post_id,shared_user_id):
    c.execute(f'select * from shared_posts where Post_ID = "{post_id}" and Shared_User_ID="{shared_user_id}"')
    return c.fetchall()  

def create():
    # User_ID = st.text_input("User_ID: ")
    data = view_user()
    # st.dataframe(pd.DataFrame(data, columns = ['User_ID', 'Email_ID', 'Phone_Number', 'Pass_word', 'First_name', 'Last_name','City','PinCode','DOB','Gender','AGE','no_of_friends']))
    user_ids = list(set([i[0] for i in data]))
    Shared_User_ID = st.selectbox('Select the User who wishes to Share the post', user_ids)
    data_ = view_post()
    # st.dataframe(pd.DataFrame(data, columns = ['User_ID', 'Email_ID', 'Phone_Number', 'Pass_word', 'First_name', 'Last_name','City','PinCode','DOB','Gender','AGE','no_of_friends']))
    post_ids = list(set([i[0] for i in data_]))
    Post_ID = st.selectbox('Select the Post which the user wishes to Share', post_ids)
    if st.button("Share Post ?"):
        add_data("shared_posts",Shared_User_ID,Post_ID)
        st.success("Successfully added record!")
        
# def view():
#     c.execute('select * from users')
#     return c.fetchall()

# def delete_record(User_id):
    # c.execute(f'delete from users where User_ID = "{User_id}"')
    
# def update(user_id, updated_email, updated_Phone_Number, updated_First_Name, updated_Last_Name, updated_City,updated_PinCode):
    # c.execute(f'update train SET Email_ID = "{updated_email}", Phone_Number = "{updated_Phone_Number}", First_name = "{updated_First_Name}", Last_name = "{updated_Last_Name}", City = "{updated_City}" , PinCode ="{updated_PinCode}" where User_ID = {user_id}')

def delete():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['Post_ID','Shared_User_ID']))
    post_ids = list(set([i[0] for i in data]))
    Post_ID= st.selectbox('Select the shared Post to be unshared', post_ids)
    shared_user_ids = list(set([i[1] for i in data]))
    Shared_user_ID= st.selectbox('Select the User who wishes The post to be Unshared', shared_user_ids)
    if st.button('Delete Record'):
        delete_record(Shared_user_ID,Post_ID)
        st.success("Deleted!")
        # st.experimental_rerun()
     
# def get_user(user_id):
#     c.execute(f'select * from train where Train_no = "{user_id}"')
#     return c.fetchall()   
        
def edit():
    data = view()
    st.dataframe(pd.DataFrame(data, columns = ['Post_ID','Shared_User_ID']))
    post_ids = list(set([i[0] for i in data]))
    user_ids = list(set([i[1] for i in data]))
    choice = st.selectbox('Select the Post to be Reshared',post_ids)
    choice1 = st.selectbox('Select the user who is involved in the process',user_ids)
    data = get_post(choice,choice1)
    if data:
        data_ = view_post()
    # st.dataframe(pd.DataFrame(data, columns = ['User_ID', 'Email_ID', 'Phone_Number', 'Pass_word', 'First_name', 'Last_name','City','PinCode','DOB','Gender','AGE','no_of_friends']))
        post_ids = [i[0] for i in data_]
        Post_ID = st.selectbox('Select the New Post to be  Reshared', post_ids)
        # updated_Post = st.selectbox("Select the new Post")
        # updated_Phone_Number_str = st.text_input("Enter the New Mobile Number")
        # # updated_Phone_Number = int(updated_Phone_Number_str)
        # updated_First_Name = st.text_input("Enter New First_Name")
        # updated_Last_Name = st.text_input("Enter New Last_Name")
        # updated_City = st.text_input("Enter New City")
        # updated_Pin = st.text_input("Enter New PinCode")
        # updated_PinCode = int(updated_Pin)
        if Post_ID == '':
            Post_ID = data[0][0]
        # if updated_Phone_Number_str == '':
        #     updated_Phone_Number_str = data[0][2]
        # if updated_First_Name == '':
        #     updated_First_Name = data[0][4]
        # if updated_Last_Name == '':
        #     updated_Last_Name = data[0][5]
        # if updated_City == '':
        #     updated_City = data[0][6]
        # if updated_Pin == '':
        #     updated_Pin = data[0][7]
        if st.button("Update"):
            update(choice,Post_ID,choice1)
            st.success("Updated!")
        # st.experimental_rerun()



def main():
    st.title("Shared_Posts Table")
    menu = ["Add", "View", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == 'Add':
        st.subheader("Enter details")
        try:
            create()
        except Exception as e:
            st.error("Error!"+' '+str(e))
    elif choice == 'View':
        st.subheader("Information in Table")
        try:
            data = view()
        except:
            st.error("Error!")
        df = pd.DataFrame(data, columns = ['Post_ID','Shared_User_ID'])
        st.dataframe(df)
    
    elif choice == 'Delete':
        st.subheader('Select row to delete')
        delete()
    elif choice == 'Update':
        st.subheader('Select row to update')
        edit()


# if __name__ == '__main__':
#     db = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = '',
#         database = 'instagram_database'
#     )
#     cursor = db.cursor()

main()

