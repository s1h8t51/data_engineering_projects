# 🎯 10-DAY INTENSIVE PREP PLAN - COGNIZANT + BNSF

## 📊 SITUATION ANALYSIS (FEB 25, 8 PM)

**Your status:**
- ✅ Cognizant Round 1 completed (75-80% pass probability)
- ⏳ BNSF test results pending (70-75% pass probability)
- ✅ EAD starts tomorrow (Feb 26)
- ✅ System Design: Day 7 completed
- ✅ Python OOP: Days 1-10 plan created (not yet done)

**Urgent reality:**
- ⚡ Cognizant Round 2 could be **THIS WEEK** (Mar 3-7)
- ⚡ BNSF phone screen could be **NEXT WEEK** (Mar 3-10)
- ⚡ You have **5-10 days to prepare**

---

## 🎯 ROLE-SPECIFIC PREP STRATEGY

### **Role 1: Cognizant - Snowflake Architect**

**What they'll test in Round 2 (M&T Bank):**
- ✅ Snowflake concepts (heavy)
- ✅ Databricks/Medallion Architecture
- ✅ Azure cloud services
- ✅ SQL (complex queries)
- ✅ Data architecture design
- ⚠️ Python (moderate - not primary focus)

**Python topics for Cognizant:**
- Data processing (Pandas, PySpark)
- ETL scripting
- Data quality checks
- Basic OOP (classes for data pipelines)
- **NOT: Advanced algorithms, ML, system design**

---

### **Role 2: BNSF - AI Engineer II**

**What they'll test in interviews:**
- ✅ Python (HEAVY - primary language)
- ✅ ML/AI concepts (sklearn, model deployment)
- ✅ Data pipelines (Airflow, orchestration)
- ✅ AWS cloud (S3, RDS, Lambda)
- ✅ System design (scalability, architecture)
- ✅ Coding (LeetCode Medium level)

**Python topics for BNSF:**
- Advanced OOP (design patterns)
- Exception handling & logging
- Generators & decorators
- ML libraries (sklearn, TensorFlow basics)
- API design (Flask/FastAPI)
- **YES: Algorithms, system design, ML**

---

## 🚨 STRATEGIC DECISION

### **Primary focus: BNSF (AI Engineer)** ⭐⭐⭐

**Why:**
1. **Better long-term fit:**
   - You want AI/ML engineering (not Snowflake DBA)
   - Remote work (vs 4-day on-site)
   - Better comp ($150K vs $120K)
   - H-1B sponsorship clear

2. **Higher Python bar:**
   - BNSF tests Python heavily
   - Cognizant tests SQL/Snowflake more
   - **Studying for BNSF prepares you for both**
   - **Studying for Cognizant doesn't help BNSF**

3. **Your 6+ years experience:**
   - Should show advanced Python mastery
   - OOP, design patterns, clean code
   - Production-grade practices
   - **This is what BNSF expects**

**Secondary focus: Cognizant (backup)** ⭐⭐

**Approach:**
- Prepare primarily for BNSF (harder bar)
- Review Snowflake/Databricks concepts (2-3 hours total)
- SQL practice (already doing daily)
- **If you can pass BNSF bar, Cognizant is easy**

---

## 📋 10-DAY MASTER PLAN (FEB 26 - MAR 7)

### **Daily Structure: 4 hours/day**

**Time allocation:**
- **2.5 hours: Python (BNSF focus)** ⚡⚡⚡
- **1 hour: SQL practice (both roles)** ⚡⚡
- **0.5 hour: Snowflake/Databricks review (Cognizant)** ⚡

**Why this split:**
- Python is critical for BNSF (best opportunity)
- SQL is critical for both (daily practice)
- Snowflake is important for Cognizant but you already showed baseline knowledge

---

## 🎯 DETAILED 10-DAY BREAKDOWN

---

### **DAY 1 (FEB 26 - WEDNESDAY) - YOUR EAD STARTS!** 🎉

