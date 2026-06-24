# How To: Date Index Query

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date index query

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

**Verification:**
```python
assert return_value is None
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
df['dates3'] = date_range('1/1/2014', periods=n)
```

### Step 5: Assign return_value = df.set_index(...)

```python
return_value = df.set_index('dates1', inplace=True, drop=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 6: Assign res = df.query(...)

```python
res = df.query('(index < 20130101) & (20130101 < dates3)', engine=engine, parser=parser)
```

### Step 7: Assign expec = value

```python
expec = df[(df.index < '20130101') & ('20130101' < df.dates3)]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```


## Complete Example

```python
# Workflow
n = 10
df = DataFrame(np.random.default_rng(2).standard_normal((n, 3)))
df['dates1'] = date_range('1/1/2012', periods=n)
df['dates3'] = date_range('1/1/2014', periods=n)
return_value = df.set_index('dates1', inplace=True, drop=True)
assert return_value is None
res = df.query('(index < 20130101) & (20130101 < dates3)', engine=engine, parser=parser)
expec = df[(df.index < '20130101') & ('20130101' < df.dates3)]
tm.assert_frame_equal(res, expec)
```

## Next Steps


---

*Source: test_query_eval.py:826 | Complexity: Advanced | Last updated: 2026-06-02*