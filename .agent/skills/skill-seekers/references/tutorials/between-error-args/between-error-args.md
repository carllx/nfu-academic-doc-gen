# How To: Between Error Args

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test between error args

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: inclusive
```

## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(date_range('1/1/2000', periods=10))
```

### Step 2: Assign unknown = value

```python
left, right = series[[2, 7]]
```

### Step 3: Assign value_error_msg = "Inclusive has to be either string of 'both','left', 'right', or 'neither'."

```python
value_error_msg = "Inclusive has to be either string of 'both','left', 'right', or 'neither'."
```

### Step 4: Assign series = Series(...)

```python
series = Series(date_range('1/1/2000', periods=10))
```

### Step 5: Call series.between()

```python
series.between(left, right, inclusive=inclusive)
```


## Complete Example

```python
# Setup
# Fixtures: inclusive

# Workflow
series = Series(date_range('1/1/2000', periods=10))
left, right = series[[2, 7]]
value_error_msg = "Inclusive has to be either string of 'both','left', 'right', or 'neither'."
with pytest.raises(ValueError, match=value_error_msg):
    series = Series(date_range('1/1/2000', periods=10))
    series.between(left, right, inclusive=inclusive)
```

## Next Steps


---

*Source: test_between.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*