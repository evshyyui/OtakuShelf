import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="OtakuShelf", layout="wide")

if "library" not in st.session_state:
    st.session_state.library = pd.DataFrame(columns=["Title", "Type", "Genre", "Status", "Chapter", "Rating", "Start Date", "Review"])
# sidebar
st.sidebar.title("OtakuShelf")
page = st.sidebar.radio("Menu", ["Home", "Add Entry", "My Library", "Statistics", "About"])

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
        if not title:
            st.error("Please enter a title!")
        else:
            new_entry = {
                "Title": title,
                "Type": series_type,
                "Genre": ", ".join(genre),
                "Status": status,
                "Chapter": chapter,
                "Rating": rating,
                "Start Date": start_date,
                "Review": review
            }
            st.session_state.library = pd.concat([st.session_state.library, pd.DataFrame([new_entry])], ignore_index=True)
            st.success(f"Added **{title}** to your libarry!")

# library
elif page == "My Library":

    st.header("My Reading Library")
    if st.session_state.library.empty:
        st.info("Your library is empty. Add some series first!")
    else:
        st.dataframe(st.session_state.library)

    with st.expander("Library Tips"):
        st.write("Track chapters to stay updated with releases and rate series after finishing.")

# statistics
elif page == "Statistics":
    st.header("Reading Statistics")

    total_series = len(st.session_state.library)
    completed = len(st.session_state.library[st.session_state.library["Status"] == "Completed"])
    reading_now = len(st.session_state.library[st.session_state.library["Status"] == "Reading"])

    st.metric("Total Series", total_series)
    st.metric("Completed", completed)
    st.metric("Currently Reading", reading_now)

    # progress bar based on completed total
    progress = int((completed / total_series) * 100) if total_series > 0 else 0
    st.progress(progress)

    #rating chart
    if not st.session_state.library.empty:
        chart_data = st.session_state.library[["Title", "Rating"]].set_index("Title")
        st.bar_chart(chart_data)
    
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
