import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(202)

# Generate traffic data
segments = []
for i in range(50):  # 50 rail segments
    segment = {
        'segment_id': f'SEG-{i:03d}',
        'location': f'Mile-{i*10}',
        'max_capacity_trains_per_hour': np.random.choice([2, 3, 4, 5]),
        'avg_speed_limit_mph': np.random.choice([40, 50, 60]),
        'segment_length_miles': np.random.randint(5, 20),
        'double_track': np.random.choice([True, False]),
        'maintenance_schedule': np.random.choice(['none', 'weekly', 'daily'], p=[0.7, 0.2, 0.1])
    }
    segments.append(segment)

segments_df = pd.DataFrame(segments)

# Generate train schedule
n_trains = 200
start_time = datetime(2026, 2, 25, 0, 0)
trains = []
for i in range(n_trains):
    train = {
        'train_id': f'TRAIN-{i:04d}',
        'departure_time': start_time + timedelta(minutes=np.random.randint(0, 1440)),
        'priority': np.random.choice([1, 2, 3, 4, 5]),  # 5 = highest
        'type': np.random.choice(['Freight', 'Express', 'Local']),
        'num_cars': np.random.randint(50, 150),
        'destination_segment': np.random.randint(0, 50)
    }
    trains.append(train)

trains_df = pd.DataFrame(trains)

segments_df.to_csv('rail_segments.csv', index=False)
trains_df.to_csv('train_schedule.csv', index=False)
'''
```

---

### **PROBLEM STATEMENT:**

BNSF Railway - Traffic Flow Control System
===========================================

Optimize train traffic to minimize delays and maximize throughput.

INPUT:
- rail_segments.csv (50 segments)
- train_schedule.csv (200 trains)

PART 1 (25 minutes): Conflict Detection
----------------------------------------
Write a function: detect_conflicts(trains_df, segments_df)

Requirements:
1. Calculate when each train will be on each segment
2. Detect conflicts:
   - Two trains on same single-track segment
   - Capacity exceeded (> max_capacity trains per hour)
   - Trains too close (< 10 minute separation)

3. For each conflict, identify:
   - Conflict type
   - Affected trains
   - Segment location
   - Time window
   - Severity score (1-10)

4. Use efficient algorithm:
   - Sort trains by departure time: O(n log n)
   - Sweep through timeline: O(n*m) where m = segments
   - Early exit optimizations

5. Return:
   - Conflicts DataFrame:
     ['conflict_id', 'segment', 'train1', 'train2', 
      'time', 'type', 'severity']
   - Summary:
     {
       'total_conflicts': int,
       'critical_conflicts': int (severity > 7),
       'affected_trains': int,
       'peak_conflict_time': datetime
     }

Example:
>>> conflicts, summary = detect_conflicts(trains, segments)
>>> print(summary)
{
  'total_conflicts': 47,
  'critical_conflicts': 8,
  'affected_trains': 62,
  'peak_conflict_time': '2026-02-25 14:30'
}


PART 2 (25 minutes): Schedule Optimization
-------------------------------------------
Write a function: optimize_schedule(trains_df, segments_df, conflicts_df)

Requirements:
1. Resolve conflicts by adjusting departure times
2. Optimization strategy:
   - Priority-based: higher priority trains get preference
   - Minimize total delay across all trains
   - Respect capacity constraints

3. Algorithm:
   - Greedy approach: process trains by priority (high to low)
   - For each train:
     * Calculate earliest conflict-free departure
     * Assign new time if needed
     * Update occupancy map
   - Time complexity: O(n²) acceptable for n=200

4. Constraints:
   - Can delay trains but not advance them
   - Maximum delay per train: 120 minutes
   - Express trains can be delayed max 30 minutes
   - Maintain minimum 10-minute separation

5. Return:
   - Optimized schedule DataFrame:
     ['train_id', 'original_departure', 'optimized_departure',
      'delay_minutes', 'estimated_arrival', 'conflicts_resolved']
   - Optimization metrics:
     {
       'conflicts_resolved': int,
       'remaining_conflicts': int,
       'total_delay_minutes': int,
       'avg_delay_minutes': float,
       'trains_delayed': int,
       'express_delays': int
     }

Example:
>>> optimized_schedule, metrics = optimize_schedule(trains, segments, conflicts)
>>> print(metrics)
{
  'conflicts_resolved': 45,
  'remaining_conflicts': 2,
  'total_delay_minutes': 1840,
  'avg_delay_minutes': 9.2,
  'trains_delayed': 68,
  'express_delays': 4
}


PART 3 (20 minutes): Dynamic Rescheduling
------------------------------------------
Write a function: handle_delay_cascade(schedule_df, delay_event)

delay_event = {
    'train_id': 'TRAIN-0042',
    'delay_minutes': 45,
    'affected_segment': 'SEG-015',
    'cause': 'mechanical_issue'
}

Requirements:
1. Identify downstream impacts:
   - Which trains are affected by this delay?
   - What conflicts does this create?
   - Cascade effect through network

2. Re-optimize affected portion of schedule:
   - Only modify trains after the delayed train
   - Minimize ripple effect
   - Prioritize express trains

3. Calculate business impact:
   - Lost revenue (delay penalties)
   - Customer satisfaction impact
   - Resource utilization

4. Return:
   - Updated schedule for affected trains
   - Cascade analysis:
     {
       'directly_affected_trains': int,
       'cascade_depth': int (how many "hops"),
       'total_additional_delay': int (minutes),
       'estimated_revenue_impact': float,
       'recommended_actions': list[str]
     }

Example:
>>> updated_schedule, cascade = handle_delay_cascade(schedule, delay_event)
>>> print(cascade)
{
  'directly_affected_trains': 8,
  'cascade_depth': 3,
  'total_additional_delay': 180,
  'estimated_revenue_impact': -12500,
  'recommended_actions': [
    'Hold TRAIN-0051 for 15 minutes',
    'Reroute TRAIN-0063 to parallel track',
    'Notify customers of delays'
  ]
}


CONSTRAINTS:
- Efficient algorithms (sorting, priority queues)
- Handle real-time updates
- Scale to 1000+ trains
- Production-ready code

EVALUATION:
- Conflict detection accuracy: 35%
- Optimization quality: 40%
- Algorithm efficiency: 25%
'''