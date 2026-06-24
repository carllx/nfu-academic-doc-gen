# How To: Filter Out All Groups

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter out all groups

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

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.filter(lambda x: x.mean() > 1000), s[[]])
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 12, 12, 1], 'B': 'a b c d'.split()})
```

### Step 6: Assign grouper = unknown.apply(...)

```python
grouper = df['A'].apply(lambda x: x % 2)
```

### Step 7: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(grouper)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.filter(lambda x: x['A'].sum() > 1000), df.loc[[]])
```


## Complete Example

```python
# Workflow
s = Series([1, 3, 20, 5, 22, 24, 7])
grouper = s.apply(lambda x: x % 2)
grouped = s.groupby(grouper)
tm.assert_series_equal(grouped.filter(lambda x: x.mean() > 1000), s[[]])
df = DataFrame({'A': [1, 12, 12, 1], 'B': 'a b c d'.split()})
grouper = df['A'].apply(lambda x: x % 2)
grouped = df.groupby(grouper)
tm.assert_frame_equal(grouped.filter(lambda x: x['A'].sum() > 1000), df.loc[[]])
```

## Next Steps


---

*Source: test_filters.py:71 | Complexity: Advanced | Last updated: 2026-06-02*