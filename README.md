Flight Search & Price Alert System
Overview

Python-based flight deal monitoring system that:

Fetches destination pricing data from Google Sheets using the Sheety API
Searches live flight fares using the Amadeus API
Compares live fares against predefined threshold prices
Triggers Email and WhatsApp alerts using Twilio when lower fares are identified
Features
Automated flight fare monitoring
Google Sheets integration
API-based workflow automation
WhatsApp notification alerts
Email notification alerts
Secure environment variable handling using .env
Modular Object-Oriented Programming (OOP) architecture
Technologies Used
Python
Requests Library
Sheety API
Amadeus Flight API
Twilio API
dotenv
Object-Oriented Programming (OOP)
Project Workflow
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
Project Structure
flight-search/
│
├── data_manager.py
├── flight_data.py
├── flight_search.py
├── notification_manager.py
├── main.py
├── requirements.txt
├── .env
└── README.md
Setup Instructions
1. Clone the Repository
git clone <repository-url>
2. Install Dependencies
pip install -r requirements.txt
3. Configure Environment Variables

Create a .env file and add:

AMADEUS_API_KEY=
AMADEUS_SECRET=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
SHEETY_TOKEN=
4. Run the Application
python main.py
Future Improvements
Add scheduler support for periodic execution
Deploy on cloud/VPS environment
Integrate database logging
Add fare trend visualization dashboard
Implement multi-user alert subscriptions
