import requests
from bs4 import BeautifulSoup
import streamlit as st

@st.cache_data
def fetch_img(species_code="manher1"):
    url = f"https://ebird.org/species/{species_code}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        img_element = soup.select_one('div.Media-content img')
        
        if img_element and 'src' in img_element.attrs:
            img_url = img_element['src']
            img_data = requests.get(img_url).content
            return img_data
        else:
            return None
            
    except Exception as e:
        st.error(f"Error fetching image: {str(e)}")
        return None

if __name__ == "__main__":
    img_data = fetch_img("manher1")    