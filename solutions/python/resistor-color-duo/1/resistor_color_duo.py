def value(colors):
    color_code={
            "black":0,
            "brown":1,
            "red":2,
            "orange":3,
            "yellow":4,
            "green":5,
            "blue":6,
            "violet":7,
            "grey":8,
            "white":9,
        }
    color_duo=''
    for i,color in enumerate(colors):
        if i<2 :color_duo=color_duo+f'{color_code[color]}' 
    return int(color_duo)