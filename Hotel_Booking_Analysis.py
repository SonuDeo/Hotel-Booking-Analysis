
# Companion script: Hotel_Booking_Analysis.py
# Place hotel_bookings.csv in the same folder and run: python Hotel_Booking_Analysis.py
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_dataset(path='hotel_bookings.csv'):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        raise FileNotFoundError('Place hotel_bookings.csv in the same folder.')

def save_fig(fig, name):
    outdir = 'notebook_outputs'
    os.makedirs(outdir, exist_ok=True)
    p = os.path.join(outdir, name)
    fig.savefig(p, bbox_inches='tight')
    print('Saved:', p)

def main():
    df = load_dataset()
    print('Loaded', df.shape)
    data = df.copy()
    if 'children' in data.columns:
        data['children'] = data['children'].fillna(0).astype(int)
    for col in ['agent','company']:
        if col in data.columns:
            data[col] = data[col].fillna(0).astype(int)
    if set(['adults','children','babies']).issubset(data.columns):
        data['total_guests'] = data['adults'] + data['children'] + data['babies']
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    if 'arrival_date_month' in data.columns:
        data['arrival_month_num'] = data['arrival_date_month'].apply(lambda x: months.index(x)+1 if x in months else np.nan)

    # Example plot: cancellation distribution
    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(1,1,1)
    canceled_counts = data['is_canceled'].value_counts().sort_index()
    ax.bar(canceled_counts.index.astype(str), canceled_counts.values)
    ax.set_xticks([0,1])
    ax.set_xticklabels(['Not Canceled','Canceled'])
    ax.set_ylabel('Number of bookings')
    ax.set_title('Reservation Status: Canceled vs Not Canceled')
    save_fig(fig, 'fig_reservation_status.png')

if __name__ == '__main__':
    main()
