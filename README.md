# Autonomous Object-Tracking Robotic Framework

**Authors:** Nathan Beer & Tomer Bengayev

## Project Overview
This project presents an autonomous robotic navigation system designed for real-time object tracking. The core of the system utilizes deep learning-based computer vision (YOLOv8) and natural language processing to identify, follow, and maintain visual contact with designated targets. 

This repository contains the modular software framework developed for this agent, focusing on high-level computer vision integration, spatial decision-making, and kinematic control.

## Project Status
The software framework is fully developed, unit-tested, and validated within an x86_64 development environment. 
* **Note:** The final physical hardware integration (Raspberry Pi/Robot controller) was deferred due to complex driver-level integration constraints encountered during the final development phase. This submission focuses on the professional-grade software architecture and the verified algorithmic implementation.

## Resource Access
Due to submission size limitations, the model weight files and presentation materials are hosted externally:
[**Download Models & Presentation (Google Drive Link)**](https://drive.google.com/drive/folders/1HLlBghSVgGtlEBA0yy9invSrj6Z-34Vu)

---

## Instructions for Development & Deployment (VS Code)

To deploy or test this code using Visual Studio Code, follow these steps:

### 1. Environment Setup
1. **Clone/Open the repository** in your VS Code workspace.
2. **Open the Terminal** in VS Code (Terminal > New Terminal).
3. **Install Dependencies:** Run the following command to ensure all required libraries are present:
   ```bash
   pip install ultralytics opencv-python SpeechRecognition