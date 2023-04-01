import matplotlib.pyplot as plt

mult = 10


delt = 9 * mult
for x in range(-delt+1, delt):
    x /= mult
    plt.plot([x],[(x**2 - 1)],'g.-')
plt.show()

delt = 9 * mult
for x in range(-delt+1, delt):
    x /= mult
    plt.plot([x],[x**2 - 8*x + 15],'g.-')
plt.show()

delt = 9 * mult
for x in range(-delt+1, delt):
    x /= mult
    plt.plot([x],[-x**2 + 4*x],'g.-')
plt.show()

delt = 9 * mult
for x in range(-delt+1, delt):
    x /= mult
    y = (x**2 - 6*x + 10)*(x>=1) + (x + 2)*(x<1)
    plt.plot([x],[y],'g.-')
plt.show()