import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    plt.scatter(x, y, label='Original Data')
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    y_fit = intercept + slope * x

    # Filter data from the year 2000 onward
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']

    # Create second line of best fit 
    slope_recent, intercept_recent, r_r_value, r_p_value, r_std_err = linregress(x_recent, y_recent)
    nyears_recent = pd.Series(range(2000, 2051))  # Extend to 2050
    nsea_recent = intercept_recent + slope_recent * nyears_recent

    nyears = pd.Series(range(x.min(), 2051)) 
    nsea = intercept + slope * nyears

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.plot(nyears, nsea, 'r', label='Prediction (All Data)')
    plt.plot(nyears_recent, nsea_recent, 'green', label='Prediction (Since 2000)') 
    plt.legend()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()