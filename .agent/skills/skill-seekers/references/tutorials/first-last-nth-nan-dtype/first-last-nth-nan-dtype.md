# How To: First Last Nth Nan Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test first last nth nan dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'data': ['A'], 'nans': Series([None], dtype=object)})
```

### Step 2: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('data')
```

### Step 3: Assign expected = value

```python
expected = df.set_index('data').nans
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.nans.first(), expected)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.nans.last(), expected)
```

### Step 6: Assign expected = value

```python
expected = df.nans
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.nans.nth(-1), expected)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.nans.nth(0), expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'data': ['A'], 'nans': Series([None], dtype=object)})
grouped = df.groupby('data')
expected = df.set_index('data').nans
tm.assert_series_equal(grouped.nans.first(), expected)
tm.assert_series_equal(grouped.nans.last(), expected)
expected = df.nans
tm.assert_series_equal(grouped.nans.nth(-1), expected)
tm.assert_series_equal(grouped.nans.nth(0), expected)
```

## Next Steps


---

*Source: test_nth.py:166 | Complexity: Advanced | Last updated: 2026-06-02*