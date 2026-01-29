sex = input(" Enter your sex (M/F): ")
hemoglobin_value = float(input(" Enter your hemoglobin value(g/l): "))
if sex == "M" and hemoglobin_value <= 167 and hemoglobin_value >= 134:
    print("you have a normal hemoglobin for adult males")
elif sex == "M" and hemoglobin_value <= 134:
    print(" your hemolobin value is low " )
elif sex == "M" and hemoglobin_value >= 167:
    print(" your hemoglobin value is high " )
elif sex == "F" and hemoglobin_value >= 117 and hemoglobin_value <= 155:
    print(" you have a normal hemoglobin for adult females ")
elif sex == "F" and hemoglobin_value >= 155:
    print(" your hemoglobin value is high ")
elif sex == "F" and hemoglobin_value <= 117:
    print(" your hemoglobin value is low ")
