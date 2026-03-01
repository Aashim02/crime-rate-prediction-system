# API Smoke Test Report

- Time: 2026-03-01 22:31:42
- Base URL: http://127.0.0.1:5000

## Results

- GET /health
  - Response: {"status":"API running"}


- POST /predict
  - Payload: {"crime_type":1,"area":2,"time":3,"month":5}
  - Response: {"prediction":"High Crime Risk"}


- POST /predict_crime
  - Payload: {"location":"Downtown","crime_type":"Theft","incident_count":3}
  - Response: {"prediction":1}


- POST /crime_alert
  - Payload: {"prediction":1}
  - Response: {"alert":"High crime risk detected. Please stay alert in this area."}

