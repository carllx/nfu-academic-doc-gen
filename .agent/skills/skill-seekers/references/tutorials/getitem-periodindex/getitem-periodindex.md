# How To: Getitem Periodindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem periodindex

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign rng = period_range(...)

```python
rng = period_range('1/1/2000', periods=5)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 5)), columns=rng)
```

### Step 3: Assign ts = value

```python
ts = df[rng[0]]
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts, df.iloc[:, 0])
```

### Step 5: Assign ts = value

```python
ts = df['1/1/2000']
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts, df.iloc[:, 0])
```


## Complete Example

```python
# Workflow
rng = period_range('1/1/2000', periods=5)
df = DataFrame(np.random.default_rng(2).standard_normal((10, 5)), columns=rng)
ts = df[rng[0]]
tm.assert_series_equal(ts, df.iloc[:, 0])
ts = df['1/1/2000']
tm.assert_series_equal(ts, df.iloc[:, 0])
```

## Next Steps


---

*Source: test_getitem.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*