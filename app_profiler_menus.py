import streamlit as st
import pandas as pd
import numpy as np
from urllib.parse import quote
from scholarly import scholarly

# Set page title
st.set_page_config(page_title="Cameron Green", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "Contact"],
)

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Cameron Green"
    field = "Spatial Data Infrastructure (SDI) Engineer"
    company = "Riskscape (PTY) Ltd"

    # Display basic profile information
    st.write(f"**{name}**")
    st.write(f"{field}")
    st.markdown(
        f'<a href="https://www.riskscape.pro/" target="_blank">{company}</a>',
        unsafe_allow_html=True
    )
    
    st.image(
    r"C:\Users\cameron.green\OneDrive - Riskscape\Pictures\programming-world-map-on.jpg"
)

elif menu == "Publications":
    st.title("Publications")
    st.write("**This is a live web scrape of all publications, please allow some time for the scraping to complete.**")

    # Search your Google Scholar profile by user ID (a part of your profile link)
    author = scholarly.search_author_id("EmcpSGoAAAAJ")  # Use your actual ID
    author = scholarly.fill(author, sections=['publications'])

    # Display publications
    for pub in author['publications'][:10]:  # Show top 10 or more if needed
        pub_filled = scholarly.fill(pub)
        title = pub_filled.get('bib', {}).get('title', 'No title')
        year = pub_filled.get('bib', {}).get('pub_year', 'Unknown year')
        st.markdown(f"•{title} - ({year})")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)
        # Add widget to filter by Energy levels
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)

    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    # Define contact details
    email = "cameron.green@riskscape.pro"
    linkedin = "https://www.linkedin.com/in/cameronlgreen/"

    # Display LinkedIn as a clickable link
    st.markdown(
        f'<a href="{linkedin}" target="_blank">LinkedIn</a>',
        unsafe_allow_html=True
    )

    # Prepare subject and body (URL encoded)
    subject = quote("Inquiry about your professional services")
    body = quote("Hello,\n\nI would like to set up a meeting to discuss future projects")

    # Display mailto link properly
    st.markdown(
        f'<a href="mailto:{email}?subject={subject}&body={body}">Email me</a>',
        unsafe_allow_html=True
    )