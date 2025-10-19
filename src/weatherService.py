import xml.etree.ElementTree as ET
import requests
import os
from dotenv import load_dotenv
from typing import Dict, Tuple

# laoding env variables
load_dotenv()
# Configuration
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "weatherapi-com.p.rapidapi.com"
WEATHER_API_URL = f"https://{RAPIDAPI_HOST}/current.json"


def fetch_weather_data(city: str) -> Dict:

    headers = {"X-RapidAPI-Key": RAPIDAPI_KEY, "X-RapidAPI-Host": RAPIDAPI_HOST}
    params = {"q": city}

    try:
        if not RAPIDAPI_KEY:
            raise Exception("API key not configured.")
        response = requests.get(
            WEATHER_API_URL, headers=headers, params=params, timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch weather data: {str(e)}")


def parse_weather_response(data: Dict) -> Dict:

    location = data.get("location", {})
    current = data.get("current", {})

    return {
        "Weather": f"{current.get('temp_c', 'N/A')} C",
        "Latitude": str(location.get("lat", "N/A")),
        "Longitude": str(location.get("lon", "N/A")),
        "City": f"{location.get('name', 'Unknown')} {location.get('country', '')}",
    }


def convert_to_xml(data: Dict) -> str:
    root = ET.Element("root")

    # Map keys for XML output
    xml_mapping = {
        "Weather": "Temperature",
        "City": "City",
        "Latitude": "Latitude",
        "Longitude": "Longitude",
    }

    for key, xml_key in xml_mapping.items():
        element = ET.SubElement(root, xml_key)
        value = data.get(key, "")
        # Extract numeric temperature for XML format
        if xml_key == "Temperature" and isinstance(value, str):
            element.text = value.replace(" C", "")
        else:
            element.text = value.split()[0] if xml_key == "City" else value

    return ET.tostring(
        root, encoding="UTF-8", method="xml", xml_declaration=True
    ).decode("utf-8")


def validate_request_body(data: Dict) -> Tuple[bool, str]:

    if not data:
        return False, "Request body is required"

    if "city" not in data:
        return False, "City parameter is required"

    if not data["city"] or not isinstance(data["city"], str):
        return False, "City must be a non-empty string"

    output_format = data.get("output_format", "json").lower()
    if output_format not in ["json", "xml"]:
        return False, "output_format must be 'json' or 'xml'"

    return True, ""
