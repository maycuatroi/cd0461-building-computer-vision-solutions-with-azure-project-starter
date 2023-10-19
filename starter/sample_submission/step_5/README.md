# Submission Checklist:

### Monitor performance and usage metrics of each cognitive service

1. [x] Screenshots of the Service Consumption Report showing the usage pattern and performance of each Azure cognitive
   resource
    - ![monitor.png](screenshots%2Fmonitor.png)
2. [x] Your final reflection write-up in PDF or text format
   - As part of this project, I have gained valuable experience in developing an automated passenger boarding kiosk using computer vision and AI technologies. The objective was to create a system that could scan passengers' ID cards and boarding passes, extract their information, verify their identity through facial recognition, and scan their carry-on luggage for prohibited items.
   - Throughout the project, I utilized various Azure services such as Azure Form Recognizer, FaceVison, and Azure Custom Vision. These services allowed me to extract passenger information, validate identity, compare faces, and identify prohibited items in luggage.
   - The development process involved creating a passenger manifest, fabricating digital IDs and boarding passes, and using the project owner's ID card and video for facial recognition validation. Additionally, sample images of passenger carry-on luggage were used to test the prohibited item detection system.
   - The overall experience of simulating the kiosk's functionality provided insights into the potential of automated airline boarding processes. The system demonstrated the ability to efficiently process and validate passenger data, ensuring a secure and seamless boarding experience.
   - In conclusion, this project has been a valuable opportunity to work with cutting-edge technologies in the field of computer vision and AI. It has enhanced my skills in system design, data processing, and integration of various Azure services. I am confident that the knowledge gained from this project will benefit future endeavors in the field of automation and passenger management.

### Merge various extracted information together for data validation and build the final solution

1. [x] A list of all the Python libraries used in your project in text format
    - List of libraries: [requirements.txt](..%2Frequirements.txt)
2. [x] Code snippet or screenshot showing that face matching is completed with X% match between face from the video and
   face from the ID
    - Code: [compare-face-matching.py](compare-face-matching.py)
    - Screenshot: ![face-identify.png](screenshots%2Fface-identify.png)
4. [x] Code snippet or screenshot showing you have generated the validation results from all the data from ID, boarding
   pass, and face video, and finally stored the validation results to the flight manifest table
    - Code: [generate-validation-result.py](generate-validation-result.py)
    - Output: [flight_manifest_validated.csv](flight_manifest_validated.csv)
5. [x] Screenshot for all successful validations
    - Screen shot: ![output-sc.png](screenshots%2Foutput-sc.png)
5. [x] If validation failed, a screenshot of the error message
    - No
6. [x] Your final manifest table, which has all the updated validation results
    - Output: [flight_manifest_validated.csv](flight_manifest_validated.csv)