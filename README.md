# Real-Time Taxi Trip Analyzer – Logic App with Teams Notifications

This project uses Azure Logic Apps to process taxi trip events in real-time, analyze them using an Azure Function, and post categorized insights (normal, interesting, or suspicious) directly into a Microsoft Teams channel using Adaptive Cards.

## Screenshots

![8ee010b6-8ef8-457b-a7e5-d07bfbec34ca](https://github.com/user-attachments/assets/0fe3a601-b002-4c68-8ed3-86f5d501f5fe)


## What It Does
* Connects to an Azure Event Hub to receive incoming taxi trip data.
* Decodes and parses trip event messages (base64-encoded).
* Sends trip data to an Azure Function that flags if it's "interesting" or "suspicious".
* Posts real-time Adaptive Cards in Microsoft Teams with trip summaries.

## Technologies Used

* Azure Logic Apps
* Azure Event Hub
* Azure Function App (trip analyzer)
* Microsoft Teams Connector (Adaptive Card posts)
* Adaptive Card JSON Schema

## Architecture Overview

```
Event Hub ➞ Logic App ➞ Azure Function ➞ Microsoft Teams
```


## ⚖Setup Instructions

### 1. Deploy Azure Resources

Make sure you have these ready:

* An Azure Event Hub (e.g. `cst8917lab4-trips`)
* An Azure Function App with a working `analyze_trip` POST endpoint
* A Logic App (Consumption or Standard)
* Teams channel and bot permissions set up

### 2. Import Logic App JSON

1. Go to your Logic App in the Azure Portal.
2. Click “Logic App Designer”.
3. Click “Code view” → Replace the JSON with `workflow.json`.
4. Save.

### 3. Set Connection Parameters

Make sure you configure:

* Teams Connector (OAuth sign-in to Teams)
* Event Hub Connector (namespace and key binding)
* Validate that your Azure Function URL is reachable

### 4. Microsoft Teams Setup

Your messages will post to:

* **Team Group ID**: `46e4b3cd-51de-43f2-b9d6-25c99cb6021b`
* **Channel ID**: `19:d7W-8JoB_1JFJ8eZZ-xrcfOAYrEuwJL-riL2dg8q61g1@thread.tacv2`

Make sure you grant the Logic App bot access to that Team and Channel.

## Azure Function Sample Logic (analyze\_trip)

Here’s a sample of what your Azure Function might return:

```json
[
  {
    "vendorID": "CMT",
    "tripDistance": "8.3",
    "passengerCount": "3",
    "paymentType": "Card",
    "summary": "Trip looks fine overall.",
    "insights": [],
    "isInteresting": false
  }
]
```

Another example for a suspicious one:

```json
[
  {
    "vendorID": "CMT",
    "tripDistance": "0.1",
    "passengerCount": "4",
    "paymentType": "Cash",
    "summary": "Short trip with multiple passengers and cash payment.",
    "insights": ["SuspiciousVendorActivity"],
    "isInteresting": true
  }
]
```

## Adaptive Card Messages in Teams

Three types of cards are posted:

1. Normal Trip – Green card with summary.
2. Interesting Trip – Orange card with insights.
3. Suspicious Activity – Red alert with vendor and payment anomalies.

## Testing

To test the full pipeline:

1. Manually publish a message to your Event Hub in base64-encoded format.
2. Watch Teams for the posted Adaptive Card.
3. Use `monitor` in Logic App to view runs and debug any issues.

## Done By

Keval Trivedi
Course: CST8917
Lab 4 – Real-Time Trip Event Analyzer
