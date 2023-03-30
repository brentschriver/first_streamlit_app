import streamlit
import pandas as pd

streamlit.title("Our New Boutique")
streamlit.header("Spring 2023")
streamlit.text("Unisex Top")
streamlit.text("Unisex Bottom")
streamlit.text("Women Top")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Create an interactive list for users to add fruits
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit))
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
