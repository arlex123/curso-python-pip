import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Digite el pais => ')
  
  result = utils.get_population(data, country)

  if len(result) > 0:
    country = result[0]
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(keys, values)

if __name__ == '__main__':
  run()