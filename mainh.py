import  streamlit as st

st.title("Welcome to the programing languages training website")

st.header("FULL STACK DEVELOPER IN 200 DAYS")

st.subheader("Hi I am Huma Dawari. I will teach you some programing languages so that you can design a Website or application etc.")

st.header("LEARN HTML AND CSS IN 1-20 DAYS")
st.markdown("The HyperText Markup language or HTML is the standard markup language for document designed to be displayed in a web browser. it defines the content and structure of web content. it is often assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript. And Cascading Style Sheets is a style sheet language used for specifying the presenting and styling of a dcument written in a markup language such as HTML or XML. CSS is a cornerstone technology of the World Wid Web, alongside HTML and JavaScript.   ")


st.header("LEARN JAVASCRIPT IN 21-35 DAYS")
st.markdown("JavaScript, often abbreviated as JS, is a programming language and core technology of the world Wide Web, alongside HTML and CSS. As of 2023,98.7% of websites use JavaScript on the client side for webpage behavior,often incorporating third-party libraries. ")

st.header("LEARN BOOTSTRAP IN 36-46 DAYS")
st.markdown("Bootstrap is a free front-end framework for faster and easier web development. Bootstrap includes HTML and CSS based design templates for typography, forms, buttons, tables, navigation, modals, image carousels and many other, as well as optional JavaScript plugins.")

st.header("LEARN REACT IN 47-60 DAYS")
st.markdown("React is a free and open-source front-end JavaScript library for building user interfaces based on components. It is maintained by Meta and a community of individual developers and companies. React can be used to develop single-page, mobile, or server-rendered application with frameworks like Next.js. ")

st.header("LEARN PYTHON IN 61-90 DAYS")
st.markdown("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readablity with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-ornated and functional programming")

st.header("LEARN DJANGO IN 91-120 DAYS ")
st.markdown("Django is a high-level python web framework that encourage rapid development and clean, pragmatic design. built by experenced developers, it taks care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. it is free and open source. ridiculously fast.")

st.header("LEARN MYSQL IN 121-141 DAYS ")
st.markdown("MYSQL database is a clint/server system that consists of a multithreaded SQL server that support diffirent back ends, several different clint programs and libraries, and administrative tools, and a wide range of application-programming interfaces(APIs).")

st.header("LEARN GIT AND GITHUB IN 142-160 DAYS")
st.markdown("github,Inc. is an AI-powered developer platform that allows developer to create, story, and manage their code. It uses git software, providing the distributed version control of git plus access control, bug tracking software feature requests, task management, continuous integration, and wikis for every project.")

st.header("LEARN REST API IN 161-172 DAYS")
st.markdown("REST is a software architectural style that was created to guide the design and development of the architectural for the world wide web. REST defines a set of constraints for how the architectural of a distributed, internet-scale hypermedia system, such as the web, should behave. ")

st.header("LEARN AWS IN 173-185 DAYS")
st.markdown("Amazon Web Services, Inc. is a subsidiary of amazon that provides on-demand cloud computing platform and APIs to indiviuals, companies, and governments, on metered, pay-as-you-go basis. clients will often use this in combination with autoscaling,")

st.subheader("LEARN REVISE IN 186-200 DAYS ")
st.subheader("START BUILDING PROJICTS ")




st.subheader("Our course will start soon, you can register here")

import pandas as pd

name = st.text_input("Enter your name : ")
fname = st.text_input("Enter your Father name : ")
city = st.text_input("Enter your City name : ")
address = st.text_input("Enter your Address line : ")
phone = st.text_input("Enter your phone number : ")
email = st.text_input("Enter your email address : ")
adr = st.text_input("Enter your Text : ")
classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6))

button = st.button("Done")
if button :
    st.markdown(f"""
    name : {name}
    Father name : {fname}
    City name : {city}
    Address line : {address}
    Phone number : {phone}
    email address : {email}
    class : {classdata}""")



st.markdown(" if you have any questions you can email me ")
st.markdown("humadawari@gmail.com")

