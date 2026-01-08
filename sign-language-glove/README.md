# Glove-Based Sign Language Translation System

## Problem Statement
People who rely on sign language often face communication challenges when others around them do not understand hand gestures. This can create dependence on interpreters and limit natural, spontaneous interaction.

## Project Overview
This project demonstrates a **glove-based sign language translation system** inspired by sensor-based wearable solutions.  
Instead of camera-based hand tracking, the system uses **sensor-based input** to capture finger movements and translate gestures into meaningful output.

Due to hardware limitations, **flex sensor data is simulated**, but the complete gesture recognition and translation pipeline is fully implemented.

## How the System Works
1. Finger bend data is captured using **simulated flex sensors**
2. The sensor values are processed using **rule-based gesture recognition**
3. Recognized gestures are mapped to meaningful words
4. The output is displayed as text and converted into **speech using text-to-speech**

## Why Sensor-Based Input?
- Works reliably in low-light or occluded environments
- Avoids limitations of camera-based hand tracking
- More suitable for accessibility-focused applications
- Improves consistency and precision in gesture recognition

## Technologies Used
- Python
- Simulated Flex Sensors
- Rule-Based Gesture Recognition
- Text-to-Speech (`pyttsx3`)

## How to Run the Project
1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
Submission for Hand Tracking & Gesture Interaction assignment

