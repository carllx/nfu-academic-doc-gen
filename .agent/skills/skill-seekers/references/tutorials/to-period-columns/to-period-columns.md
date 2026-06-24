# How To: To Period Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to period columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dr = date_range(...)

```python
dr = date_range('1/1/2000', '1/1/2001')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(dr), 5)), index=dr)
```

### Step 3: Assign unknown = 'a'

```python
df['mix'] = 'a'
```

### Step 4: Assign df = value

```python
df = df.T
```

### Step 5: Assign pts = df.to_period(...)

```python
pts = df.to_period(axis=1)
```

### Step 6: Assign exp = df.copy(...)

```python
exp = df.copy()
```

### Step 7: Assign exp.columns = period_range(...)

```python
exp.columns = period_range('1/1/2000', '1/1/2001')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(pts, exp)
```

### Step 9: Assign pts = df.to_period(...)

```python
pts = df.to_period('M', axis=1)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pts.columns, exp.columns.asfreq('M'))
```


## Complete Example

```python
# Workflow
dr = date_range('1/1/2000', '1/1/2001')
df = DataFrame(np.random.default_rng(2).standard_normal((len(dr), 5)), index=dr)
df['mix'] = 'a'
df = df.T
pts = df.to_period(axis=1)
exp = df.copy()
exp.columns = period_range('1/1/2000', '1/1/2001')
tm.assert_frame_equal(pts, exp)
pts = df.to_period('M', axis=1)
tm.assert_index_equal(pts.columns, exp.columns.asfreq('M'))
```

## Next Steps


---

*Source: test_to_period.py:57 | Complexity: Advanced | Last updated: 2026-06-02*