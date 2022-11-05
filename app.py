import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Video Games Sales",
                   page_icon=":bar_chart:",
                   layout="wide")


sns.set_style("darkgrid")
st.title("VIDEO_GAMES_SALES VISUALIZATION")
df=pd.read_csv("vgsales.csv")
st.dataframe(df)
st.header("Global Sales")
fig = px.scatter(df, x="Year", y="Global_Sales")
st.plotly_chart(fig)



st.header("Sales In Year")
fig, ax = plt.subplots(1, 1)
sns.countplot(data=df,
              x="Genre",
              order = df["Genre"].value_counts().index,
              palette="Dark2")
plt.xticks(rotation=90)
st.pyplot(fig)


st.header("Counts Of Different Games")

sns.countplot(data=df,
              x="Platform",
              order = df["Platform"].value_counts().index,
              palette="Dark2")
plt.xticks(rotation=90)
st.pyplot(fig)
st.header("CORRELATION ")

from sklearn.preprocessing import LabelEncoder

# Encode selected categorical columns to prepare for heatmap plotting
encoded_df = df.copy()
categ = ["Platform", "Genre", "Publisher"]
encoder = LabelEncoder()
encoded_df[categ] = encoded_df[categ].apply(encoder.fit_transform)
sns.heatmap(encoded_df.corr(),
            cmap="flare",
            annot=True)
st.pyplot(fig)


st.subheader("top sales values of a dataframe")
st.dataframe(df.nlargest(10, "Global_Sales"))
st.subheader('Q: What are the top 5 gaming Genres that are making high sales?')
sales_genre = df.groupby("Genre").agg({"Global_Sales": pd.Series.sum})
data = sales_genre.nlargest(5, "Global_Sales")

st.dataframe(data)


st.subheader('Q: Which Publishers made the most sales?')
sales_publisher = df.groupby("Publisher").agg({"Global_Sales": pd.Series.sum})
data = sales_publisher.nlargest(5, "Global_Sales")

st.dataframe(data)


st.subheader("Q: What PC-FX games were sold?")
st.dataframe(df.query("Platform == 'PCFX'"))
input_col,pie_col=st.columns(2)
pf=df["Global_Sales"]




jf=pf.sort_values(ascending=False).reset_index()
top_n=input_col.text_input("How many of theGlobal Sales would you like to see?",10)
top_n=int(top_n)
jf=jf.head(top_n)
jf=jf.head(top_n)



print(jf)

fig, ax = plt.subplots(1, 1)
sns.countplot(data=jf,
              x=jf["Global_Sales"],

              palette="Dark2")
plt.xticks(rotation=90)
st.pyplot(fig)