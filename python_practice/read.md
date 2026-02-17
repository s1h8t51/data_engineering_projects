# 🎯 FREE RESOURCES TO MASTER PYTHON IN 15 DAYS

## 📊 YOUR SKILL GAP ANALYSIS

**SQL: 9/10 - YOU'RE ALREADY STRONG** ✅
- Just practice 30 min/day to maintain
- Focus on speed and edge cases

**Python: NEEDS WORK** ⚠️
- Pandas: 6/10 (decent, needs polish)
- OOP: 2/10 (critical gap - study first!)
- Error handling: 2/10 (important for Citi)
- Generators: 1/10 (study last)

**Priority order:**
1. OOP & Design Patterns (2/10 → need 8/10)
2. Error Handling & Logging (2/10 → need 8/10)
3. Pandas Operations (6/10 → need 9/10)
4. Generators & Context Managers (1/10 → need 7/10)

---

## 🆓 FREE RESOURCES BY TOPIC

---

## 🔴 TOPIC 1: OOP & DESIGN PATTERNS (2/10 → URGENT)

### **Free Resources:**

**1. Real Python - OOP (BEST FREE RESOURCE)** ⭐⭐⭐
- URL: realpython.com/python3-object-oriented-programming
- URL: realpython.com/inheritance-composition-python
- URL: realpython.com/python-super
- **Why:** Clear explanations, practical examples
- **Time:** 3-4 hours total

**2. Python Design Patterns - GitHub** ⭐⭐⭐
- URL: github.com/faif/python-patterns
- **Why:** Code examples for every pattern
- **What:** Singleton, Factory, Observer, Strategy, Decorator
- **Time:** 2-3 hours

**3. Refactoring Guru (FREE)** ⭐⭐⭐
- URL: refactoring.guru/design-patterns/python
- **Why:** Visual explanations + Python code
- **Patterns to study:**
  - Singleton (database connections)
  - Factory (creating objects)
  - Strategy (algorithm selection)
  - Observer (event handling)
  - Decorator (adding functionality)
- **Time:** 4-5 hours

**4. YouTube: Arjan Codes** ⭐⭐⭐
- URL: youtube.com/@ArjanCodes
- **Videos to watch:**
  - "Python OOP Tutorial" (45 min)
  - "Python Design Patterns" series
  - "SOLID Principles in Python" (30 min)
- **Time:** 3-4 hours

**5. FreeCodeCamp - Python OOP** ⭐⭐
- URL: youtube.com/watch?v=Ej_02ICOIgs
- **Why:** 2-hour comprehensive tutorial
- **Time:** 2 hours

---

### **OOP Practice Resources:**

**1. Exercism.io (Free)** ⭐⭐⭐
- URL: exercism.org/tracks/python
- **Why:** OOP-focused exercises with mentorship
- **Time:** 30 min/day

**2. HackerRank Python OOP** ⭐⭐
- URL: hackerrank.com/domains/python
- **Filter by:** OOP section
- **Time:** 1-2 hours

**3. LeetCode Design Problems** ⭐⭐⭐
- URL: leetcode.com
- **Search:** "Design" category problems
- Examples:
  - Design HashMap
  - Design LRU Cache
  - Design Logger Rate Limiter
- **Time:** 30 min/day

---

### **OOP Key Concepts to Master:**

```python
# Study in this order:

# WEEK 1, DAY 1: Classes & Objects
class DataPipeline:
    # __init__, __str__, __repr__
    # Instance vs class variables
    # Instance vs class vs static methods

# WEEK 1, DAY 2: Inheritance
class ETLPipeline(DataPipeline):
    # super(), method overriding
    # Multiple inheritance
    # MRO (Method Resolution Order)

# WEEK 1, DAY 3: Encapsulation
class Database:
    # Public, protected (_), private (__)
    # Properties (@property)
    # Getters and setters

# WEEK 1, DAY 4: Polymorphism
# Duck typing
# Abstract base classes

# WEEK 1, DAY 5: Design Patterns
# Singleton, Factory, Strategy, Observer
```

