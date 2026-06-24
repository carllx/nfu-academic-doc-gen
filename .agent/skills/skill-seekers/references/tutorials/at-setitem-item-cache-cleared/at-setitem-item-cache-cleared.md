# How To: At Setitem Item Cache Cleared

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at setitem item cache cleared

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(index=[0])
```

### Step 2: Assign unknown = 1

```python
df['x'] = 1
```

### Step 3: Assign unknown = 2

```python
df['cost'] = 2
```

### Step 4: df['cost']

```python
df['cost']
```

### Step 5: df.loc[[0]]

```python
df.loc[[0]]
```

### Step 6: Assign unknown = 4

```python
df.at[0, 'x'] = 4
```

### Step 7: Assign unknown = 789

```python
df.at[0, 'cost'] = 789
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [4], 'cost': 789}, index=[0])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['cost'], expected['cost'])
```


## Complete Example

```python
# Workflow
df = DataFrame(index=[0])
df['x'] = 1
df['cost'] = 2
df['cost']
df.loc[[0]]
df.at[0, 'x'] = 4
df.at[0, 'cost'] = 789
expected = DataFrame({'x': [4], 'cost': 789}, index=[0])
tm.assert_frame_equal(df, expected)
tm.assert_series_equal(df['cost'], expected['cost'])
```

## Next Steps


---

*Source: test_at.py:56 | Complexity: Advanced | Last updated: 2026-06-02*