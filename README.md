# RetinaXAI: Explainable AI for Diabetic Retinopathy Screening in Rural India 👁️🩺

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![HTML5 / ES6 Modules](https://img.shields.io/badge/Stack-HTML5%20%7C%20Vanilla%20ES6%20%7C%20TailwindCSS-teal.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Explainable AI](https://img.shields.io/badge/XAI-Grad--CAM%20Saliency%20Heatmaps-orange.svg)](https://arxiv.org/abs/1610.02391)

An end-to-end, production-ready, client-side web application built for hackathon demonstration and rural healthcare deployment (ASHA workers, primary health sub-centers, and mobile eye clinics).

---

## 🎯 The Problem Statement
**"Explainable AI for Diabetic Retinopathy screening in rural India"**

- **The Crisis**: Over 77 million people in India live with diabetes. Diabetic Retinopathy (DR) damages retinal capillaries and is the leading cause of preventable working-age blindness.
- **The Rural Chasm**: While 70% of India's population resides in rural areas, over 70% of ophthalmologists are clustered in major tier-1 cities. The rural doctor-to-patient ratio for eye specialists is less than 1 in 250,000.
- **The Silent Danger**: In early stages (Mild to Moderate NPDR), patients experience **zero pain and zero vision loss**. Over 80% of rural diabetics only visit a clinic after irreversible retinal detachment or vitreous hemorrhage has already occurred.
- **Why Explainable AI (XAI)?**: Black-box deep learning models generate distrust among clinicians and patients. By projecting **Grad-CAM (Gradient-weighted Class Activation Mapping)** heatmaps directly onto the retina, clinicians and health workers can visually inspect *why* the AI flagged microaneurysms, hemorrhages, or neovascularization.

---

## 🌟 Key Features

### 1. 🔍 Explainable AI (XAI) & Grad-CAM Visualization
- **Multi-Layer Visualization Engine**:
  - **Original Fundus**: High-definition retinal aperture view.
  - **Grad-CAM Heatmap**: Real-time thermal gradient (Blue = cold/normal $\rightarrow$ Green $\rightarrow$ Yellow $\rightarrow$ Red = peak pathological attention).
  - **Lesion Detection Map**: Highlights microaneurysms, blot hemorrhages, hard exudate rings, and cotton wool spots with bounding markers.
  - **Vessel Segmentation**: High-contrast green-channel capillary structure extraction.
- **Interactive Heatmap Opacity Slider**: Smooth alpha-blending slider (0% to 100%) to fade the saliency map over the retinal scan.
- **ICDR 5-Grade Staging**: Automated diagnostic classification from **Grade 0 (Normal)** to **Grade 4 (Proliferative DR)** with confidence score gauges.
- **Preloaded Clinical Samples**: 1-click preset library across all 5 severity levels for instant testing during the hackathon.
- **Custom Image Upload**: Drag-and-drop or camera capture for high-resolution fundus images or smartphone condensing lens attachments.

### 2. 🌐 Multilingual with Dynamic RTL (Right-to-Left) Support
- **6 Supported Languages**:
  1. 🇬🇧 English (`en`)
  2. 🇮🇳 Hindi - हिन्दी (`hi`)
  3. 🇳🇵 Nepali - नेपाली (`ne`)
  4. 🇮🇳 Tamil - தமிழ் (`ta`)
  5. 🇦🇪 Arabic - العربية (`ar` - **RTL Layout**)
  6. 🇵🇰 Urdu - اردو (`ur` - **RTL Layout**)
- **Automatic Layout Inversion**: When **Urdu** or **Arabic** is selected, the entire document direction flips to `dir="rtl"`, realigning navigation, sidebar, forms, labels, and badges naturally for native readers.

### 3. 🌓 Dark Mode & Light Mode
- High-contrast clinical theme system designed for rural field clinics and night-time examinations.
- Instant toggle with persistence in `localStorage`.

### 4. 🎙️ Arogya Netra AI Voice Assistant & Chatbot
- **Speech-to-Text (Microphone input)**: Leverages the browser Web Speech API for hands-free voice inquiries.
- **Text-to-Speech (Audio response)**: Reads out diagnostic explanations and clinical advice in the selected language.
- **Rural Knowledge Base**: Pre-configured with clinical advice on DR prevention, smartphone fundus photography steps for ASHA workers, diet tips, and explanation of heatmap colors.

### 5. 💊 Patient Medication & Insulin Adherence Tracker
- **Log Daily Medications**: Tablets, insulin injections, and eye drops with dosage and meal timing (Before/After meal).
- **Daily Checklist**: Interactive morning, afternoon, and night dose checklists.
- **Adherence Score & Streak**: Computes real-time compliance percentage (e.g. 100% Optimal, Partial Attention, or Critical Low) to monitor patient intake and avoid hyperglycemic complications.

### 6. 🏥 Multi-Country Emergency Directory & Top Eye Hospitals
- Country dropdown switcher supporting:
  - 🇮🇳 **India**: Aravind Eye Care, Sankara Nethralaya, LVPEI, AIIMS, Dr. Shroff's (108 / 102 ambulance, 1075 helpline, ASHA link).
  - 🇳🇵 **Nepal**: Tilganga Institute of Ophthalmology, Nepal Eye Hospital (102 ambulance).
  - 🇦🇪 **UAE**: Moorfields Dubai, Cleveland Clinic Abu Dhabi (998 ambulance).
  - 🇸🇦 **Saudi Arabia**: King Khaled Eye Specialist Hospital (997 ambulance).
  - 🇧🇩 **Bangladesh**: National Institute of Ophthalmology Dhaka (999 ambulance).
- Direct "Call Now" buttons and Google Maps directions links.

### 7. 📄 Printable Clinical Referral Report & WhatsApp Triage
- Generates a formal, printable diagnostic report with patient demographics, retinal scan + Grad-CAM snapshot, ICDR severity, biomarker breakdown, and referring doctor signature line.
- Direct 1-click **"Share via WhatsApp"** button for ASHA workers to send referral summaries directly to district ophthalmologists.

---

## 📁 Project Structure

```
c:/Users/dell/Downloads/upcoming/
├── index.html               # Main single-page application shell
├── css/
│   └── styles.css           # Custom theme variables, RTL rules, and print styling
├── js/
│   ├── app.js               # Application orchestrator, event bindings & profile state
│   ├── i18n.js              # Localization dictionary (6 languages) & RTL engine
│   ├── xai_engine.js        # Grad-CAM heatmap, procedural fundus & ICDR diagnostics
│   ├── voice_assistant.js   # Web Speech recognition, speech synthesis & chatbot
│   ├── medicine_tracker.js  # Medication adherence calculator & daily dose tracker
│   └── hospital_data.js     # Country-based emergency & hospital directory
├── server.py                # Zero-dependency Python 3 local development server
├── start.bat                # Windows 1-click launcher script
└── README.md                # Project documentation & presentation guide
```

---

## 🚀 How to Run

### Option 1: 1-Click Launcher (Windows)
Simply double-click:
```cmd
start.bat
```

### Option 2: Using Python (Recommended)
Open PowerShell or Command Prompt inside the project directory:
```bash
python server.py
```
This starts the local web server at `http://localhost:8000/index.html` and automatically opens your browser.

### Option 3: Direct File Open
You can also open `index.html` directly in Google Chrome, Microsoft Edge, or Mozilla Firefox.

---

## 🏆 Hackathon Presentation & Demonstration Script

1. **The Hook (30 sec)**:
   - "Good morning judges. 77 million Indians have diabetes, but 70% of eye doctors are in cities. Early diabetic retinopathy has zero symptoms until it's too late. How do we bring specialist screening to rural India?"
2. **The Demo (90 sec)**:
   - **Show AI Screening**: Click the **"Severe NPDR"** or **"Proliferative DR"** sample scan.
   - **Explain XAI**: Switch visualization from *Original* to *Grad-CAM Heatmap* and *Lesion Map*. Move the *Opacity Slider* to show the judges the red thermal attention peaks over the microaneurysms and hemorrhages.
   - **Show Multilingual & RTL**: Switch language to **Urdu** or **Arabic** to show the UI dynamically re-orienting to Right-to-Left (`dir="rtl"`). Switch to **Hindi** or **Tamil** to show local script accessibility.
   - **Show Voice Assistant**: Click the mic or a quick prompt to demonstrate *Arogya Netra* explaining the heatmap colors.
   - **Show Medicine Tracker**: Demonstrate ticking morning/night doses and watch the adherence percentage update in real-time.
   - **Export Report**: Click **"Print / Export Medical Report"** to show the referral slip for district hospitals.
3. **Closing (30 sec)**:
   - "RetinaXAI bridges the rural-urban specialist divide, empowers ASHA workers, builds patient trust through Explainable AI, and saves millions of eyes from preventable blindness."
