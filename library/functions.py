"""return linear dependency plots and passes criteria keys, take values ​​entered by the user"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

criteria = {"Country": {'United States of America (the)', 'Australia', 'Chile', 'Canada'},
            "AirportName": {'Seattle-Tacoma International ', 'Daniel K. Inouye International ', 'Calgary International',
                            'Los Angeles International', 'Santiago International Airport',
                            'Washington Dulles International ',
                            'San Francisco International', 'Montreal Trudeau', 'Denver International',
                            'Boston Logan International ', 'Charlotte Douglas International',
                            'Dallas/Fort Worth International ',
                            'Chicago OHare International', 'Montreal Mirabel', 'Newark Liberty International ',
                            'Edmonton International', 'Hartsfield-Jackson Atlanta International ', 'Toronto Pearson',
                            'Winnipeg International', 'Detroit Metropolitan Wayne County ', 'McCarran International',
                            'John F. Kennedy International', 'Halifax International', 'Hamilton International',
                            'Miami International ', 'Vancouver International', 'LaGuardia', 'Kingsford Smith'},
            "State": {'Florida', 'Virginia', 'Georgia', 'Alberta', 'New Jersey', 'Colorado', 'Washington', 'Nevada',
                        'Manitoba',
                        'British Columbia', 'New York', 'Hawaii', 'Illinois', 'Michigan', 'California',
                        'Santiago Province',
                        'Massachusetts', 'Quebec', 'Nova Scotia', 'New South Wales', 'Ontario', 'Texas',
                        'North Carolina'},
            "City": {'College Park', 'Dorval', 'Newark', 'SeaTac', 'Calgary', 'Hamilton', 'Santiago', 'Charlotte',
                        'Grapevine',
                        'Floris', 'Chicago', 'Paradise', 'Boston', 'Halifax', 'Mirabel', 'Denver', 'Mississauga',
                        'Los Angeles',
                        'Winnipeg', 'Urban Honolulu', 'Leduc County', 'Romulus', 'New York', 'Sydney', 'Miami Springs',
                        'Richmond',
                        'South San Francisco'}}

def show_plot(dataset, criteria, criteria_value, from_date, to_date, make_mean, separator="'"):
    """returns a graph of the linear dependence of airport occupancy on the date, filters the data and saves it, takes the values ​​entered by the user"""
    df = dataset
    df.head()
    df = df.query(f"'{criteria_value}' == {criteria} and '{from_date}' <= Date <= '{to_date}' ")
    df.plot(x="Date",
            y="PercentOfBaseline",
            alpha=0.5)
    name_file = '../output/' + criteria + '_' + criteria_value + '_from_' + from_date + '_to_' + to_date + '.png'
    if make_mean:
        plt.axhline(y=np.nanmean(df.PercentOfBaseline))
    plt.savefig(name_file)
    plt.show()
