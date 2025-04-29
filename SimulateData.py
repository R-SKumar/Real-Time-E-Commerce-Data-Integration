import streamlit as st
import json
import random
import boto3
from datetime import datetime

# AWS Region & Stream Names
AWS_REGION = "<aws region>"
CLICKSTREAM_STREAM = "<Stream name>"
TELEMETRY_STREAM = "<Stream name>"

# Sample product data
products = [
    {"Item_ID": "M1", "Item_Name": "Apple iPhone 15 Pro Max"},
    {"Item_ID": "M2", "Item_Name": "Samsung Galaxy Z Fold5"},
    {"Item_ID": "M3", "Item_Name": "Google Pixel 8 Pro"},
    {"Item_ID": "L1", "Item_Name": "Dell XPS 15"},
    {"Item_ID": "L2", "Item_Name": "Apple MacBook Pro M3"},
    {"Item_ID": "L3", "Item_Name": "HP Spectre x360"},
    {"Item_ID": "C1", "Item_Name": "Sony Alpha a7 IV"},
    {"Item_ID": "C2", "Item_Name": "Fujifilm X-T5"},
    {"Item_ID": "C3", "Item_Name": "Canon EOS R6 Mark II"},
]

# Sample truck telemetry data
truck_ids = ["TRK001", "TRK002", "TRK003"]

# Initialize Kinesis client
@st.cache_resource
def get_kinesis_client():
    return boto3.client("kinesis", region_name=AWS_REGION)

client = get_kinesis_client()

# App UI
st.title("📡 Real-Time Data Simulator")
data_type = st.selectbox("Select data stream to simulate", ["Clickstream", "Truck Telemetry"])

events_to_send = st.slider("Number of events to send", min_value=1, max_value=50, value=5)

if st.button("🚀 Send Data"):
    for _ in range(events_to_send):
        if data_type == "Clickstream":
            STREAM_NAME = CLICKSTREAM_STREAM
            product = random.choice(products)
            payload = {
                "Item_ID": product["Item_ID"],
                "Item_Name": product["Item_Name"],
                "Click_Counts": random.randint(1, 100),
                "Timestamp": datetime.utcnow().isoformat()
            }
            partition_key = product["Item_ID"]

        else:
            STREAM_NAME = TELEMETRY_STREAM
            truck_id = random.choice(truck_ids)
            payload = {
                "truck_id": truck_id,
                "gps_location": {
                    "latitude": round(random.uniform(33.0, 41.0), 6),
                    "longitude": round(random.uniform(-120.0, -70.0), 6),
                    "altitude": round(random.uniform(5, 1000), 2),
                    "speed": round(random.uniform(30, 80), 2)
                },
                "vehicle_speed": round(random.uniform(30, 80), 2),
                "engine_diagnostics": {
                    "engine_rpm": random.randint(1500, 3000),
                    "fuel_level": round(random.uniform(20.0, 100.0), 2),
                    "temperature": round(random.uniform(70.0, 100.0), 2),
                    "oil_pressure": round(random.uniform(30.0, 60.0), 2),
                    "battery_voltage": round(random.uniform(12.5, 14.5), 2)
                },
                "odometer_reading": round(random.uniform(50000, 150000), 1),
                "fuel_consumption": round(random.uniform(10.0, 25.0), 2),
                "vehicle_health_and_maintenance": {
                    "brake_status": random.choice(["Good", "Needs Inspection"]),
                    "tire_pressure": {
                        "front_left": round(random.uniform(30.0, 36.0), 1),
                        "front_right": round(random.uniform(30.0, 36.0), 1),
                        "rear_left": round(random.uniform(32.0, 38.0), 1),
                        "rear_right": round(random.uniform(32.0, 38.0), 1),
                    },
                    "transmission_status": "Operational"
                },
                "environmental_conditions": {
                    "temperature": round(random.uniform(10.0, 35.0), 2),
                    "humidity": round(random.uniform(20.0, 80.0), 2),
                    "atmospheric_pressure": round(random.uniform(1005.0, 1025.0), 2)
                },
                "timestamp": datetime.utcnow().isoformat()
            }
            partition_key = truck_id

        # Send to Kinesis
        response = client.put_record(
            StreamName=STREAM_NAME,
            PartitionKey=partition_key,
            Data=json.dumps(payload).encode("utf-8")
        )
        st.json(payload)

    st.success(f"{events_to_send} events sent to {data_type} stream ✅")
