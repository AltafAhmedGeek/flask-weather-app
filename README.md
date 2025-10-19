# 🚀 Flask RapidAPI Integration

This project is a simple **Flask** application that integrates with an external API using **RapidAPI**. It uses environment variables for configuration and demonstrates how to securely manage API keys and make external API calls.

---

## 🧰 Requirements

Before running the application, make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

---

## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/AltafAhmedGeek/flask-weather-app.git
   cd flask-weather-app
   ```

2. **Install dependencies**
   ```bash
   pip install Flask requests python-dotenv
   ```

3. **Set up environment variables**

   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

   Then open the `.env` file and replace the placeholder with your valid **RapidAPI key**:
   ```env
   RAPIDAPI_KEY=your_valid_rapidapi_key_here
   ```

---

## ▶️ Run the Application

Start the Flask app with:
```bash
python app.py
```

Once running, the app will be available at:
```
http://127.0.0.1:5000/
```

---

## 🧪 Testing the API

You can test the endpoints using:
 
- [Postman](https://www.postman.com/)  
- `curl` in your terminal  

Example:
```bash
curl  -X POST \
  'http://127.0.0.1:5000/getCurrentWeather' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "city":"mumbai",
  "output_format":"xml"
}'
```

---

## 📁 Project Structure

```
.
├── app.py
├── src/weatherService.py
├── .env
├── .env.example
└── README.md
```

---

## 🔐 Environment Variables

| Variable       | Description                     | Required |
|----------------|----------------------------------|-----------|
| `RAPIDAPI_KEY` | Your API key from RapidAPI       | ✅        |

---

## 🧑‍💻 Technologies Used

- **Flask** — lightweight Python web framework  
- **Requests** — for making HTTP API calls  
- **python-dotenv** — for managing environment variables securely  

---

## 📜 License

This project is licensed under the [MIT License].
