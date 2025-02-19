import matplotlib.pyplot as plt

# Create a simple plot
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Test Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Save the plot to a file
plt.savefig('test_plot.png')
plt.close()
