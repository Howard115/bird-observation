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
- `get_observation.py`: Handles eBird API interactions and location services
- `fetch_img.py`: Manages bird image fetching using Selenium

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

## Technical Details

### Key Components
- **Streamlit**: Frontend framework
- **eBird API**: Bird observation data source
- **Selenium**: Web scraping for bird images
- **Pandas**: Data manipulation and analysis
- **Pydantic**: Settings management

### Caching
- Bird observation data is cached for 24 hours
- Images are cached in session state for improved performance

### Location Services
- Uses browser geolocation
- Fetches observations within 15km radius
- Data limited to the past 7 days
