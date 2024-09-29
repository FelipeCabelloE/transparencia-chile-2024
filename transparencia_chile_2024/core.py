import pandas as pd
import streamlit as st

st.title("Denuncias")


DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load data."""
    return pd.read_csv("data/processed/denuncias.csv")


# Create a text element and let the reader know the data is loading.
data_load_state = st.text("Loading data...")
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")


st.subheader("Denuncias por año")

st.bar_chart(data.groupby(["agno"]).size())

if st.checkbox("Mostrar los datos?"):
    st.subheader("Denuncias.csv")
    st.write(data)
