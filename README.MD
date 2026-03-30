# Secret Gadget Guard (SGG)

## Overview
Secret Gadget Guard (SGG) is a context-aware mobile security system designed to detect suspicious device relocation using geolocation anomaly detection.

Unlike traditional mobile security apps that rely on immediate triggers, SGG monitors device location over time and detects when a device remains in an unusual location for a prolonged period (3–5 hours).

## Key Features
- 📍 Background location tracking
- 🧠 Geolocation anomaly detection
- ⏱ Time-based alert system
- 📧 Email notification with location data
- 🔐 Proactive mobile security approach

## System Architecture
- Android App (Kotlin) → collects location data  
- Python Backend → processes anomaly detection  
- REST API → communication layer  
- Email Service → alert system  

## Current Status
🚧 Project in early development stage  
- [x] Idea and system design completed  
- [ ] Android location tracking module  
- [ ] Python anomaly detection module  
- [ ] Alert system implementation  

## Technologies
- Python
- Kotlin (Android)
- REST APIs
- Geolocation Services
-  SMTP

## Goal
To build a lightweight, intelligent, and proactive mobile security system that improves device safety through behavioral analysis.

## Author
Emmanuel Akpan Okon
