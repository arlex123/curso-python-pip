import utils
import read_csv
import charts
import pandas as pd

def run():
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Digite el pais => ')
  
  result = utils.get_population(data, country)

  if len(result) > 0:
    country = result[0]
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(keys, values)

if __name__ == '__main__':
  run()