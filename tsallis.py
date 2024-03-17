def tsallis_entropy(p, q):
    if q == 1:
        return -np.sum(p * np.log(p))
    else:
        return 1/(q-1) * (1 - np.sum(p**q))
