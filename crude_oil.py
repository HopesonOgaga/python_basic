def crude_volume(tank_volume, fill_percentage):
    return tank_volume * (fill_percentage/100)



print(f"the amount of crude fill the tank is {crude_volume(1000,68)} cubic metre")