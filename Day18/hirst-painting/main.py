import colorgram

colors = colorgram.extract("painting_orginal.jpg", 30)
color_pallet = []
for i in range(len(colors)):
    # print(colors[i].rgb)
    color_pallet.append(colors[i].rgb)
print(color_pallet)
