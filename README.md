# flight_search
Automated tool to send a personal message alert when the flight prices hit the lower threshold within a specified time range.


Work Flow:
- Google sheets contains the raw data of destinations, time range and price threshold for message trigger.
- Google API call is used to read the data from google sheet.
- This data is further used to do an api call in amadeus flight search api service to check if any flight exists which meets our required lower price limit.
- On identification of such a flight, twillio api service is used to trigger a whatsapp message to notify the specified user regarding the flight, date and price details.



Key Concept used:
- Api calls

This tool can further be scheduled to run on a weekly/daily basis to automate the entire workflow.
