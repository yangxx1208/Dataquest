## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
print(type(flags))

most_bars_country = flags["name"][flags["bars"].idxmax()]


highest_population_country = flags["name"][flags["population"].idxmax()]
print(flags.columns)



## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = flags[flags["orange"] == 1].shape[0] /total_countries

stripe_probability = flags[flags["stripes"] > 1].shape[0] /total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = .5 ** 10

hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.

red_countries = flags[flags["red"] == 1].shape[0]

three_red = red_countries * (red_countries -1 ) *( red_countries -2)/total_countries/ (total_countries -1 ) /(total_countries -2)

## 5. Disjunctive probability ##

start = 1
end = 18000

hundred_prob = (18000/100) /18000

seventy_prob = int(18000/70) /18000

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

red_and_orange = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0]

red = flags[flags["red"] == 1] .shape[0]

orange = flags[flags["orange"] == 1].shape[0]

red_or_orange = (red + orange - red_and_orange)/total_countries



stripes = flags[flags["stripes"] > 0].shape[0] / flags.shape[0]
bars = flags[flags["bars"] > 0].shape[0] / flags.shape[0]
stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0] / flags.shape[0]

stripes_or_bars = stripes + bars - stripes_and_bars

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None


heads_or = 1 - .5 ** 3