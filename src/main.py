from numpy.random import randint

def get_seq_in():               # make sure user inputs a valid combination to flip for
    while True:
        seq = input("Enter an arbitrarily-long sequence of H and T: ").lower()
        if set(seq).issubset("ht"):
            return seq

        print("Invalid characters in sequence! include only H and T (case-insensitive)\n")


def get_num_flips():            # make sure user inputs a valid flips number
    while True:
        num_flips = input("Number of times to flip coins: ")
        if num_flips.isdigit() and (nr:= int(num_flips)) > 0:
            return nr

        print(f"Invalid input ('{num_flips}') - must be a positive integer (ex. 5)\n")


def seq_to_int_list(seq: str):                      # format sequence str (ex. "HHHTH") to list of ints ([1,1,1,0,1])
    return [int(c == "h") for c in seq.lower()]


def flip_for_seq(num_flips: int, seq: list[int]):   # flip coins given # times and return whether each flip matched or didn't
    seq_l = len(seq)
    seq = seq_to_int_list(seq)

    results = randint( 2, size=(num_flips, seq_l) )
    return [list(x)==seq for x in results]


def cf_prob(num_flips: int = None, seq: str = None):    # get the occurrence probability of a given sequence over a given number of attempts
    if num_flips == None: num_flips = get_num_flips()
    if seq == None: seq = get_seq_in()

    freq = flip_for_seq(num_flips, seq)
    num_found = sum(freq)

    print(f"\n{'*'*30}\nSequence: {seq.upper()} \nSequence Length: {len(seq)}")
    print("Number of flips: {:,} \n".format(num_flips))
    print(f"Sequence occurrence frequency: {round(100*num_found/num_flips, 2)}% ({num_found}/{num_flips})\n{'*'*30}\n")


def main():                                             # run our three tests (three heads, 3x alternating HT, user choice)
    cf_prob(num_flips=100000, seq="HHH")
    cf_prob(num_flips=1000000, seq="HTHTHT")
    cf_prob()


if __name__ == "__main__":
    main()