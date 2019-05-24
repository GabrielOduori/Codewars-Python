
def tortoise(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        time = g * 3600 / (v2 - v1)
        H = int(time / 3600)
        MM = int((time % 3600) / 60)
        S = int(time % 3600% 60)
        required_time = [H, MM, S]
    return required_time





#test: tortoise(720, 850, 70);
