  if np.mod(i, 50) == 0:
        print("\r{:.1f}% done!".format(100 * i / len(locdf)), end="", flush=True)