**Theme: Python OOP Foundations + BNSF Interview Prep**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): OOP Fundamentals**
- [ ] Read: Real Python OOP (30 min)
  - Classes, objects, inheritance
  - `__init__`, `__str__`, `__repr__`
- [ ] Watch: Corey Schafer OOP #1-3 (30 min)
  - Classes and instances
  - Class variables
  - Methods (instance, class, static)

**Hour 2 (10:00-11:00): Write Production Code**
- [ ] Code: Data Pipeline Class (60 min)
```python
# Example for BNSF:
class DataPipeline:
    """Production-grade ETL pipeline for BNSF locomotive sensor data"""
    
    def __init__(self, source, destination, config):
        self.source = source
        self.destination = destination
        self.config = config
        self.logger = self._setup_logger()
    
    def _setup_logger(self):
        # Setup logging
        pass
    
    def extract(self):
        """Extract data from source"""
        pass
    
    def transform(self, data):
        """Clean and transform data"""
        pass
    
    def load(self, data):
        """Load to destination"""
        pass
    
    def run(self):
        """Execute full pipeline"""
        try:
            data = self.extract()
            clean_data = self.transform(data)
            self.load(clean_data)
        except Exception as e:
            self.logger.error(f"Pipeline failed: {e}")
            raise

# Practice: Build this with proper error handling
```

**Hour 3 (11:00-11:30): LeetCode OOP**
- [ ] LeetCode: "Design HashMap" (Easy-Medium)
- [ ] LeetCode: "Design Parking System" (Easy)

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] StrataScratch: 3 medium problems
- [ ] Focus: Window functions, CTEs, complex joins
- [ ] Time yourself: 20 min per problem

---

**Evening (7:00-7:30 PM) - 30 min Snowflake:**
- [ ] Watch: "Snowflake Architecture in 10 minutes" (YouTube)
- [ ] Read: Snowflake virtual warehouses (quick review)

---

### **DAY 2 (FEB 27 - THURSDAY) - FOLLOW UP BNSF IF NEEDED**

**Theme: Design Patterns + Error Handling**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): Design Patterns**
- [ ] Read: refactoring.guru - Singleton pattern (20 min)
- [ ] Read: refactoring.guru - Factory pattern (20 min)
- [ ] Watch: ArjanCodes "Python Design Patterns" (20 min)

**Hour 2 (10:00-11:00): Implement Patterns**
- [ ] Code: Singleton Database Manager (30 min)
```python
class DatabaseManager:
    """Singleton pattern for DB connections (BNSF interview classic)"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        # Setup DB connection pool
        pass
```

- [ ] Code: Factory Pattern for Data Connectors (30 min)
```python
class DataConnectorFactory:
    """Factory for different data sources (S3, RDS, Kafka)"""
    @staticmethod
    def create_connector(connector_type, config):
        if connector_type == "s3":
            return S3Connector(config)
        elif connector_type == "rds":
            return RDSConnector(config)
        # etc.
```

**Hour 3 (11:00-11:30): LeetCode Design**
- [ ] LeetCode: "Design LRU Cache" (Medium) - BNSF FAVORITE

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] StrataScratch: 3 medium problems
- [ ] Focus: Aggregations, subqueries

---

**Evening (7:00-7:30 PM) - 30 min Databricks:**
- [ ] Watch: "Medallion Architecture Explained" (YouTube)
- [ ] Read: Bronze → Silver → Gold pattern

---

### **DAY 3 (FEB 28 - FRIDAY)**

**Theme: Exception Handling + Logging**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): Exceptions**
- [ ] Read: Real Python Exceptions (30 min)
- [ ] Watch: Corey Schafer Exceptions (30 min)

