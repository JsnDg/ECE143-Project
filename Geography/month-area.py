import pandas as pd
fire=pd.read_csv('forestfires.csv')
month=fire.month.map({'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12})
intensity=fire.area
day=fire.day.map({'mon':1, 'tue':2, 'wed':3, 'thu':4, 'fri':5, 'sat':6, 'sun':7})

def fires_and_month_day(intensity, month, day):
    '''
    Plots the frequency of observing fires in respective months and days
    '''
    import matplotlib.pyplot as plt
    assert isinstance(intensity, pd.core.series.Series)
    assert isinstance(month, pd.core.series.Series)
    assert isinstance(day, pd.core.series.Series)
    assert intensity.all()>=0
    assert 0<month.all()<13
    assert 0<day.all()<8
    month_num=month.iloc[intensity.nonzero()[0]]
    day_num=day.iloc[intensity.nonzero()[0]]
    fig, axs = plt.subplots(1, 2)
    axs[0].grid(linestyle = '--')
    axs[1].grid(linestyle = '--')
    axs[0].hist(month_num, bins=12)
    axs[1].hist(day_num.dropna(), bins=7)
    axs[0].set_xlabel('month')
    axs[0].set_ylabel('frequency of fire')
    axs[1].set_xlabel('day')
    axs[1].set_ylabel('frequency of fire')
    plt.show()

    
fires_and_month_day(intensity,month,day)
