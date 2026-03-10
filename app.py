import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="OtakuShelf", layout="wide")

# sidebar
st.sidebar.title("OtakuShelf")
page = st.sidebar.radio("Menu", ["Home", "Add Entry", "My LIbrary", "Statistics", "About"])

# home
if page == "Home":

    st.title("📚 OtakuShelf")
    st.header("Your Manga / Manhwa / Manhua Tracker")
    st.subheader("Welcome!")
    st.write("Track what you're currently reading, rate your favorites, and monitor your reading progress.")
    st.info("Supports Manga, Manhwa, and Manhua tracking.")

# add entry
elif page == "Add Entry":

    st.header("Add a Series")
    title = st.text_input("Title")
    genre = st.multiselect("Genre", ["Action", "Romance", "Fantasy", "Comedy", "Drama", "Horror", "Slice of Life", "Adventure"])
    series_type = st.selectbox("Series Type", ["Manga", "Manhwa", "Manhua"])
    status = st.radio("Reading Status", ["Reading", "Completed", "Plan To Read", "Dropped"])
    chapter = st.number_input("Current Chapter", 0, 5000)
    rating = st.slider("Your Rating", 1, 10)
    start_date = st.date_input("Start Date", date.today())
    review = st.text_area("Personal Notes / Review")

    if st.button("Add to Library"):
        st.success("Entry added to libarry!")

# library
elif page == "My Library":

    st.header("My Reading Library")
    sample_data = pd.DataFrame({
        "Title": ["Kaya-chan wa Kowakunai", "The Greatest Estate Developer", "Tamen De Gushi"],
        "Type": ["Manga", "Manhwa", "Manhua"],
        "Status": ["Reading", "Completed", "Reading"],
        "Rating": [9, 10, 9]
    })
    st.dataframe(sample_data)

    with st.expander("View Library Tips"):
        st.write("Track chapters to stay updated with releases.")

# statistics
elif page == "Statistics":

    st.header("Reading Statistics")
    st.metric("Total Series", 12)
    st.metric("Completed", 5)
    st.metric("Currently Reading", 4)
    st.progress(60)
    chart_data = pd.DataFrame({
        "Series": ["Kaya-chan", "Estate Developer", "Tamen De Gushi"],
        "Rating": [9, 10, 9]
    })
    st.bar_chart(chart_data.set_index("Series"))
    
# about
elif page == "About":

    st.header("About This App")
    st.write("""
    **App Name:** OtakuShelf
    **Use Case:**
    This app allows users to track manga, manhwa, and manhua they are reading.
    **Target Users:**
    Manga readers and webcomic fans who want to manage their reading list.
             
    **Inputs Collected:**
    - Title
    - Type of Series
    - Genre
    - Reading status
    - Current Chapter
    - Rating
    - Start date
    - Reviews
             
    **Outputs Displayed:**
    - Library table
    - Reading statistics
""")
