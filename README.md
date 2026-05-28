# flight_search
Python-based flight deal monitoring system that:

-fetches destination pricing data from Google Sheets via Sheety API,
-searches live flight fares using Amadeus API,
-compares prices against threshold values,
-triggers email/WhatsApp alerts using Twilio.

Features:
-Automated flight search
-Google Sheets integration
-API-based workflow
-WhatsApp notifications
-Email alerts
-Environment variable security
-Modular OOP design

Technologies Used:
-Python
-Requests
-Sheety API
-Amadeus API
-Twilio API
-dotenv
-OOP concepts

Workflow:
Google sheet--Sheety API--Python processing--Amadeus Flight search--Price Comaprison--Notification trigger
