

def read_all(addrss):
    with open(addrss) as f:
        count = 1
        for line in f:
            count+=1
            print(line)
            break
        print(count)

# addrss = "/Users/charlie/datasets/MLIB_normalized/INITIAL_EXPERIMENTS_MIPLIB/DATA/30n20b8/30n20b8_strat=6_max=500_k=10_sort=-5_rank=1_retrainlimit=-1.dat"
# addrss = "/Users/charlie/datasets/MLIB_normalized/INITIAL_EXPERIMENTS_MIPLIB/DATA/acc-tight5/acc-tight5_strat=6_max=500_k=10_sort=-5_rank=1_retrainlimit=-1.dat"
addrss = "/Users/charlie/datasets/MLIB_normalized/INITIAL_EXPERIMENTS_MIPLIB/DATA/aflow40b/aflow40b_strat=6_max=500_k=10_sort=-5_rank=1_retrainlimit=-1.dat"
read_all(addrss)