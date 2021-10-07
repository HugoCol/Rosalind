
if __name__ == '__main__':
    file = open("Timorafschrifting 26-8-2020.csv")
    for line in file:

        if "Meo" in line:
            m = line.split(",")
            print(m[6]+","+m[7])
        if "2,75" in line:
            print(line)

# check de wasmachine kosten
# check de



    # for line in file:
    #     print(line)