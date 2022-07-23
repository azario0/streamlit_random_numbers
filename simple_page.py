import streamlit as st
from numpy import random



#parameters of the page
st.set_page_config(page_title="random number", layout="wide")

st.title('Welcome to my streamlit lab !')
#this would print a straight line to separate divs
st.write("---")
st.header("This is a random number with the function random")
#generat random number
x = random.randint(0,5)


st.write("This is a random number generated from 0 to 5 : "+str(x))
st.write("And this is the code used to generate the random number : ")
code="""
from numpy import random
x = random.randint(0,5)"""
st.code(code,language='python')



st.write("---")

st.header("This is a 1D array of random numbers between 0 and 4 and it has 50 elements : ")
#to generate random numbers from 0 to 4 , and it would generate 50 numbers
x=random.randint(0,5,50)


randc1,randc2=st.columns([2,5])
randc1.subheader("This is the array .")
randc1.write(x)
randc2.subheader("This is the line chart of the array .")
randc2.line_chart(x)

with randc1:
    code = """
#this is the code wroten to generate the array :
from numpy import random
x=random.randint(0,5,50)
#This is the code wroten to display the array :
randc1,randc2=st.columns([2,5])
randc1.subheader("This is the array .")
randc1.write(x)
    """
    st.code(code,language='python')


with randc2:
    if st.button('Change the numbers !'):
        x=random.randint(0,5,50)
    code = """
#I've used the same generated array with the code on the left .
#This is how i've displayed that chart :
randc2.subheader("This is the line chart of the array .")
randc2.line_chart(x)
#This is the code wroten to change the numbers !
if st.button('Change the numbers !'):
    x=random.randint(0,5,50)
#Both the chart and the array would be updated !
#Because i'm modifying the x value that's used on both displays .
    """
    st.code(code,language='python')


st.write('---')


st.header("And now let's make a 2D array")





rows = st.slider('Select the number of the rows :', 2, 15, 5)
columns = st.slider('Select the number of the columns :', 2, 15, 5)

z=random.randint(0,6,size=(rows,columns))
#To change the numbers
if st.button('Change the numbers in both rows and colums !'):
    z=random.randint(0,6,size=(rows,columns))




t1,t2=st.columns([5,8])
t2.subheader("This is the bar chart of the 2D array : ")
t1.subheader("This is the 2D array of random numbers : ")
with t1:
    st.write(z)
    code="""
#The code used to generate those random numbers and put them into
#a 2D array is the following :
z=random.randint(0,6,size=(5,3))
#The code used to make that button and to regenerate another random
#Numbers is the following
if st.button('Change the numbers in both rows and colums !'):
    z=random.randint(0,6,size=(5,3))
#As you can see it's very easy and effective .
#Thanks to keep reading or testing !
"""
    st.code(code,language='python')
with t2:
    st.bar_chart(z)
    code="""
#The code used to display that chart is the following
st.bar_chart(z)
#The code used to enter the number of rows and columns is the following :
rows = st.slider('Select the number of the rows :', 2, 15, 5)
columns = st.slider('Select the number of the columns :', 2, 15, 5)
    """
    st.code(code,language='python')

st.write("---")
