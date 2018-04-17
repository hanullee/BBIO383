def species_richness():
    S1 = {"microbe1":6, "microbe2":1, "microbe3":1, "microbe4":1}
    S2 = {"microbe1":7, "microbe2":1, "microbe3":1, "microbe4":1}
    S3 = {"microbe1":7, "microbe2":1, "microbe3":1, "microbe4":1}
    S4 = {"microbe1":7, "microbe2":1, "microbe3":1, "microbe4":1}
    S5 = {"microbe1":7, "microbe2":1, "microbe3":1, "microbe4":1}
    S6 = {"microbe1":7, "microbe2":1, "microbe3":2, "microbe4":1}
    S7 = {"microbe1":4, "microbe2":6, "microbe3":0, "microbe4":0}
    S8 = {"microbe1":3, "microbe2":0, "microbe3":0, "microbe4":7}
    S9 = {"microbe1":3, "microbe2":0, "microbe3":6, "microbe4":0}
    S10 = {"microbe1":4, "microbe2":6, "microbe3":0, "microbe4":0}
    S11 = {"microbe1":6, "microbe2":3, "microbe3":1, "microbe4":0}
    S12 = {"microbe1":3, "microbe2":0, "microbe3":0, "microbe4":7}
    temp_list = []
    temp_list.append(S1)
    temp_list.append(S2)
    temp_list.append(S3)
    temp_list.append(S4)
    temp_list.append(S5)
    temp_list.append(S6)
    temp_list.append(S7)
    temp_list.append(S8)
    temp_list.append(S9)
    temp_list.append(S10)
    temp_list.append(S11)
    temp_list.append(S12)
    count = 0
    for each_dict in temp_list:
        num_Species = 0
        count += 1
        for key in each_dict:
            if each_dict[key] != 0:
                num_Species += 1
        print("Richness of S%i = %i" %(count, num_Species))

def main():
    species_richness()

if __name__ == '__main__':
    main()