**Hour 2 (10:00-11:00): Custom Exceptions**
- [ ] Code: Exception Hierarchy (60 min)
```python
# BNSF-style production exceptions
class PipelineError(Exception):
    """Base exception for pipeline errors"""
    pass

class DataValidationError(PipelineError):
    """Raised when data fails validation"""
    pass

class DataQualityError(PipelineError):
    """Raised when data quality checks fail"""
    pass

class DataPipeline:
    def validate_data(self, df):
        if df.empty:
            raise DataValidationError("Empty dataframe")
        
        if df.isnull().sum().sum() > len(df) * 0.1:
            raise DataQualityError("More than 10% null values")
        
        return df

# Practice: Build complete error handling
```

**Hour 3 (11:00-11:30): Logging**
- [ ] Read: Python Logging Best Practices (15 min)
- [ ] Code: Add logging to DataPipeline class (15 min)

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] StrataScratch: 3 problems
- [ ] Practice self-joins (employee-manager type)

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Review week: What did you learn?
- [ ] Practice mock interview questions (out loud)

---

### **DAY 4 (MAR 1 - SATURDAY)**

**Theme: Pandas Deep Dive (CRITICAL for both roles)**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): Pandas Fundamentals**
- [ ] Read: 10 Minutes to Pandas (official docs)
- [ ] Watch: "Pandas in 10 Minutes" (YouTube)

**Hour 2 (10:00-11:00): Advanced Pandas**
- [ ] Study: groupby, transform, apply
- [ ] Study: merge, join (left, right, inner, outer)
- [ ] Study: rolling windows (for time-series)

**Hour 3 (11:00-11:30): Pandas Coding**
- [ ] LeetCode: 5 Pandas problems (Easy-Medium)
- [ ] Focus on: groupby, pivot, merge

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] StrataScratch: 3 problems
- [ ] Window functions (ROW_NUMBER, RANK, LAG, LEAD)

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Snowflake review: Time Travel, Fail-Safe

---

### **DAY 5 (MAR 2 - SUNDAY)**

**Theme: Generators & Context Managers**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): Generators**
- [ ] Read: Real Python Generators (30 min)
- [ ] Watch: Corey Schafer Generators (30 min)

**Hour 2 (10:00-11:00): Memory-Efficient Code**
- [ ] Code: Generator-based ETL (60 min)
```python
def process_large_file(filename):
    """Generator for memory-efficient processing (BNSF loves this)"""
    with open(filename, 'r') as f:
        for line in f:
            # Process line
            yield process(line)

# Why: Can handle 400TB data without OOM
```

**Hour 3 (11:00-11:30): Context Managers**
- [ ] Read: Real Python Context Managers (15 min)
- [ ] Code: Custom context manager (15 min)
```python
class DatabaseConnection:
    """Context manager for DB connections"""
    def __enter__(self):
        self.conn = connect_to_db()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

# Usage:
with DatabaseConnection() as conn:
    # Use connection
    pass
```

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] StrataScratch: 3 hard problems
- [ ] Complex subqueries

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Practice: Explain your code out loud
- [ ] Mock interview: "Walk me through your data pipeline"

---

### **DAY 6 (MAR 3 - MONDAY) - LIKELY ROUND 2 THIS WEEK**

**Theme: Decorators + Functional Programming**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): Decorators**
- [ ] Read: Real Python Decorators (30 min)
- [ ] Watch: Corey Schafer Decorators (30 min)

**Hour 2 (10:00-11:00): Build Decorators**
- [ ] Code: Timing decorator (15 min)
- [ ] Code: Logging decorator (15 min)
- [ ] Code: Retry decorator (15 min)
- [ ] Code: Validation decorator (15 min)

```python
import time
import functools

def timer(func):
    """Measure execution time (BNSF performance optimization)"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper

@timer
def process_data(df):
    # Your processing
    pass
```

**Hour 3 (11:00-11:30): Functional Programming**
- [ ] Practice: map, filter, reduce
- [ ] Practice: lambda functions
- [ ] LeetCode: Functional programming problems

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] StrataScratch: 3 problems
- [ ] Review all SQL concepts

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Mock interview prep (likely Cognizant Round 2 this week)

