def calculate_windchill(T,V):
    wc= 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    return wc

def change_temperature(T):
    fahrenheit = (T*9/5)+32
    return fahrenheit 

def main():
    print()
    T = int(input("What is the temperature?: "))
    medition = input("Fahrenheit or Celsius (F/C)? ") 
    V = 5

    print()
    if medition !="F":
        T = change_temperature(T)

    while V <= 60:
        wind_chill = calculate_windchill(T,V)

        print(f"At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F")
        V +=5
    print()

main()