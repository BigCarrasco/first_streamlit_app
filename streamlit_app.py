import streamlit
import pandas

streamlit.title('My parents New Healthy diner')
streamlit.header('Breakfast Favorites Menu')

streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smothie')
streamlit.text('🥣 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#toma en una variable, el csv leido por pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#establece como indices las frutas
my_fruit_list = my_fruit_list.set_index('Fruit')

#seleccionador de las frutas atraves del index
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the data in the page
streamlit.dataframe(my_fruit_list)

  # https://firstappapp-ymce4dyf6hir7pa2zz9ikb.streamlit.app/
 
