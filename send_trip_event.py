from azure.eventhub import EventHubProducerClient, EventData
import json

CONNECTION_STR = 'Endpoint=sb://kevaltaxi-namespace.servicebus.windows.net/;SharedAccessKeyName=SendPolicy;SharedAccessKey=NmvrPYHJPWj2s+9wlGTU/ocqrOTO4gyo1+AEhL9PWbY='
EVENTHUB_NAME = 'taxi-trips-hub'

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME
)

event_data_batch = producer.create_batch()

trip_event = {
    "ContentData": {
        "vendorID": "V001",
        "tripDistance": 0.6,
        "passengerCount": 5,
        "paymentType": "2"
    }
}

event_data_batch.add(EventData(json.dumps(trip_event)))

producer.send_batch(event_data_batch)
print("✅ Trip event sent.")
