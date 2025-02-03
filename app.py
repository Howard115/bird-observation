import streamlit as st
import pandas as pd
from get_user_location import get_user_location
from ebird.api import get_nearby_observations
from urllib.parse import quote
from dotenv import load_dotenv
import os
from fetch_img import fetch_img

load_dotenv()

# Initialize session state for bird observations
if 'nearby_bird_observations' not in st.session_state:
    user_location = get_user_location()
    records = get_nearby_observations(
        os.getenv('EBIRD_API_KEY'), 
        user_location['latitude'], 
        user_location['longitude'], 
        dist=15, 
        back=7,
        locale='zh',
        hotspot=True,
        max_results=100
    )
    st.session_state['nearby_bird_observations'] = records

# Load and process the data

def load_data():
    """Load and process bird observation data into DataFrames"""
    df = pd.DataFrame(st.session_state['nearby_bird_observations'])
    location_species = df.groupby('locName')['comName'].agg(
        lambda x: ', '.join(sorted(set(x)))
    ).reset_index()
    location_species.columns = ['Location', 'Species Present']
    return df, location_species

# Create the Streamlit app
st.title('Bird Observation Analysis')

# Initialize session state variables
if not all(key in st.session_state for key in ['df', 'location_summary']):
    st.session_state.df, st.session_state.location_summary = load_data()

st.subheader('Species Present at Each Location')

# Add Google Maps direction link
locations = st.session_state.location_summary['Location'].tolist()
if locations:
    # URL encode location names (handles international characters)
    formatted_locations = [quote(loc) for loc in locations]
    
    # Use the last location as destination and others as waypoints
    destination = formatted_locations[-1]
    waypoints = '|'.join(formatted_locations[:-1]) if len(formatted_locations) > 1 else ''
    
    maps_url = f"https://www.google.com/maps/dir/?api=1&waypoints={waypoints}&destination={destination}&travelmode=driving"
    st.markdown(f"[View Route on Google Maps]({maps_url})")

# Create an interactive display for the location summary
for _, row in st.session_state.location_summary.iterrows():
    with st.container():
        st.write(f"📍 {row['Location']}")
        species_list = row['Species Present'].split(', ')
        
        # Create columns for species popovers (5 species per row)
        cols = st.columns(5)
        for idx, species in enumerate(species_list):
            with cols[idx % 5]:
                # Get species details from the main dataframe
                species_data = st.session_state.df[
                    st.session_state.df['comName'] == species
                ]
                species_code = species_data['speciesCode'].iloc[0]
                
                with st.popover(f"{species}"):
                    # Show observation details first
                    st.write("**Recent Observations:**")
                    for _, obs in species_data.iterrows():
                        st.write(f"{obs['obsDt']}: {obs['howMany']} birds")
                    
                    # Create a unique key for storing the image
                    img_key = f"img_{species_code}"
                    if img_key not in st.session_state:
                        st.session_state[img_key] = None
                    
                    # Show button only if image hasn't been loaded yet
                    if st.session_state[img_key] is None:
                        if st.button(f"Load image for {species}", key=f"btn_{species_code}"):
                            try:
                                st.session_state[img_key] = fetch_img(species_code)
                            except Exception as e:
                                st.session_state[img_key] = f"Error: {str(e)}"
                    
                    # Display image if it has been loaded
                    if st.session_state[img_key] is not None:
                        if isinstance(st.session_state[img_key], str) and st.session_state[img_key].startswith("Error"):
                            st.error(st.session_state[img_key])
                        else:
                            st.image(st.session_state[img_key])
        st.divider()  # Add a visual separator between locations

# Add download button
csv = st.session_state.location_summary.to_csv(index=False)
st.download_button(
    label="Download Location Summary as CSV",
    data=csv,
    file_name="location_summary.csv",
    mime="text/csv",
)