import xml.etree.ElementTree as ET
from flask import Flask, request, jsonify, Response
from src.weatherService import (
    fetch_weather_data,
    parse_weather_response,
    convert_to_xml,
    validate_request_body,
)

app = Flask(__name__)


@app.route("/getCurrentWeather", methods=["POST"])
def get_current_weather():
    try:
        request_data = request.get_json()

        # Validate request
        is_valid, error_msg = validate_request_body(request_data)
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        city = request_data["city"]
        output_format = request_data.get("output_format", "json").lower()

        # Fetch and parse weather data
        raw_data = fetch_weather_data(city)
        weather_data = parse_weather_response(raw_data)

        # Return response in requested format
        if output_format == "xml":
            xml_response = convert_to_xml(weather_data)
            return Response(xml_response, mimetype="application/xml", status=200)
        else:
            return jsonify(weather_data), 200

    except Exception as e:
        error_response = {"error": str(e)}

        # Return error in requested format if possible
        output_format = (
            request.get_json().get("output_format", "json").lower()
            if request.get_json()
            else "json"
        )

        if output_format == "xml":
            root = ET.Element("root")
            error_elem = ET.SubElement(root, "error")
            error_elem.text = str(e)
            xml_error = ET.tostring(
                root, encoding="UTF-8", method="xml", xml_declaration=True
            ).decode("utf-8")
            return Response(xml_error, mimetype="application/xml", status=500)
        else:
            return jsonify(error_response), 500


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
