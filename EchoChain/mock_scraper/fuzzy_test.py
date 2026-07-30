from fuzzywuzzy import fuzz

title1 = "Samsung Galaxy Book3 RAM"
title2 = "Samsung GalaxyBook 3 Ram Module"

score = fuzz.ratio(title1, title2)
print(f"Similarity Score: {score}")