# How To: Filter Mixed Df

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter mixed df

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 12, 12, 1], 'B': 'a b c d'.split()})
```

### Step 2: Assign grouper = unknown.apply(...)

```python
grouper = df['A'].apply(lambda x: x % 2)
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(grouper)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [12, 12], 'B': ['b', 'c']}, index=[1, 2])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.filter(lambda x: x['A'].sum() > 10), expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 12, 12, 1], 'B': 'a b c d'.split()})
grouper = df['A'].apply(lambda x: x % 2)
grouped = df.groupby(grouper)
expected = DataFrame({'A': [12, 12], 'B': ['b', 'c']}, index=[1, 2])
tm.assert_frame_equal(grouped.filter(lambda x: x['A'].sum() > 10), expected)
```

## Next Steps


---

*Source: test_filters.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*