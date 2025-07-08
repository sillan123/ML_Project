End 2 END ML Project

#File Structure

ML_PROJECT/
│
├── build/                    # (auto-generated) Built distributions, not edited manually
├── ml_env/                   # Your Python virtual environment (best practice)
├── mlproject.egg-info/       # (auto-generated) Metadata for packaging
│
├── src/                      #  MAIN SOURCE CODE goes here
│   ├── __init__.py           # Marks 'src' as a Python package
│   │
│   ├── components/           #  Contains core modular components of the ML pipeline
│   │   ├── __init__.py
│   │   ├── data_ingestion.py        # For reading, downloading, or loading data
│   │   ├── data_transformation.py   # For preprocessing, encoding, scaling, etc.
│   │   ├── model_trainer.py         # For training ML models
│   │
│   ├── pipeline/            #  Ties components into workflows/pipelines
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py      # Code for running prediction on new data
│   │   ├── train_pipeline.py        # Code for triggering the full training workflow
│   │
│   ├── exception.py         #  Custom exception handling module
│   ├── logger.py            #  Logging setup for debugging and monitoring
│   ├── utils.py             #  Utility functions used across modules
│
├── .gitignore               # Files/folders to ignore in Git (like ml_env/, __pycache__)
├── README.md                #  Project overview, usage, installation guide
├── requirements.txt         #  Python dependencies needed
├── setup.py                 #  Packaging script (used for `pip install .`)
