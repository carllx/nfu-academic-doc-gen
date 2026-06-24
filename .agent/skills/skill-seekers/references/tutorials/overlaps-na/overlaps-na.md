# How To: Overlaps Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: NA values are marked as False

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: constructor, start_shift
```

## Step-by-Step Guide

### Step 1: 'NA values are marked as False'

```python
'NA values are marked as False'
```

### Step 2: Assign unknown = start_shift

```python
start, shift = start_shift
```

### Step 3: Assign interval = Interval(...)

```python
interval = Interval(start, start + shift)
```

### Step 4: Assign tuples = value

```python
tuples = [(start, start + shift), np.nan, (start + 2 * shift, start + 3 * shift)]
```

### Step 5: Assign interval_container = constructor.from_tuples(...)

```python
interval_container = constructor.from_tuples(tuples)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([True, False, False])
```

### Step 7: Assign result = interval_container.overlaps(...)

```python
result = interval_container.overlaps(interval)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: constructor, start_shift

# Workflow
'NA values are marked as False'
start, shift = start_shift
interval = Interval(start, start + shift)
tuples = [(start, start + shift), np.nan, (start + 2 * shift, start + 3 * shift)]
interval_container = constructor.from_tuples(tuples)
expected = np.array([True, False, False])
result = interval_container.overlaps(interval)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_overlaps.py:68 | Complexity: Advanced | Last updated: 2026-06-02*