def health_calc(age,exercise_hrs,cigs_smoked):
    result = (100-age)+(exercise_hrs*3.5)-(cigs_smoked*2)
    print(result)


fahad_data = [23,3,1]

health_calc(fahad_data[0],fahad_data[1],fahad_data[2])
health_calc(*fahad_data)