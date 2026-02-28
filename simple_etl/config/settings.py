import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, 'data/raw/raw.csv')
CLEAN = os.path.join(BASE, 'data/processed/clean.csv')
