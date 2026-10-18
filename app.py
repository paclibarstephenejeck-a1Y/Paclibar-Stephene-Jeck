
import requests

url = "https://paclibar-stephene-jeck.onrender.com/student"

try:
    response = requests.get(url, timeout=60)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        print("Student ID:", data.get("student_id", "Not found"))
        print("Name:", data.get("name", "Not found"))
        print("Program:", data.get("program", "Not found"))
        print("Year:", data.get("year", "Not found"))
        print("Section:", data.get("section", "Not found"))

    else:
        print("Request failed.")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("Connection error:", e)
