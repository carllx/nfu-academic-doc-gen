# How To: Date Query With Nat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date query with NaT

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

### Step 1: Assign n = 10

```python
n = 10
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((n, 3)))
```

### Step 3: Assign unknown = date_range(...)

```python
df['dates1'] = date_range('1/1/2012', periods=n)
```

### Step 4: Assign unknown = date_range(...)

```python
df['dates2'] = date_range('1/1/2013', periods=n)
```

### Step 5: Assign unknown = date_range(...)

```python
df['dates3'] = date_range('1/1/2014', periods=n)
```

### Step 6: Assign unknown = value

```python
df.loc[np.random.default_rng(2).random(n) > 0.5, 'dates1'] = pd.NaT
```

### Step 7: Assign unknown = value

```python
df.loc[np.random.default_rng(2).random(n) > 0.5, 'dates3'] = pd.NaT
```

### Step 8: Assign res = df.query(...)

```python
res = df.query('(dates1 < 20130101) & (20130101 < dates3)', engine=engine, parser=parser)
```

### Step 9: Assign expec = value

```python
expec = df[(df.dates1 < '20130101') & ('20130101' < df.dates3)]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```


## Complete Example

```python
# Workflow
n = 10
df = DataFrame(np.random.default_rng(2).standard_normal((n, 3)))
df['dates1'] = date_range('1/1/2012', periods=n)
df['dates2'] = date_range('1/1/2013', periods=n)
df['dates3'] = date_range('1/1/2014', periods=n)
df.loc[np.random.default_rng(2).random(n) > 0.5, 'dates1'] = pd.NaT
df.loc[np.random.default_rng(2).random(n) > 0.5, 'dates3'] = pd.NaT
res = df.query('(dates1 < 20130101) & (20130101 < dates3)', engine=engine, parser=parser)
expec = df[(df.dates1 < '20130101') & ('20130101' < df.dates3)]
tm.assert_frame_equal(res, expec)
```

## Next Steps


---

*Source: test_query_eval.py:812 | Complexity: Advanced | Last updated: 2026-06-02*