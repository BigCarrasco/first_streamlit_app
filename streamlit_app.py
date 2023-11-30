import streamlit
import pandas, requests, snowflake.connector

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
streamlit.dataframe(fruits_to_show)

####### lesson 9 #######
streamlit.header('Fuit advice header')
fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#se comentaron las linea que tenia la respuesta en crudo y sin normalizar
###streamlit.text(fruityvice_response) 
###streamlit.text(fruityvice_response.json()) #just write the data on screen

#creacion de la variable para la normalizacion de la vista del json con pandas
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#exposicion por streamlit la variable normalizada
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit list contains")
streamlit.dataframe(my_data_row)

  # https://firstappapp-ymce4dyf6hir7pa2zz9ikb.streamlit.app/
 
