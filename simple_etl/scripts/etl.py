import pandas as pd
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config import settings

class ETLEngine:
    def run(self):
        # Extract
        df = pd.DataFrame({
            'id': [1, 2, 3],
            'user': [' admin ', 'JOHN', ' guest '],
            'val': [100.5, 200.0, -10],
            'date': ['2024-01-01', '2024-01-02', 'wrong']
        })
        df.to_csv(settings.RAW, index=False)
        print(f"[*] Extracted: {len(df)} rows")
        
        # Transform
        df['user'] = df['user'].str.strip().str.lower()
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df[(df['val'] > 0) & (df['date'].notna())].copy()
        print(f"[*] Transformed: {len(df)} rows")
        
        # Load
        df.to_csv(settings.CLEAN, index=False)
        print(f"[*] Loaded to: {settings.CLEAN}")

if __name__ == "__main__":
    ETLEngine().run()