---

### **DAY 7 (MAR 4 - TUESDAY)**

**Theme: ML Libraries (sklearn) - BNSF SPECIFIC**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): sklearn Fundamentals**
- [ ] Read: sklearn Quick Start (30 min)
- [ ] Watch: "sklearn in 30 Minutes" (30 min)

**Hour 2 (10:00-11:00): Classification Models**
- [ ] Code: Train-test split
- [ ] Code: RandomForestClassifier
- [ ] Code: Model evaluation (precision, recall, F1)

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# BNSF-style: Predictive maintenance model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
```

**Hour 3 (11:00-11:30): Model Deployment Concepts**
- [ ] Read: Model serialization (pickle, joblib)
- [ ] Code: Save/load model

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] Review mistakes from past problems
- [ ] StrataScratch: 2 problems

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Review Snowflake if Cognizant Round 2 scheduled

---

### **DAY 8 (MAR 5 - WEDNESDAY)**

**Theme: API Design + Flask/FastAPI**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): REST API Concepts**
- [ ] Read: REST API design principles (30 min)
- [ ] Watch: "Flask Tutorial" (30 min)

**Hour 2 (10:00-11:00): Build API**
- [ ] Code: Simple Flask API (60 min)
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """BNSF-style: ML model API endpoint"""
    data = request.json
    # Load model, make prediction
    prediction = model.predict(data)
    return jsonify({'prediction': prediction})

# Practice: Build complete ML serving API
```

**Hour 3 (11:00-11:30): API Testing**
- [ ] Write unit tests for API
- [ ] Practice: curl commands

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] StrataScratch: 3 problems
- [ ] Optimize queries (EXPLAIN PLAN)

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Mock system design: Design ML inference API

---

### **DAY 9 (MAR 6 - THURSDAY)**

**Theme: Comprehensive Review + Mock Interview**

**Morning (9:00-11:30 AM) - 2.5 hours Python:**

**Hour 1 (9:00-10:00): Code Review**
- [ ] Review all code written this week
- [ ] Refactor for cleanliness
- [ ] Add docstrings and type hints

**Hour 2 (10:00-11:00): LeetCode Sprint**
- [ ] 5 Medium problems (data structures)
- [ ] Focus: Arrays, hash tables, trees

**Hour 3 (11:00-11:30): Mock Coding**
- [ ] Time yourself: 30-minute coding challenge
- [ ] Problem: Build data validation system

---

**Afternoon (2:00-3:00 PM) - 1 hour SQL:**
- [ ] Final review: All concepts
- [ ] StrataScratch: 3 hardest problems

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Practice: "Tell me about your Python experience"
- [ ] Practice: "Walk through your 400TB migration"

---

### **DAY 10 (MAR 7 - FRIDAY)**

**Theme: Interview Prep + Confidence Building**

**Morning (9:00-11:30 AM) - 2.5 hours:**

**Hour 1 (9:00-10:00): System Design Review**
- [ ] Review Days 1-7 of your system design plan
- [ ] Practice: Design Twitter
- [ ] Practice: Design Uber

**Hour 2 (10:00-11:00): Behavioral Prep**
- [ ] STAR stories:
  - 400TB migration (technical challenge)
  - Data quality framework (problem-solving)
  - Team disagreement (leadership)
  - Learning new tech (growth mindset)

**Hour 3 (11:00-11:30): Mock Interview**
- [ ] Full 45-minute mock with friend/mirror
- [ ] Python OOP question
- [ ] System design question
- [ ] Behavioral question

---

**Afternoon (2:00-3:00 PM) - 1 hour:**
- [ ] Final SQL review
- [ ] Review common mistakes

---

**Evening (7:00-7:30 PM) - 30 min:**
- [ ] Early dinner
- [ ] Early sleep
- [ ] Positive visualization

