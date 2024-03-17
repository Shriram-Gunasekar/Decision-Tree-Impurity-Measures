def renyi_entropy(p, alpha):
    if alpha == 1:
        return -np.sum(p * np.log(p))
    else:
        return 1/(1-alpha) * np.log(np.sum(p**alpha))
