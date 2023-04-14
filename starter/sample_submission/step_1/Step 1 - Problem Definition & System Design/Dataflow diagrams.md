# Dataflow diagrams

```mermaid
graph LR
    1[1. Passenger Manifest] -->|Input| 5[5. Boarding Pass Validation]
    2[2. Digital IDs] -->|Input| 3[3. Identity Verification]
    4[4. Boarding Passes] -->|Input| 5[5. Boarding Pass Validation]
    6[6. Passenger Videos] -->|Input| 7[7. Facial Recognition]
    8[8. Carry-on Item Images] -->|Input| 9[9. Prohibited Item Detection]

    5 -->|Passenger Information| 3
    3 -->|Identity Verification| 7
    2 -->|Digital ID Information| 3
    4 -->|Boarding Pass Information| 5
    6 -->|Video| 7
    8 -->|Carry-on Item Images| 9

    5 -->|Validated Boarding Pass| 10[10. Boarding Pass Validation Result]
    3 -->|Verified Identity| 11[11. Identity Verification Result]
    7 -->|Facial Verification Result| 12[12. Facial Recognition Result]
    9 -->|Prohibited Item Flag| 13[13. Prohibited Item Detection Result]

    10 -->|Validation Result| 14[14. Boarding Confirmation]
    11 -->|Verification Result| 14
    12 -->|Verification Result| 14
    13 -->|Detection Result| 14

    14 -->|Boarding Status| 15[15. Final Boarding Status]
```

Explaining Data Flow as shown in the above image:

1. The passenger manifest, digital IDs, boarding passes, passenger videos, and carry-on item images are input into the process.
2. The Azure Form Recognizer service extracts passenger information from the boarding passes.
3. The Azure Form Recognition Digital ID service extracts personal information and face from passengers' digital IDs.
4. The extracted passenger information is validated against the manifest list.
5. The passenger identity is verified using their personal ID.
6. The Azure Video Indexer service compares the face photo from the digital ID to the passenger's video to perform facial recognition.
7. Azure Custom Vision services are utilized to create a machine learning model for identifying prohibited items in carry-on luggage using the provided lighter images.
8. The Azure Custom Vision model is tested using the sample images of passenger carry-on luggage provided in the project.
9. The validation results, including the validated boarding pass, verified identity, facial recognition result, and prohibited item flag are output from the process.
10. The final boarding confirmation is displayed based on the validation results.
11. The final boarding status is output from the process.