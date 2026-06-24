# How To: Column Select Via Attr

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test column select via attr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign result = df.groupby.C.sum(...)

```python
result = df.groupby('A').C.sum()
```

### Step 2: Assign expected = unknown.sum(...)

```python
expected = df.groupby('A')['C'].sum()
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 4: Assign unknown = 1.5

```python
df['mean'] = 1.5
```

### Step 5: Assign result = df.groupby.mean(...)

```python
result = df.groupby('A').mean(numeric_only=True)
```

### Step 6: Assign expected = unknown.agg(...)

```python
expected = df.groupby('A')[['C', 'D', 'mean']].agg('mean')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
result = df.groupby('A').C.sum()
expected = df.groupby('A')['C'].sum()
tm.assert_series_equal(result, expected)
df['mean'] = 1.5
result = df.groupby('A').mean(numeric_only=True)
expected = df.groupby('A')[['C', 'D', 'mean']].agg('mean')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_grouping.py:60 | Complexity: Intermediate | Last updated: 2026-06-02*