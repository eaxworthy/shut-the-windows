#Temorarily out of order due to changes in PurpleAir's api access protocols.

# shut-the-windows
Personal use project that sends a text notification when air quality is too poor to have windows open. Updates are sent whenever quality changes from less than 140 aqi to greater than, and vice versa. No further messages are sent until the next state change between (healthy/unhealthy). Quality is checked every 15 minutes while the program is running.

### Requirements:
A twilio sid and authentication token
A sensor ID for the purpleair sensor you want your data read in from.
Your twilio number that texts will be sent from.

Load these values, along with names and phone numbers, into the config.py template.