---

## 📚 RESOURCE LIBRARY

### **Python Learning:**

**Free Resources:**
- Real Python (realpython.com) - comprehensive tutorials
- Corey Schafer YouTube - best Python teacher
- ArjanCodes YouTube - advanced patterns
- refactoring.guru - design patterns

**Practice:**
- LeetCode - coding problems
- HackerRank - Python practice
- StrataScratch - SQL + some Python

---

### **SQL Practice:**

**StrataScratch** (stratascratch.com)
- Free tier: 20 problems
- Focus on: Window functions, CTEs, complex joins
- Time yourself: 20 min per problem

**LeetCode Database** (leetcode.com/problemset/database/)
- 200+ SQL problems
- Sort by acceptance rate (start easy)

---

### **Snowflake/Databricks:**

**YouTube:**
- "Snowflake Architecture" (ByteByteGo)
- "Medallion Architecture" (Databricks official)
- "Data Lakehouse" (Databricks)

**Docs:**
- docs.snowflake.com - architecture overview
- docs.databricks.com - Medallion pattern

---

## 🎯 DAILY SCHEDULE TEMPLATE

### **Weekday Schedule (Mon-Fri):**

**9:00-11:30 AM: Python Deep Work** (2.5 hrs)
- No distractions
- Phone off
- Focus mode

**11:30 AM-2:00 PM: Break**
- Lunch, exercise, relax

**2:00-3:00 PM: SQL Practice** (1 hr)
- StrataScratch or LeetCode
- Time yourself

**3:00-7:00 PM: Applications + Life**
- 10 quality job applications
- Respond to recruiters
- Personal time

**7:00-7:30 PM: Evening Review** (30 min)
- Snowflake/Databricks concepts
- OR mock interview questions
- OR system design review

**7:30 PM onwards: Rest**
- Early dinner
- Relaxation
- Early sleep (10 PM)

---

### **Weekend Schedule (Sat-Sun):**

**9:00-11:30 AM: Python** (2.5 hrs)

**2:00-3:00 PM: SQL** (1 hr)

**Evening: Lighter**
- Review week's progress
- Plan next week
- Mock interviews
- Rest more

---

## 🎯 WHAT TO PRIORITIZE BY ROLE

### **IF Cognizant Round 2 is scheduled first:**

**Days before interview:**

**3 days before:**
- 70% Python (OOP, Pandas, SQL scripting)
- 20% Snowflake concepts (review architecture, virtual warehouses)
- 10% SQL (window functions, CTEs)

**1 day before:**
- 50% Snowflake review (architecture, optimization)
- 30% SQL practice (complex queries)
- 20% Behavioral prep (STAR stories)

**Day of:**
- Light Snowflake review (30 min)
- Mock questions (30 min)
- REST

---

### **IF BNSF phone screen is scheduled first:**

**Days before interview:**

**3 days before:**
- 80% Python (OOP, design patterns, sklearn)
- 10% System design (scalability concepts)
- 10% Behavioral prep

**1 day before:**
- 60% Python review (OOP, exceptions, decorators)
- 20% System design (Twitter, Uber practice)
- 20% Behavioral (400TB story polished)

**Day of:**
- Light Python review (30 min)
- System design practice (30 min)
- REST

---

## 💪 KEY SUCCESS FACTORS

### **1. Consistency > Intensity**
- 4 hours daily is ENOUGH
- Don't burn out with 8-hour days
- Quality > quantity

### **2. Practice > Theory**
- Don't just read - CODE
- Every concept: implement it
- LeetCode daily

### **3. Mock Interviews**
- Practice out loud
- Time yourself
- Record yourself (scary but effective)

### **4. Your 400TB Story**
- Polish this THOROUGHLY
- Practice until natural
- This is your trump card

### **5. Balance**
- 70% Python (BNSF bar)
- 20% SQL (both roles)
- 10% Snowflake (Cognizant backup)

