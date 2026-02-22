import pandas as pd
import numpy as np

np.random.seed(101)

# Generate rail network
cities = ['Chicago', 'Denver', 'Seattle', 'Portland', 'LA', 'Phoenix', 
          'Dallas', 'Houston', 'KC', 'Minneapolis']

routes = []
for i, city1 in enumerate(cities):
    for j, city2 in enumerate(cities):
        if i < j:  # avoid duplicates
            distance = np.random.randint(200, 2000)
            capacity = np.random.choice([50, 75, 100, 125])
            cost_per_mile = np.random.uniform(2.5, 4.5)
            routes.append({
                'route_id': f'R-{len(routes):03d}',
                'from_city': city1,
                'to_city': city2,
                'distance_miles': distance,
                'capacity_cars': capacity,
                'cost_per_mile': cost_per_mile,
                'avg_delay_hours': np.random.uniform(0, 5),
                'reliability_score': np.random.uniform(0.7, 1.0)
            })

routes_df = pd.DataFrame(routes)

# Generate shipments
n_shipments = 500
shipments = {
    'shipment_id': [f'S-{i:04d}' for i in range(n_shipments)],
    'origin': np.random.choice(cities, n_shipments),
    'destination': np.random.choice(cities, n_shipments),
    'cargo_cars': np.random.randint(10, 50, n_shipments),
    'priority': np.random.choice(['Low', 'Medium', 'High', 'Urgent'], n_shipments),
    'deadline_hours': np.random.randint(24, 168, n_shipments),
    'revenue': np.random.uniform(5000, 50000, n_shipments)
}
shipments_df = pd.DataFrame(shipments)

# Remove same origin-destination
shipments_df = shipments_df[shipments_df['origin'] != shipments_df['destination']]

routes_df.to_csv('rail_network.csv', index=False)
shipments_df.to_csv('shipments.csv', index=False)


'''

---

### **PROBLEM STATEMENT:**
```
BNSF Railway - Network Optimization System
===========================================

Optimize rail network routing for maximum profit and efficiency.

INPUT: 
- rail_network.csv (45 routes)
- shipments.csv (~450 shipments)

PART 1 (20 minutes): Route Finding Algorithm
---------------------------------------------
Write a function: find_optimal_route(origin, destination, network_df, criteria='cost')

Requirements:
1. Find best route between two cities
2. Support multiple criteria:
   - 'cost': minimize total cost (distance * cost_per_mile)
   - 'time': minimize total time (distance/avg_speed + delays)
   - 'reliability': maximize reliability score

3. Handle multi-hop routes (may need intermediate cities)
4. Return:
   - Route path: ['Chicago', 'Denver', 'Seattle']
   - Total distance
   - Total cost
   - Estimated time
   - Overall reliability score

Algorithm requirements:
- Use Dijkstra's or A* algorithm
- Time complexity: O(E log V) where E=edges, V=vertices
- Handle disconnected graphs (no route possible)

Example:
>>> route = find_optimal_route('Chicago', 'Seattle', routes_df, 'cost')
>>> print(route)
{
  'path': ['Chicago', 'Denver', 'Seattle'],
  'total_distance': 1750,
  'total_cost': 5687.50,
  'estimated_hours': 36.2,
  'reliability': 0.87
}


PART 2 (30 minutes): Shipment Assignment Optimizer
---------------------------------------------------
Write a function: optimize_shipment_assignment(shipments_df, routes_df, constraints)

constraints = {
    'max_cars_per_route': 100,
    'available_trains': 20,
    'cost_budget': 500000
}

Requirements:
1. Assign shipments to routes considering:
   - Route capacity (can't exceed max_cars_per_route)
   - Priority (Urgent > High > Medium > Low)
   - Deadlines (must arrive on time)
   - Available trains

2. Optimization objective:
   - Maximize: total revenue
   - Minimize: total cost
   - Maximize: on-time deliveries
   - Combined score = revenue - cost + (on_time_bonus * 1000)

3. Greedy algorithm approach:
   a) Sort shipments by priority and revenue
   b) For each shipment, find best route
   c) Check capacity and constraints
   d) Assign if feasible, skip if not

4. Return:
   - Assignment DataFrame:
     ['shipment_id', 'assigned_route', 'departure_time', 
      'arrival_time', 'cost', 'revenue', 'on_time']
   - Optimization summary:
     {
       'total_shipments_assigned': int,
       'total_shipments_skipped': int,
       'total_revenue': float,
       'total_cost': float,
       'profit': float,
       'on_time_percentage': float,
       'capacity_utilization': float
     }

Example:
>>> assignments, summary = optimize_shipment_assignment(shipments, routes, constraints)
>>> print(summary)
{
  'total_shipments_assigned': 387,
  'total_shipments_skipped': 63,
  'total_revenue': 8950000,
  'total_cost': 3420000,
  'profit': 5530000,
  'on_time_percentage': 94.3,
  'capacity_utilization': 78.2
}


PART 3 (20 minutes): Real-Time Optimization
--------------------------------------------
Write a function: handle_disruption(assignments_df, disruption_event)

disruption_event = {
    'affected_route': 'R-012',
    'disruption_type': 'track_maintenance',
    'duration_hours': 12,
    'affected_shipments': ['S-0045', 'S-0123', ...]
}

Requirements:
1. Identify affected shipments
2. Find alternative routes for each
3. Calculate delay and additional cost
4. Re-optimize assignments considering:
   - New costs
   - New timelines
   - Priority adjustments (urgent shipments get priority)

5. Return:
   - Rerouting plan:
     ['shipment_id', 'original_route', 'new_route', 
      'additional_cost', 'delay_hours', 'still_on_time']
   - Impact analysis:
     {
       'affected_shipments_count': int,
       'successfully_rerouted': int,
       'will_be_late': int,
       'additional_cost': float,
       'customer_impact_score': float (0-100)
     }

Example:
>>> rerouting, impact = handle_disruption(assignments, disruption_event)
>>> print(impact)
{
  'affected_shipments_count': 23,
  'successfully_rerouted': 21,
  'will_be_late': 2,
  'additional_cost': 45000,
  'customer_impact_score': 8.7  # out of 100, lower is better
}


CONSTRAINTS:
- Must use efficient algorithms (Dijkstra's, greedy, etc.)
- Time complexity: O(n log n) or better
- Handle large networks (1000+ routes)
- Production-ready error handling

EVALUATION:
- Algorithm correctness: 50%
- Optimization quality: 30%
- Code efficiency: 20%
'''