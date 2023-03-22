envelope = (50, 100)
postcard = (40, 60)

if (postcard[0] + 1) < envelope[0] and (postcard[1] + 1) < envelope[1]:
    print('открытка поместится в конверт')
else:
    print('открытка не поместится в конверт')