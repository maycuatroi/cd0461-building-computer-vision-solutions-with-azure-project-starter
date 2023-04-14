# Step 1 - Problem Definition & System Design

[Dataflow diagrams](Step%201%20-%20Problem%20Definition%20&%20System%20Design/Dataflow%20diagrams.md)

[Architecture Diagram](Step%201%20-%20Problem%20Definition%20&%20System%20Design/Architecture%20Diagram.md)

## Problem Statement:

The objective of this project is to develop an automated passenger boarding kiosk for airline operations using computer vision and AI technologies. The kiosk should be able to scan the passenger's ID card and boarding pass, extract their information, verify their identity through facial recognition, and scan their carry-on luggage for prohibited items. Based on the validation results, the kiosk should either allow the passenger to board the plane or suggest that they seek assistance from an airline representative.

## Data Sources:

The input data for this project includes a flight manifest list of passengers, their digital ID cards, boarding passes, a video of the project owner's face, and sample images of passengers' carry-on luggage.

## Solution Strategy:

1. Use Azure Form Recognizer to extract passenger information from boarding passes.
2. Utilize Azure Form Recognition Digital ID service to extract personal information and face from passengers' digital IDs.
3. Validate passenger information against the manifest list.
4. Verify passenger identity using their personal ID.
5. Compare the face photo from the digital ID to the passenger's video using Azure Video Indexer.
6. Create a machine learning model for identifying prohibited items in carry-on luggage using Azure Custom Vision services.
7. Test the Azure Custom Vision model using the sample images of passenger carry-on luggage provided in the project.
8. Display a final message allowing the passenger to board the plane or recommending that they seek assistance from an airline representative based on the validation results.

## Simulate the kiosk experience

1. A passenger manifest with a list of 5+ passengers and their information will be created.
2. Fabricated digital IDs will be created for all passengers listed in the manifest.
3. Fabricated boarding passes will be created for all passengers listed in the manifest.
4. The project owner's fabricated ID card will be included in the list of passengers to validate the facial recognition system using the project owner's video.
5. A 15-30 second video of the project owner will be used as the kiosk's facial recognition system.
6. The sample images of passenger carry-on luggage provided in the project will be used to scan for lighters, and if a lighter is present, the passenger will be flagged for prohibited items in their carry-on baggage.
7. All of this input data will be processed by various Azure computer vision services to simulate the automated airline boarding process.

## Input Data Sources:

- Flight manifest list for all passengers (5+)
- Fabricated digital IDs for all passengers listed in the manifest
- Fabricated boarding passes for all passengers listed in the manifest
- The project owner's fabricated ID card and a 15-30 second video of the project owner's face
- Sample images of passenger carry-on luggage provided in the project for prohibited item detection.