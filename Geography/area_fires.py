import pandas as pd
import matplotlib.pyplot as plt
fire=pd.read_csv('forestfires.csv')
intensity=fire.area

def plot_areas_with_fires(intensity):
    '''
    Plots the large and small fires as a pie chart showing the 
    probability of occurrence of each
    '''
    import pandas as pd
    import matplotlib.pyplot as plt
    assert isinstance(intensity, pd.core.series.Series)
    assert intensity.all()>=0
    inten=intensity.iloc[intensity.nonzero()[0]]
    total=inten.count()
    small=inten[inten < 50 ].count() 
    large=inten[inten > 50 ].count() 
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'small fires','large fires'
    sizes = [small, large]
    explode = (0, 0.1)  # only "explode" the 2nd slice 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.show()
    
plot_areas_with_fires(intensity)
