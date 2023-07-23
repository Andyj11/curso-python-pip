def get_population(country_dict):
  # keys = ['col', 'bol']
  # values = [300, 400]

  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  keys = population_dict.keys()
  values = population_dict.values()
  return keys, values


def get_world_population_percent(datas):
  percent_dict = {
    data['Country/Territory']: float(data['World Population Percentage'])
    for data in datas
  }
  keys = percent_dict.keys()
  values = percent_dict.values()
  return keys, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,
                       data))
  return result
