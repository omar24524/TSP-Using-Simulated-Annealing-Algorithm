import numpy as np
import matplotlib.pyplot as plt

# Assuming the Coordinate class is defined as follows:
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_total_distance(coords):
        # Calculate the total distance of the path
        total_distance = 0
        for i in range(len(coords) - 1):
            total_distance += np.sqrt((coords[i+1].x - coords[i].x)**2 + (coords[i+1].y - coords[i].y)**2)
        # Add distance from last to first to close the loop
        total_distance += np.sqrt((coords[0].x - coords[-1].x)**2 + (coords[0].y - coords[-1].y)**2)
        return total_distance

if __name__ == '__main__':
    coords = [Coordinate(np.random.uniform(), np.random.uniform()) for _ in range(20)]

    fig = plt.figure(figsize=(18, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    # Plot initial path
    for first, second in zip(coords[:-1], coords[1:]):
        ax1.plot([first.x, second.x], [first.y, second.y], 'b')
    ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax1.plot(c.x, c.y, 'ro')

    # Simulated Annealing
    cost0 = Coordinate.get_total_distance(coords)
    T = 30
    factor = 0.99

    for i in range(1000):
        print(i,'cost = ',cost0)
        T *= factor  # Decrease temperature
        for j in range(500):
            r1, r2 = np.random.randint(0, len(coords), size=2)

            # Swap two coordinates
            coords[r1], coords[r2] = coords[r2], coords[r1]

            cost1 = Coordinate.get_total_distance(coords)

            if cost1 < cost0:
                cost0 = cost1
            else:
                x = np.random.uniform()
                if x < np.exp((cost0 - cost1) / T):
                    cost0 = cost1
                else:
                    # Swap back if not accepted
                    coords[r1], coords[r2] = coords[r2], coords[r1]

    # Plot optimized path
    for first, second in zip(coords[:-1], coords[1:]):
        ax2.plot([first.x, second.x], [first.y, second.y], 'b')
    ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax2.plot(c.x, c.y, 'ro')

    plt.show()