# How To: Filter Out No Groups

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter out no groups

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 3, 20, 5, 22, 24, 7])
```

### Step 2: Assign grouper = s.apply(...)

```python
grouper = s.apply(lambda x: x % 2)
```

### Step 3: Assign grouped = s.groupby(...)

```python
grouped = s.groupby(grouper)
```

### Step 4: Assign filtered = grouped.filter(...)

```python
filtered = grouped.filter(lambda x: x.mean() > 0)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(filtered, s)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 12, 12, 1], 'B': 'a b c d'.split()})
```

### Step 7: Assign grouper = unknown.apply(...)

```python
grouper = df['A'].apply(lambda x: x % 2)
```

### Step 8: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(grouper)
```

### Step 9: Assign filtered = grouped.filter(...)

```python
filtered = grouped.filter(lambda x: x['A'].mean() > 0)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(filtered, df)
```


## Complete Example

```python
# Workflow
s = Series([1, 3, 20, 5, 22, 24, 7])
grouper = s.apply(lambda x: x % 2)
grouped = s.groupby(grouper)
filtered = grouped.filter(lambda x: x.mean() > 0)
tm.assert_series_equal(filtered, s)
df = DataFrame({'A': [1, 12, 12, 1], 'B': 'a b c d'.split()})
grouper = df['A'].apply(lambda x: x % 2)
grouped = df.groupby(grouper)
filtered = grouped.filter(lambda x: x['A'].mean() > 0)
tm.assert_frame_equal(filtered, df)
```

## Next Steps


---

*Source: test_filters.py:82 | Complexity: Advanced | Last updated: 2026-06-02*