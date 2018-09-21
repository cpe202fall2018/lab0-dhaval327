def weight_on_planets():
    weight = float(input("What do you weigh on earth? \n"))
    mars_weight = weight * 0.38
    jupiter_weight = weight * 2.34
    print("On Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds."
          .format(mars_weight, jupiter_weight))


if __name__ == '__main__':
    weight_on_planets()