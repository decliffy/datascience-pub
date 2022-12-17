"""
Description: This code creates a frequency distribution chart of countries
that begin with initial letter. The code prints out details of the countries
that begin with the most frequent initial letter

Author: Clifford E. D'Souza
"""
import pandas as pd
import pycountry
import seaborn as sns
import matplotlib.pyplot as plt


def show_country_details(initial_letter):
    """
    Displays all countries where the name
    begins with the supplied initial letter

    param: initial_letter: str - starting letter
    """
    if len(initial_letter) == 0 or len(initial_letter) > 1:
        raise 'Incorrect input format'

    for country_instance in pycountry.countries:
        if country_instance.name[0] == initial_letter:
            print(country_instance.name, country_instance.flag, country_instance.alpha_3)


if __name__ == '__main__':
    country_name_list = []
    country_start_letter_list = []

    for country in pycountry.countries:
        country_name = country.name
        country_name_list.append(country_name)
        country_start_letter_list.append(country_name[0])

    df = pd.DataFrame(data={'Country_Name': country_name_list, 'First_Letter': country_start_letter_list})

    df_agg = df.groupby('First_Letter')['Country_Name'].nunique().reset_index().sort_values('Country_Name',
                                                                                            ascending=False)

    ax = sns.barplot(x='First_Letter',
                     y='Country_Name',
                     data=df_agg)

    ax.set(xlabel='Country Initial Letter',
           ylabel='# of Countries',
           title='Countries starting with letter')

    # Show the plot
    plt.show()

    # Show details of countries
    # starting with the most common initial letter
    show_country_details(df_agg['First_Letter'].iloc[0])