---

## 🟡 TOPIC 2: ERROR HANDLING & LOGGING (2/10 → URGENT)

### **Free Resources:**

**1. Real Python - Error Handling** ⭐⭐⭐
- URL: realpython.com/python-exceptions
- URL: realpython.com/the-most-diabolical-python-antipattern
- **Time:** 2 hours

**2. Real Python - Logging** ⭐⭐⭐
- URL: realpython.com/python-logging
- URL: realpython.com/python-logging-source-code
- **Why:** Industry standard logging patterns
- **Time:** 2 hours

**3. YouTube: Corey Schafer - Exceptions** ⭐⭐⭐
- URL: youtube.com/watch?v=NIWwJbo-9_8
- URL: youtube.com/watch?v=-ARI4Cz-awo (logging)
- **Why:** Clear, practical Python tutorials
- **Time:** 1.5 hours

**4. Python Official Docs** ⭐⭐
- URL: docs.python.org/3/library/logging.html
- URL: docs.python.org/3/tutorial/errors.html
- **Time:** 1-2 hours

---

### **Key Concepts to Master:**

```python
# 1. Custom exceptions (Citi will test this)
class DataPipelineError(Exception):
    pass

class ValidationError(DataPipelineError):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Validation failed for {field}: {message}")

class DatabaseConnectionError(DataPipelineError):
    pass

class DataQualityError(DataPipelineError):
    def __init__(self, row_count, error_rate):
        self.row_count = row_count
        self.error_rate = error_rate
        super().__init__(
            f"Quality check failed: {error_rate:.1%} error rate "
            f"on {row_count} rows"
        )

# 2. Try/except/else/finally pattern
def load_data_to_db(data, connection):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.executemany(INSERT_QUERY, data)
        connection.commit()
    except DatabaseConnectionError as e:
        connection.rollback()
        logger.error(f"Connection failed: {e}")
        raise
    except ValidationError as e:
        logger.warning(f"Validation issue: {e}")
        # Don't raise - continue with valid rows
    except Exception as e:
        connection.rollback()
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        raise DataPipelineError("Load failed") from e
    else:
        logger.info(f"Successfully loaded {len(data)} rows")
    finally:
        if cursor:
            cursor.close()

# 3. Professional logging setup
import logging
import logging.handlers

def setup_logging(log_level='INFO', log_file='pipeline.log'):
    logger = logging.getLogger('DataPipeline')
    logger.setLevel(log_level)
    
    # Format
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | '
        '%(filename)s:%(lineno)d | %(message)s'
    )
    
    # Console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    
    # File handler (rotating, max 10MB, keep 5 files)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=10*1024*1024, backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console)
    logger.addHandler(file_handler)
    
    return logger

# Usage
logger = setup_logging()
logger.info("Pipeline started")
logger.warning("Missing values detected: 5%")
logger.error("Connection timeout", exc_info=True)
logger.critical("Data corruption detected!")
```

---

## 🟢 TOPIC 3: PANDAS OPERATIONS (6/10 → POLISH)

### **Free Resources:**

**1. Pandas Official Documentation** ⭐⭐⭐
- URL: pandas.pydata.org/docs/user_guide/index.html
- **Focus sections:**
  - GroupBy
  - Merge/Join
  - Window functions
  - MultiIndex
- **Time:** 3-4 hours

**2. Real Python - Pandas Tutorials** ⭐⭐⭐
- URL: realpython.com/pandas-groupby
- URL: realpython.com/pandas-merge-join-and-concatenate
- URL: realpython.com/pandas-dataframe
- **Time:** 4-5 hours

**3. Kaggle Free Pandas Course** ⭐⭐⭐
- URL: kaggle.com/learn/pandas
- **Why:** Interactive, hands-on, free
- **Time:** 4-5 hours complete

**4. YouTube: Corey Schafer Pandas Series** ⭐⭐⭐
- URL: youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
- **Videos:** 10 videos on Pandas
- **Time:** 4-5 hours

