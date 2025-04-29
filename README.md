# 🚚📈 Real-Time E-Commerce Clickstream & Fleet Telemetry Data Integration

## 🧩 Overview

This project is a prototype real-time data integration system designed for an e-commerce company. It processes two critical data streams:

1. **Customer Clickstream Data** from the online platform
2. **IoT Telemetry Data** from a fleet of delivery trucks

The goal is to improve customer experience and optimize logistics using AWS serverless services and real-time processing pipelines.

---

## 📌 Problem Statement

To ensure seamless customer experience and operational efficiency, our system must:

- Understand **customer preferences** through clickstream analysis.
- Monitor **truck performance** using IoT sensors and optimize fleet logistics.

---

## 🛒 Online Platform Optimization

### ✅ Objective:
Analyze customer interactions to optimize UX and marketing for product categories:
- Mobile Phones
- Laptops
- Cameras

### 📊 Real-Time Data Collected:
- `item_id`
- `item_name`
- `click_count`

---

## 🚛 Fleet Management & Logistics Optimization

### ✅ Objective:
Monitor and analyze vehicle performance, maintenance, and environmental data from delivery trucks.

### 🛰️ Real-Time Telemetry Data Collected (Every Minute):
- `truck_id`
- `gps_location`: latitude, longitude, altitude, speed
- `vehicle_speed`
- `engine_diagnostics`: RPM, fuel level, temperature, oil pressure, battery voltage
- `odometer_reading`
- `fuel_consumption`
- `vehicle_health_and_maintenance`: brake status, tire pressures, transmission status
- `environmental_conditions`: temperature, humidity, pressure

### ✅ SCD Type 2:
Truck data is stored in DynamoDB with Slowly Changing Dimension (Type 2) schema to retain historical changes over time.

---

## 🏗️ Architecture

- **Data Ingestion**: Custom REST API + AWS Kinesis Data Streams
- **Data Processing**: AWS Lambda functions for transformation and computation
- **Data Storage**: 
  - Clickstream → DynamoDB
  - Truck telemetry → DynamoDB (SCD Type 2)
- **Data Generation**: Python scripts simulate real-time data

---

## 📦 Tech Stack

| Component         | Technology            |
|------------------|-----------------------|
| Real-time Streams | AWS Kinesis           |
| Compute           | AWS Lambda            |
| Storage           | AWS DynamoDB          |
| API Simulation    | Python (Flask/FastAPI)|
| Infrastructure    | AWS (Serverless)      |

---

