# 💎 GemEditor Pro: Secure Hybrid Desktop Application
DEMO LIVE { https://lakshaywalia05.github.io/reportmaker }

![Version](https://img.shields.io/badge/Status-Production%20Ready-green) ![Security](https://img.shields.io/badge/Security-DRM%20Locked-red) ![Tech](https://img.shields.io/badge/Tech-Python%20%7C%20HTML5-blue)

**GemEditor Pro** is a secure, proprietary desktop software developed for Gemology Labs to generate high-fidelity authentication reports.

This project demonstrates a **Hybrid Architecture**, leveraging the system-level security of **Python** with the modern, responsive UI capabilities of **HTML5 & TailwindCSS**. The application is compiled into a single, standalone executable that runs 100% offline.

### 📥 Download Demo
[![Download Demo](https://img.shields.io/badge/Download-Demo_App_(.exe)-blue?style=for-the-badge&logo=windows)](https://github.com/lakshaywalia05/GemCardApp/archive/refs/tags/v1.0.zip)

*(Click the button above to download the secure Windows .exe)*

---

## 🏗️ Architecture Design

The application runs a secure Python backend that acts as a "Security Shell" around a modern Chromium-based frontend.

```mermaid
graph TD
    User[User Launches .EXE] -->|Starts| Python[Python Security Kernel]
    
    subgraph "Backend Logic (Python 3.12)"
        Python -->|Verifies| License{License Check}
        License -- Invalid/Expired --> Lock["🔴 Lock Screen (Access Denied)"]
        License -- Valid --> Engine[🟢 Initialize Chromium Engine]
    end

    subgraph "Frontend UI (HTML5/JS)"
        Engine -->|Injects| Assets[Offline Assets]
        Assets -->|Renders| UI[Gem Report Interface]
        UI -->|Processing| Cropper[Image Cropping Engine]
    end
```
🛠️ Technology Stack
Language: Python 3.12

GUI Engine: PyWebView (Chromium Wrapper)

Frontend: HTML5, TailwindCSS (Utility-First)

Security: Custom DRM Logic (Local File Encryption)

Build Tool: PyInstaller (One-File compilation)

⚠️ Note on Source Code
This is a commercial application. The full source code is stored in a private repository to protect the intellectual property and security algorithms.

Developer: Lakshay Walia Contact: lakshaywalia132@gmail.com
| **Main Dashboard** | **Security Lock Screen** |
|:---:|:---:|
| ![Main UI](screenshots/screen1.png) | ![Locked](screenshots/screen2.png) |