**5. DataQuest Pandas Cheat Sheet** ⭐⭐
- URL: dataquest.io/blog/pandas-cheat-sheet
- **Why:** Quick reference during practice
- **Time:** 30 min review

---

### **Practice Platforms:**

**1. Kaggle Notebooks (Free)** ⭐⭐⭐
- URL: kaggle.com/notebooks
- **Why:** Real datasets, free compute
- **Practice:** Download financial datasets, practice operations
- **Time:** 1 hour/day

**2. LeetCode Pandas Problems** ⭐⭐⭐
- URL: leetcode.com/studyplan/30-days-of-pandas
- **Why:** Interview-style Pandas problems
- **Time:** 30 min/day

**3. StrataScratch** ⭐⭐⭐
- URL: stratascratch.com
- **Why:** Real company interview questions (SQL + Python)
- **Free tier:** 50+ problems
- **Companies:** Citi, JPMorgan, Goldman Sachs
- **Time:** 30 min/day

---

### **Pandas Key Operations to Master:**

```python
# FOCUS on these for Citi interview:

# 1. GroupBy (CRITICAL)
df.groupby(['account_type', 'month']).agg({
    'amount': ['sum', 'mean', 'count', 'std'],
    'transaction_id': 'nunique'
}).reset_index()

# 2. Window functions (CRITICAL)
df['rolling_avg'] = df.groupby('account_id')['amount']\
    .transform(lambda x: x.rolling(7).mean())

df['rank'] = df.groupby('account_id')['amount']\
    .rank(method='dense', ascending=False)

df['cumsum'] = df.groupby('account_id')['amount']\
    .transform('cumsum')

# 3. Merge/Join (CRITICAL)
# Left join
result = pd.merge(transactions, accounts, 
                  on='account_id', how='left')

# Multiple keys
result = pd.merge(df1, df2, 
                  left_on=['id', 'date'],
                  right_on=['ref_id', 'txn_date'])

# 4. Apply custom functions
def calculate_risk_score(group):
    if group['amount'].std() > 1000:
        return 'high'
    elif group['amount'].mean() > 500:
        return 'medium'
    return 'low'

df['risk'] = df.groupby('account_id').apply(calculate_risk_score)

# 5. Pivot tables
pivot = df.pivot_table(
    values='amount',
    index='customer_id',
    columns='transaction_type',
    aggfunc={'amount': ['sum', 'count']},
    fill_value=0
)
```

---

## 🔵 TOPIC 4: GENERATORS & CONTEXT MANAGERS (1/10)

### **Free Resources:**

**1. Real Python - Generators** ⭐⭐⭐
- URL: realpython.com/introduction-to-python-generators
- URL: realpython.com/python-iterators-iterables
- **Time:** 2-3 hours

**2. Real Python - Context Managers** ⭐⭐⭐
- URL: realpython.com/python-with-statement
- URL: realpython.com/python-contextlib-suppress
- **Time:** 2 hours

**3. YouTube: Corey Schafer** ⭐⭐⭐
- URL: youtube.com/watch?v=bD05uGo_sVI (generators)
- URL: youtube.com/watch?v=-aKFBoZpiqA (context managers)
- **Time:** 1 hour

---

### **Key Concepts:**

