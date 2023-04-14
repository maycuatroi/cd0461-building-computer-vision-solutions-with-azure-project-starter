import requests

from starter.sample_submission.src.config import FormRecognize

# Set the API endpoint for the Form Recognizer ID's API
endpoint = f"{FormRecognize.ENDPOINT}/formrecognizer/v2.1-preview.3/prebuilt/idDocument"
# Set the subscription key for the Form Recognizer ID's API
subscription_key = FormRecognize.KEY

# Set the content type for the digital ID image
content_type = "image/jpeg"

# Set the local path to the digital ID image
image_path = "../material_preparation_step/boarding_pass/boarding-avkash.pdf"

# Read the binary data from the digital ID image
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Set the request headers
headers = {
    "Content-Type": content_type,
    "Ocp-Apim-Subscription-Key": subscription_key
}

# Send the API request to the Form Recognizer ID's API
response = requests.post(endpoint, headers=headers, data=image_data)

# Check the response status code
if response.status_code != 200:
    print("Error: Failed to extract information from digital ID")
    print("Details: {}".format(response.json()))
else:
    # Get the extracted information from the response JSON
    extracted_data = response.json()

    # Print the extracted information
    print(extracted_data)
