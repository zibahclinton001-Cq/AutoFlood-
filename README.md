# AutoFlood-
# Auto Flood Gate

Smart gate that protects houses from flood while you sleep.

Problem
Port Harcourt floods every rainy season. Water enters compounds at night.

 Solution
Automatic gate that:
- Reads outside water level with sensor
- Closes gate when flood is coming
- Opens when water goes down
- Turns on pump if water enters inside
- Sends phone alert

How It Works
- 10cm Dry - Gate open
- 10-25cm Warning - Alert phone
- 25-40cm Danger - Gate closes
- 40cm+ Critical - Gate closed + Pump on

Tech
Python (simulation)
Real build: ESP32 + HC-SR04 + Servo Motor + Water Pump

Future
Add GSM module for SMS alert and solar power.

Author
Zibah Clinton 