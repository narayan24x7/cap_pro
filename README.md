# EcoSight: Gemini Vision Multi-Agent Waste Sorting System
**AI-powered agents detect, classify, and automate waste sorting for optimized recycling efficiency.**

![EcoSight Banner](https://github.com/Janvi75/cap_pro/blob/main/EcoSight/Images/Thmbnail_Eco-Sight.png)

[![Open Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-blue)](https://www.kaggle.com/code/janviraj/ecosight-gemini-vision-multi-agent-waste-sorting/notebook)  

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Problem Statement](#problem-statement)  
3. [Solution Statement](#solution-statement)  
4. [Architecture](#architecture)  
5. [Workflow Diagram & Demo](#workflow-diagram--demo)  
6. [Test Results](#test-results)  
7. [PDF Report Features](#pdf-report-features)  
8. [PDF Preview](#pdf-preview)  
9. [Technology Stack](#technology-stack)  
10. [Code Organization](#code-organization)  
11. [Challenges](#challenges)  
12. [Future Enhancements](#future-enhancements)  
13. [Value Statement](#value-statement)  
14. [Links](#links)

---

## Project Overview

**EcoSight** is a multi-agent system for automated waste detection, classification, and reporting. Using **Google Gemini Vision API**, it provides:

- Real-time object detection  
- Classification based on local recycling regulations  
- Personalized disposal guidance  
- Quantified environmental impact  

---

## Problem Statement

- **Classification Confusion:** Users struggle with local recycling rules.  
- **Contamination:** Non-recyclables reduce efficiency by 25–30%.  
- **Information Fragmentation:** Disposal guidelines vary widely.  
- **Lack of Feedback:** Users don’t know their impact.  

**EcoSight** addresses these challenges with a single-image capture workflow.

---

## Solution Statement

- **Specialized Expertise:** Separate agents for vision, classification, reporting.  
- **Scalable Modularity:** New features added without rebuilding.  
- **Parallel Processing:** Real-time batch analysis.  
- **Context Preservation:** Personalized recommendations via session memory.  
- **Adaptive Intelligence:** Graceful degradation if one component fails.

---

## Architecture

**Layers:**

1. **Vision Analysis Layer:** Gemini Vision API + Mock fallback.  
2. **Classification & Location Intelligence:** WasteDB + LocationFinder.  
3. **Memory & Personalization:** MemoryBank stores user history.  
4. **Reporting & Output Generation:** PDF generator + interactive downloader.

---

## Workflow Diagram & Demo

**Workflow:**  

![EcoSight Workflow GIF](https://github.com/Janvi75/cap_pro/blob/main/EcoSight/Images/Eco-Sight_Workflow.png)  


**Steps:**  
1. Upload/capture image  
2. Vision Agent detects items  
3. Classification Agent categorizes items  
4. Reporting Agent generates PDF

[Watch Full Demo](https://www.youtube.com/watch?v=G3UFc_O710k)

---

## Test Results

**Dataset:** TrashNet (2,527 images, 6 categories)  

**Single Image:**  
- Detection: 2 items (glass, paper)  
- Classification: 100% recyclable  
- Processing time: ~2 seconds  
- PDF size: 6.4 KB  

**Bulk Test:**  
- Processed 4 images in parallel  
- Success rate: 100%  
- Average recyclable rate: 62.5%  
- Total items detected: 5  
- Parallel execution significantly faster than sequential  

---

## PDF Report Features

- Cover page with session ID, timestamp, model version  
- Executive summary (recyclable %, CO₂, water, energy saved)  
- Waste composition & detailed item analysis  
- Environmental impact assessment & AI recommendations  
- Interactive dashboard with live preview, downloads, and print

---

## PDF Preview

[Click here to view the Report PDF](https://github.com/Janvi75/cap_pro/blob/main/EcoSight/Output/EcoSight_report_48bb04d2-b5c6-4a12-9514-4e4edb4675d7.pdf)

---

## Technology Stack

- Python 3.11, AsyncIO, Pydantic
- Google Gemini Vision API, google-genai SDK
- Pillow, TrashNet dataset, WasteDB
- ReportLab, IPython.display
- Kaggle Notebooks for development

## Code Organization
```
EcoSight/
├── agents/
│   ├── vision_agent.py
│   ├── classification_agent.py
│   └── reporting_agent.py
├── tools/
│   ├── vision_provider.py
│   ├── waste_db.py
│   ├── location_finder.py
│   └── pdf_generator.py
├── memory/
│   └── memory_bank.py
├── orchestration/
│   └── orchestrator.py
└── utils/
    └── pdf_downloader.py
```

## Challenges
- Color Conversion in PDF: Patched Color.toHex() for RGB conversion
- TrashNet Dataset Access: Implemented fallback paths

---

## Future Enhancements
- Gemini 1.5 Flash integration
- Persistent database backend
- FastAPI + React web interface
- Barcode scanning, gamification, AR visualization
- Multi-language support, enterprise dashboards, mobile apps

---

## Value Statement

EcoSight demonstrates how multi-agent AI systems can transform environmental sustainability, making recycling effortless, accurate, and rewarding.

---

## Links

- [📺 YouTube Demo](https://www.youtube.com/watch?v=G3UFc_O710k)
- [📓 Kaggle Notebook](https://www.kaggle.com/code/janviraj/ecosight-gemini-vision-multi-agent-waste-sorting/notebook)
 