"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('https://raw.githubusercontent.com/TEAMCBB1/streamlit/main/movies.csv')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Solution Overview", "Statistics","Meet the team", "About us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("We employed two methods of building recommmendation system:")
        st.markdown('1. Content-based filtering')
        st.markdown("Using the selected movie as a baseline, the Content-Based Recommendation system computes similarity across movies based on movie genres. We need the title of the movie as input for this sort of movie recommendation system, however our sim matrix is based on the index of each movie. To construct this, we must translate the movie title into the movie index and the movie index into the movie title. Let's write functions to control those functions.")
        st.markdown('2. Collaborative filtering')
        st.markdown("Collaborative approaches for recommender systems are ways that provide new recommendations exclusively based on prior interactions recorded between users and products. These approaches, unlike their content-based cousins, do not require item meta-data. This reduces their memory requirements, which is a significant benefit given the size of our dataset.")
        st.markdown("Collaborative filtering was our top performing approach for a movie recommender system. We combined it with our top performing model, the SVD model.")
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    #newplot

    if page_selection == "Statistics":
        st.title("Statistics")
        graphs = [ "Most Popular movie Genres", "Number of Ratings per Director","Genre with highest released movies", "Genre Popularity", "Pie Chart of genre distribution", "Ratings Distribution"]
        graphs_choice = st.selectbox(
                "Select a graph", graphs)
        if graphs_choice == "Most Popular movie Genres":
                    st.image("resources\imgs\graph3.png")
                    st.markdown(" Observation:Drama is the most commonly occurring genre with almost half the movies identifying itself as a drama film. The second one Comedy followed by Thriller, Romance, Action, Horror, Documentary, Crime, Adventure, Science Fiction, Children, Animation, Mystery and Fantasy. IMAX is the least common genre as it is the most expensive so fewer people watch it, it is also only available at the cinema and not streaming platforms such as Netflix.")
        elif graphs_choice == "Number of Ratings per Director":
                    st.image("resources\imgs\graph4.png")
                    st.markdown("Observation: Quentin Tarantino, in full Quentin Jerome Tarantino is an american director and screenwriter whose films are noted for their stylized violence, razor-sharp dialogue, and fascination with film and pop culture.and he believes that crime can make a movie pop.Tarantino's films often feature graphic violence, a tendency which has sometimes been criticized. ")
        elif graphs_choice == "Genre with highest released movies":
                    st.image("resources\imgs\graph5.png")
                    st.markdown("Observation: Dramas are most in demand when the  movie is released and have the most viewers, so the movie is released the most. This simply means that you can win in this genre and  usually not lose. ")
        elif graphs_choice == "Genre Popularity":
                    st.image("resources\imgs\graph6.png")
                    st.markdown("Observation: This shows that the drama  is the most trending of what we see across the dataset. It's definitely the trendiest and most highly rated genre because it's the most watched and the most talked about genre.")
        elif graphs_choice == "Pie Chart of genre distribution":
                    st.image("resources\imgs\graph7.png")
                    st.markdown("Observation: This graph shows the percentage of each genre in the dataset, as you can see that the drama is 25%. This allows us to conclude that drama is the most public genre of all. There is no genre that gets a drama rating above 25%.")
        elif graphs_choice == "Ratings Distribution":
                    st.image("resources\imgs\plot.png")
                    st.markdown("Observation: rating number 4 is the highest and the lowest is rating number 1.")        

    # Building out the "about us" page
    if page_selection == "Meet the team":
        left_column, right_column = st.columns(2)
        with left_column:
            st.header(" Meet our team")
            st.write("##")
            with right_column:
                img = Image.open("resources\imgs\lahli.jpeg")
                st.image(img)
            st.write(
				"""
				Malahlane Magdaline Komane - Software Engineer

                komanemalahlane@gmail.com
                """)
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            with right_column:
                img = Image.open("resources\imgs\pic2.jpeg")
                st.image(img)
            st.write(
				"""
				Malose Tshepiso Puka - Data scientist

                malosetshephisopuka@gmail.com
                """)
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            with right_column:
                img = Image.open("resources\imgs\pic1.jpeg")
                st.image(img)
            st.write(
				"""    
				Nokubongwa Ndlela - Data Analyst

                buhlebayeni04@gmail.com
				""")

     
    if page_selection == "About us": 
        st.subheader("Blue Sky.")
		#Company logo
        st.image('resources/imgs/logo.png')
        st.markdown("""
		Blue sky. focuses on Information Technology Services We take data and organize it such that it makes sense for both corporate and individual users. We also use machine learning technologies to construct and train models capable of providing data solutions.

		
		Our team of outstanding data scientists works relentlessly to make your and your customers' lives easier.
		"""
		)

        st.markdown(""" 
		For more info:

		email: info@bluesky.co.za
        """) 
        st.markdown(""" 
        contact: 011 456 5688
		""") 

        # #creating a contact
        with st.container():
            st.write("---")
            st.header(":mailbox_with_mail: Get In Touch With us!")
            st.write("##")
            
            contact_form = """"
			<form action="https://formsubmit.co/komanemalahlane@gmail.com" method="POST">
	 			<input type="hidden" name="_captcha" value="false">
     			<input type="text" name="name" placeholder="your name" required>
     			<input type="email" name="email" placeholder="your email" required>
	 			<textarea name="message" placeholder="your message"></textarea>
     			<button type="submit">Send</button>
			</form>
			"""
            
        st.markdown(contact_form, unsafe_allow_html=True)
        # Use local CSS
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("style/style.css")

        with st.container():
            st.header(" :round_pushpin: Find us here")
            st.write("##")
            st.write(
				"""
				Office 102, Thuso house, 100 jorissen str, Braamfontein, 
				Johannesburg, 2001
				""")

if __name__ == '__main__':
    main()