```python
# GENERATORS (memory efficient processing)

# 1. Generator function (use for large datasets)
def read_large_file(file_path, chunk_size=1000):
    """Read file in chunks - memory efficient"""
    with open(file_path) as f:
        while True:
            lines = list(islice(f, chunk_size))
            if not lines:
                break
            yield lines

# Usage
for chunk in read_large_file('transactions.csv', 1000):
    process_chunk(chunk)

# 2. Generator expression
# Instead of: [x**2 for x in range(1000000)]  # Uses lots of memory
squares = (x**2 for x in range(1000000))  # Memory efficient

# 3. Pipeline of generators (Citi use case)
def extract_transactions(file):
    for line in file:
        yield json.loads(line)

def validate_transactions(transactions):
    for t in transactions:
        if t['amount'] > 0 and t['account_id']:
            yield t

def transform_transactions(transactions):
    for t in transactions:
        t['amount_usd'] = t['amount'] / 100
        yield t

# Chain generators (memory efficient pipeline)
with open('transactions.json') as f:
    pipeline = transform_transactions(
        validate_transactions(
            extract_transactions(f)
        )
    )
    for transaction in pipeline:
        save_to_db(transaction)


# CONTEXT MANAGERS

# 1. Using contextlib (easiest)
from contextlib import contextmanager

@contextmanager
def database_connection(connection_string):
    conn = create_connection(connection_string)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

# Usage
with database_connection('postgresql://...') as conn:
    conn.execute("INSERT INTO ...")

# 2. Class-based context manager
class TimedOperation:
    def __init__(self, operation_name):
        self.operation_name = operation_name
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        logger.info(f"Starting: {self.operation_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        if exc_type:
            logger.error(f"Failed: {self.operation_name} ({elapsed:.2f}s)")
        else:
            logger.info(f"Completed: {self.operation_name} ({elapsed:.2f}s)")
        return False  # Don't suppress exceptions

# Usage
with TimedOperation("ETL Pipeline"):
    run_etl()
```

---



### **Afternoon (11 AM - 1 PM): Practice Problems**

**11:00 - 11:30 AM:** SQL (maintain 9/10)
- StrataScratch: 2-3 finance problems
- Keep your SQL sharp

**11:30 AM - 12:30 PM:** Python problems
- LeetCode/HackerRank: 2-3 problems
- Focus on your weak areas

**12:30 - 1:00 PM:** Review + notes
- What did you learn today?
- What's still confusing?

---

### **Evening (4 PM - 5 PM): System Design**

**4:00 - 5:00 PM:** System Design
- Continue your 30-day plan
- Read System Design Primer
- Watch ByteByteGo videos

---

## ✅ QUICK REFERENCE CHEAT SHEETS

### **OOP Cheat Sheet (Free):**
- URL: github.com/jwasham/coding-interview-university
- Section: Object-Oriented Design

### **Python Cheat Sheet:**
- URL: pythoncheatsheet.org
- URL: github.com/gto76/python-cheatsheet

### **Pandas Cheat Sheet:**
- URL: pandas.pydata.org/Pandas_Cheat_Sheet.pdf

### **SQL Cheat Sheet:**
- URL: sqltutorial.org/sql-cheat-sheet

---

## 💪 SUCCESS METRICS (15 DAYS)

**After 15 days, you should score:**

| Topic | Now | Target |
|-------|-----|--------|
| OOP & Patterns | 2/10 | 8/10 |
| Error Handling | 2/10 | 8/10 |
| Pandas | 6/10 | 9/10 |
| Generators | 1/10 | 7/10 |
| SQL | 9/10 | 9/10 (maintain) |
| System Design | 4/10 | 7/10 |

---

## 🚀 START TOMORROW MORNING

**Day 1 (Feb 17 - Presidents' Day):**

**9:00 AM:**
- [ ] Open: realpython.com/python3-object-oriented-programming
- [ ] Read for 1 hour

**10:00 AM:**
- [ ] Open: youtube.com/@ArjanCodes
- [ ] Watch OOP tutorial

**11:00 AM:**
- [ ] Open your code editor
- [ ] Write DataPipeline class from scratch

**11:30 AM:**
- [ ] Open: stratascratch.com
- [ ] Solve 2 SQL problems

**12:30 PM:**
- [ ] System Design reading (30 min)

**Done by 1 PM** ✅

---

**YOU HAVE 15 DAYS TO GO FROM 2/10 → 8/10 ON PYTHON** 💪

**That's absolutely achievable with 4 hours/day** ✅

**SQL is already 9/10 - just maintain** ✅

**System design is running parallel** ✅

**START TOMORROW MORNING AT 9 AM** 🚀

Let me know if you need practice problems for any specific topic! 🎯
