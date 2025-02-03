from streamlit_javascript import st_javascript
import time

def get_user_location():
    res = st_javascript("""await new Promise((resolve, reject) => {
        if (!navigator.geolocation) {
            reject("Geolocation is not supported by this browser.");
    }

        navigator.geolocation.getCurrentPosition(
            // Success callback
            (position) => {
                resolve({
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude
                });
            },
            // Error callback
            (error) => {
                reject("Error getting location: " + error.message);
            },
            // Options
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            }
        );
    })
    """)
    
    while res == 0:
        time.sleep(0.1)
    return res
