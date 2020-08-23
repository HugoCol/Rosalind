def main():
    """
    Not my code
    """
    n = int(input("Months: "))
    k = int(input("Litter size: "))
    lifespan = int(input("Lifespan: "))

    adult = []
    lil_babies = 1
    big_babies = 0

    current_month = 0
    oldest_gen = 0

    for i in range(n):
        current_month += 1
        if lifespan and current_month >= lifespan:
            adult[oldest_gen] = 0
            oldest_gen += 1

        print("\nMonth", i + 1,
              "\nAdults:", sum(adult), adult,
              "\nBig babies:", big_babies,
              "\nLil babies:", lil_babies,
              "\nTotal rabbits:", sum(adult) + big_babies + lil_babies)

        adult.append(big_babies)
        big_babies = lil_babies
        lil_babies = (sum(adult)) * k

main()
