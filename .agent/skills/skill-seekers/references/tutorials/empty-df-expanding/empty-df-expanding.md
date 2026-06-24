# How To: Empty Df Expanding

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test empty df expanding

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: expander
```

## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame()
```

### Step 2: Assign result = DataFrame.expanding.sum(...)

```python
result = DataFrame().expanding(expander).sum()
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=DatetimeIndex([]))
```

### Step 5: Assign result = DataFrame.expanding.sum(...)

```python
result = DataFrame(index=DatetimeIndex([])).expanding(expander).sum()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: expander

# Workflow
expected = DataFrame()
result = DataFrame().expanding(expander).sum()
tm.assert_frame_equal(result, expected)
expected = DataFrame(index=DatetimeIndex([]))
result = DataFrame(index=DatetimeIndex([])).expanding(expander).sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_expanding.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*