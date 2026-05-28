# Flight Search & Price Alert System 
## Overview Python-based flight deal monitoring system that: 
- Fetches destination pricing data from Google Sheets using the Sheety API
-  Searches live flight fares using the Amadeus API
-  Compares live fares against predefined threshold prices
- Triggers Email and WhatsApp alerts using Twilio when lower fares are identified

 
## Features
 - Automated flight fare monitoring
 - Google Sheets integration
 - API-based workflow automation
 - WhatsApp notification alerts
- Email notification alerts -
-  Secure environment variable handling using `.env`
- Modular Object-Oriented Programming (OOP) architecture

  
## Technologies Used
- Python
- Requests Library
- Sheety API
- Amadeus Flight API
- Twilio API 
-  dotenv
- Object-Oriented Programming (OOP)

## Project Workflow 

```text


 Google Sheets
     ↓
 Sheety API
     ↓
 Python Processing
     ↓
Amadeus Flight Search
      ↓
Price Comparison Logic
       ↓
Email / WhatsApp Notification Trigger

```

