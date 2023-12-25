import time

i = 0
start = time.time()
while i < 1000000000:
    i = i + 1

print("Total Execution time = {:.3f} seconds".format(time.time() - start))