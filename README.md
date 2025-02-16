# Bird Observation Analysis Tool

## Overview
This application provides real-time bird observation data based on your current location. It fetches recent bird sightings from eBird's database, displays them with species information, and provides an interactive interface to explore bird species including their images and observation details.

## Features
- 🗺️ Location-based bird observation data
- 🦜 Species information with images
- 📍 Interactive location summaries
- 🚗 Google Maps integration for birding routes
- 📊 Downloadable observation data
- 🌐 Multi-language support (default: Chinese)

## Prerequisites
- eBird API key

## Project Structure
- `app.py`: Main Streamlit application
- `get_user_location.py`: Handles browser geolocation services 
- `fetch_img.py`: Manages bird image fetching from eBird

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Allow location access when prompted
3. Explore bird observations in your area:
   - View species lists by location
   - Click on species names to see detailed information and images
   - Use the Google Maps link to plan your birding route
   - Download observation data as CSV
   - Data limited to recent observations within 15km radius

## Technical Details

### Key Components
- **Streamlit**: Frontend framework
- **eBird API**: Bird observation data source
- **BeautifulSoup**: Web scraping for bird images
- **Streamlit Javascript**: Browser geolocation integration

### Caching
- Bird observation data is cached for 24 hours
- Images are cached in session state
- Location data persists through browser refresh

### Location Services
- Uses browser geolocation
- Fetches observations within 15km radius
- Data limited to the past 7 days
