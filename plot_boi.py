import matplotlib.pyplot as plt
# log
plt.subplot(222)
plt.plot([10000,100000,200000,400000,700000,1000000],[0.057,0.331,0.843,2.457,7.183,14.1])
#plt.yscale('log')
#plt.title('log')
plt.grid(True)
plt.show()