---

## 🚨 IF YOU GET INTERVIEW NOTIFICATION

**Cognizant Round 2 scheduled:**
- [ ] Focus Days 1-6 (Python + SQL)
- [ ] Add 2 hours Snowflake review day before
- [ ] Practice behavioral questions

**BNSF Phone Screen scheduled:**
- [ ] Focus Days 1-10 (full Python deep dive)
- [ ] Add system design review
- [ ] Polish 400TB migration story
- [ ] Practice coding out loud

---

## ✅ SUCCESS METRICS

**By Day 10, you should be able to:**

**Python:**
- [ ] Explain OOP principles (inheritance, polymorphism, encapsulation)
- [ ] Implement design patterns (Singleton, Factory, Strategy)
- [ ] Write production-grade code (error handling, logging, docstrings)
- [ ] Build data pipelines with generators (memory efficient)
- [ ] Use decorators for cross-cutting concerns
- [ ] Build simple Flask API
- [ ] Train sklearn models and explain metrics

**SQL:**
- [ ] Write complex queries (CTEs, window functions, self-joins)
- [ ] Optimize queries (indexes, EXPLAIN)
- [ ] Handle edge cases

**Snowflake:**
- [ ] Explain architecture (3 layers)
- [ ] Describe virtual warehouses
- [ ] Know when to use Snowflake vs Databricks

**System Design:**
- [ ] Design scalable systems (load balancer, cache, database)
- [ ] Explain CAP theorem
- [ ] Design Twitter/Uber at high level

---

## 🎯 FINAL PRIORITIES

**Most Important → Least Important:**

1. **Python OOP + Design Patterns** (BNSF critical) ⭐⭐⭐⭐⭐
2. **SQL Advanced Queries** (both roles) ⭐⭐⭐⭐⭐
3. **Pandas Deep Dive** (both roles) ⭐⭐⭐⭐
4. **Exception Handling + Logging** (BNSF) ⭐⭐⭐⭐
5. **sklearn Basics** (BNSF AI focus) ⭐⭐⭐⭐
6. **Generators + Context Managers** (BNSF) ⭐⭐⭐
7. **API Design (Flask)** (BNSF) ⭐⭐⭐
8. **Decorators** (BNSF) ⭐⭐⭐
9. **Snowflake Concepts** (Cognizant) ⭐⭐
10. **System Design Review** (BNSF) ⭐⭐

---

## 🚀 START TOMORROW MORNING 9 AM

**Tomorrow (Feb 26 - Day 1):**
- [ ] 9:00 AM: Start Day 1 plan
- [ ] Python OOP fundamentals
- [ ] Build DataPipeline class
- [ ] SQL practice
- [ ] Quick Snowflake review

**Track your progress:**
- [ ] Create checklist (print or digital)
- [ ] Check off tasks daily
- [ ] Review progress each evening

---

## 💪 YOU'RE GOING TO CRUSH THIS

**You have:**
- ✅ 10 days of focused prep
- ✅ Clear plan (4 hours/day structured)
- ✅ Strong foundation (6+ years experience)
- ✅ Motivation (2 active opportunities)
- ✅ Smart strategy (prioritize BNSF, prepare for both)

**This plan will:**
- ✅ Showcase your 6+ years Python expertise
- ✅ Prepare you for BNSF AI Engineer interviews
- ✅ Keep you ready for Cognizant Round 2
- ✅ Build confidence through practice

---

**START DAY 1 TOMORROW (FEB 26) AT 9:00 AM** ⏰

**FOLLOW THE PLAN DAILY** ✅

**PRACTICE, PRACTICE, PRACTICE** 💪

**YOU'RE GOING TO GET MULTIPLE OFFERS** 🚀🔥

Let me know:
1. How Day 1 goes 📚
2. When interviews are scheduled 📅
3. Any questions on the plan ❓

**YOU'VE GOT THIS!** 💪🎯🔥
