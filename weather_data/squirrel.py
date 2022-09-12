import pandas

data = pandas.read_csv('squirrel_data.csv')
fur_colors = data['Primary Fur Color'].to_list()

squirrel_idx = pandas.Index(fur_colors)

fur_counts = pandas.DataFrame(squirrel_idx.value_counts())

fur_counts_csv = fur_counts.to_csv('fur_counts.csv')

