'''
Problem 4: Moving Average (Sliding Window)

Task: Given a list of temperatures [70, 72, 75, 80, 82] and a window size K=3, return the moving average at each point.

Skill: List slicing, sum()/len() logic, or collections.deque.

'''

from collections import deque

class SensorAverage:
    def __init__(self,moving_window):
        self.moving_window = moving_window
        self.q = deque(maxlen = moving_window)
        self.current_sum = 0

    def moving_average(self,value):
        if len(self.q) == self.moving_window:
            self.current_sum -= self.q[0]
        self.q.append(value)
        self.current_sum += value
        
        # Calculate mean
        return self.current_sum / len(self.q)

# Example Usage:
tracker = SensorAverage(moving_window=3)

print(tracker.moving_average(10)) # Mean: 10.0
print(tracker.moving_average(20)) # Mean: 15.0
print(tracker.moving_average(30)) # Mean: 20.0
print(tracker.moving_average(40)) # Mean: 30.0 (10 was dropped, calculates (20+30+40)/3)
