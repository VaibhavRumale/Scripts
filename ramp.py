import requests

url = "https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/stream"
output_file = "output.txt"

for i in range(1000):
    response = requests.get(url)
    output = response.text.strip()
    
    with open(output_file, "a") as f:
        f.write(output + "\n")

