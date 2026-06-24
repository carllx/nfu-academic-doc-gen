# How To: Date Query No Attribute Access

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date query no attribute access

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
```

### Step 2: Assign unknown = date_range(...)

```python
df['dates1'] = date_range('1/1/2012', periods=5)
```

### Step 3: Assign unknown = date_range(...)

```python
df['dates2'] = date_range('1/1/2013', periods=5)
```

### Step 4: Assign unknown = date_range(...)

```python
df['dates3'] = date_range('1/1/2014', periods=5)
```

### Step 5: Assign res = df.query(...)

```python
res = df.query('(dates1 < 20130101) & (20130101 < dates3)', engine=engine, parser=parser)
```

### Step 6: Assign expec = value

```python
expec = df[(df.dates1 < '20130101') & ('20130101' < df.dates3)]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
df['dates1'] = date_range('1/1/2012', periods=5)
df['dates2'] = date_range('1/1/2013', periods=5)
df['dates3'] = date_range('1/1/2014', periods=5)
res = df.query('(dates1 < 20130101) & (20130101 < dates3)', engine=engine, parser=parser)
expec = df[(df.dates1 < '20130101') & ('20130101' < df.dates3)]
tm.assert_frame_equal(res, expec)
```

## Next Steps


---

*Source: test_query_eval.py:801 | Complexity: Intermediate | Last updated: 2026-06-02*