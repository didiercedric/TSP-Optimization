import itertools

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def total_distance(points, order):
    total = 0
    for i in range(len(order) - 1):
        total += euclidean_distance(points[order[i]], points[order[i+1]])
    total += euclidean_distance(points[order[-1]], points[order[0]])
    return total

def tsp_bruteforce(points):
    best_order = None
    best_distance = float('inf') # The value float('inf') represents positive infinity in Python
    for order in itertools.permutations(range(len(points))):
        distance = total_distance(points, order)
        if distance < best_distance:
            best_distance = distance
            best_order = order
    return best_order, best_distance

if __name__ == "__main__":
    # Replace the following points with your own coordinates
    points = [(0, 0), (1, 5), (2, 3), (5, 2)]
    
    best_order, best_distance = tsp_bruteforce(points)
    print("Best order:", best_order)
    print("Best distance:", best_distance)
