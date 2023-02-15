import seaborn as sns
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("athlete_events.csv")

st.set_page_config(layout='wide')
st.title("Olympic Dataset history")
st.subheader("Muhammad Jawwad Shah")


all_city = sorted(data['City'].unique())
col1, col2=st.columns(2)
selected_city=col1.selectbox("Select your City",all_city)
Subset_city=data[data['City']==selected_city]
st.dataframe(Subset_city)

col3,col4,col5,col6=st.columns(4)

#total Particpants 
participants=data['Name'].nunique()
col3.metric("Total Participants",participants)

#total Gold
Gold_Medal=data[data['Medal']=='Gold']
gm=Gold_Medal["Medal"].count()
col4.metric("Total Gold Medal",gm)

#total Silver
Silver_Medal=data[data['Medal']=='Silver']
sm=Silver_Medal["Medal"].count()
col5.metric("Total Silver Medal",sm)

#total Bronxe
Bronze_Medal=data[data['Medal']=='Bronze']
bm=Bronze_Medal["Medal"].count()
col6.metric("Total Bronze Medal",bm)

col7,col8,col9=st.columns(3)


#Line chart
without_no_medal=data[data['Medal']!='No_Medal']
medals_per_year = without_no_medal.groupby(["Year"])['Medal'].count()
col7.line_chart(medals_per_year)

#barchart 
#without No Medal
without_no_medal=data[data['Medal']!='No_Medal']
medals_per_athlete_name = without_no_medal.groupby("Name")["Medal"].count().reset_index()
medals_per_athlete_name=medals_per_athlete_name.sort_values("Medal", ascending=False)
col8.bar_chart(data=medals_per_athlete_name.head(5),x="Medal", y="Name")
col9.table(medals_per_athlete_name.head(5))

col10,col11,col12=st.columns(3)
#Piecahrt
Gender_medal=data[data['Medal']!= "No_Medal"]
gender=Gender_medal.groupby(['Sex','Medal'])['Medal'].count()
colors = sns.color_palette('pastel')[0:5]
fig=plt.pie(gender, labels = gender.index,autopct='%.0f%%')
st.set_option('deprecation.showPyplotGlobalUse', False) #colors = 'colors'
col11.pyplot()

#Histogram
fig=sns.histplot(data=without_no_medal,x="Year", bins=10)
col10.pyplot()

#season_plot
season_medal=without_no_medal.groupby('Season')['Medal'].count()
plt.bar(season_medal.index,season_medal.values,color=['green'])
plt.ylabel("No of Medal")
col12.pyplot()

#st.selectbox()
#option = st.selectbox(
 #   'How would you like to be contacted?',
  #  ('Email', 'Home phone', 'Mobile phone'))
#st.write('You selected:', option)
