import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

titanic = []
with open(os.path.join(__location__, 'Titanic.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic.append(dict(r))

teams = []
with open(os.path.join(__location__, 'Teams.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        teams.append(dict(r))

players = []
with open(os.path.join(__location__, 'Players.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        players.append(r)

class DB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


import copy


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.table_name + ':' + str(self.table)


table1 = Table('cities', cities)
table2 = Table('countries', countries)
table3 = Table('titanic', titanic)
table4 = Table('teams', teams)
table5 = Table('players', players)
my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)
my_DB.insert(table3)
my_DB.insert(table4)
my_DB.insert(table5)
# my_table1 = my_DB.search('cities')
# my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
# my_table1_selected = my_table1.select(['city', 'latitude'])
my_table5 = my_DB.search('players')
my_table5_filtered = my_table5.filter(lambda x: 'ia' in x['team'] and int(x['minutes']) < 200 and int(x['passes']) > 100)
my_table5_selected = my_table5_filtered.select(['surname', 'team', 'position'])
print('player on a team with “ia” in the team name played less than 200 minutes and made more than 100 passes')
print(my_table5_selected)
print()
# print(my_table1)
# print()
# print(my_table1_selected)
# print()
# print(my_table1_filtered)

my_table4 = my_DB.search('teams')
my_table4_filtered_above10 = my_table4.filter(lambda x: int(x['ranking']) <= 10)
my_table4_filtered_below10 = my_table4.filter(lambda x: int(x['ranking']) > 10)
avg1 = []
avg2 = []
for item in my_table4_filtered_above10.table:
    avg1.append(int(item['games']))
for item in my_table4_filtered_below10.table:
    avg2.append(int(item['games']))
print('The average number of games played for teams ranking below 10 versus teams ranking above or equal 10')
print(f"The average number of games played for teams ranking below 10: {sum(avg2)/len(avg2)}")
print(f"The average number of games played for teams ranking above or equal 10: {sum(avg1)/len(avg1)}")
print(my_table4_filtered_below10.aggregate(lambda x: sum(x) / len(x), 'games'))
print(my_table4_filtered_above10.aggregate(lambda x: sum(x) / len(x), 'games'))
print()

# temps = []
# for item in my_table1_filtered.table:
#     temps.append(float(item['temperature']))
# print(sum(temps) / len(temps))
# print("Using aggregation")
# print(my_table1_filtered.aggregate(lambda x: sum(x) / len(x), 'temperature'))

print('The average number of passes made by forwards versus by midfielders')
avg_mid = my_table5.filter(lambda x: x['position'] == 'midfielder').aggregate(lambda x: sum(x) / len(x), 'passes')
print('The average number of passes made by midfielders', avg_mid)
avg_for = my_table5.filter(lambda x: x['position'] == 'forward').aggregate(lambda x: sum(x) / len(x), 'passes')
print('The average number of passes made by forwards', avg_for)
print()
# my_table2 = my_DB.search('countries')
# my_table3 = my_table1.join(my_table2, 'country')
# my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
# print(my_table3_filtered.table)

