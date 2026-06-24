# How To: Rank Pct Equal Values On Group Transition

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank pct equal values on group transition

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: use_nan
```

## Step-by-Step Guide

### Step 1: Assign fill_value = value

```python
fill_value = np.nan if use_nan else 3
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[-1, 1], [-1, 2], [1, fill_value], [-1, fill_value]], columns=['group', 'val'])
```

### Step 3: Assign result = unknown.rank(...)

```python
result = df.groupby(['group'])['val'].rank(method='dense', pct=True)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0.5, 1, np.nan, np.nan], name='val')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1 / 3, 2 / 3, 1, 1], name='val')
```


## Complete Example

```python
# Setup
# Fixtures: use_nan

# Workflow
fill_value = np.nan if use_nan else 3
df = DataFrame([[-1, 1], [-1, 2], [1, fill_value], [-1, fill_value]], columns=['group', 'val'])
result = df.groupby(['group'])['val'].rank(method='dense', pct=True)
if use_nan:
    expected = Series([0.5, 1, np.nan, np.nan], name='val')
else:
    expected = Series([1 / 3, 2 / 3, 1, 1], name='val')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:588 | Complexity: Intermediate | Last updated: 2026-06-02*