# Dataset Storytelling Studio 📊

An interactive, 3-week guided project turning raw datasets into structured, insight-driven data investigations. Built with Python, pandas, Seaborn, Plotly, and Streamlit.

## Project Structure
```text
dataset-storytelling-studio/
├── app.py                      # Main Streamlit application
├── data/
│   └── public_health_data.csv  # Sample raw & cleaned dataset
├── utils/
│   └── data_loader.py          # Data ingestion & caching helpers
├── assets/
│   └── custom.css              # Custom dashboard styling
├── teacher_resources/
│   ├── Data_Investigation_Canvas.md   # 4-Page Student Worksheet
│   └── Assessment_Rubric.md           # Grading framework
└── requirements.txt            # Python dependencies
```

## Quickstart

1. **Extract the ZIP file:**
   ```bash
   unzip dataset_storytelling_studio.zip -d dataset_storytelling_studio
   cd dataset_storytelling_studio
   ```

2. **Set Up Virtual Environment & Install Dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```
