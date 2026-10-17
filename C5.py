# converts Star to Delta 

def star_to_delta(ra, rb, rc):

    # -----defining var rnum as given
    rnum = ra * rb + rb * rc + rc * ra
    # ----- calculating rab, rbc, and rac
    rab = rnum / rc
    rbc = rnum / ra
    rac = rnum / rb

    # -----returning the values
    return (round(rab, 2), round(rbc, 2), round(rac, 2))


# ------testing the functions
def test():
    print(star_to_delta(ra=10, rb=20, rc=30))


test()
