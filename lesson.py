def naughty_or_nice(data: dict) ->str:
    naughty = 0
    nice = 0
    for month in data.values():
        for day in data.values():
            if day == 'Naughty':
                naughty += 1
            else:
                nice += 1
    if naughty > nice:
        return 'Naugty!'
    else:
        return 'Nice!'

