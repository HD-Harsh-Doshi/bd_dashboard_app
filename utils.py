import pandas as pd

def process_data(df):
    """Cleans and extracts date features for analysis."""
    if df.empty:
        return df
    
    # Convert camp_date to datetime (Format: MM-DD-YY)
    df['camp_date_dt'] = pd.to_datetime(df['camp_date'], format='%m-%d-%y', errors='coerce')
    df['year'] = df['camp_date_dt'].dt.year.fillna(0).astype(int)
    
    # Fill NAs for display
    df['area'] = df['area'].fillna('Unknown')
    df['data_source'] = df['data_source'].fillna('General')
    return df