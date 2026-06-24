# How To: Getitem Generator

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem generator

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: string_series
```

## Step-by-Step Guide

### Step 1: Assign gen = value

```python
gen = (x > 0 for x in string_series)
```

### Step 2: Assign result = value

```python
result = string_series[gen]
```

### Step 3: Assign result2 = value

```python
result2 = string_series[iter(string_series > 0)]
```

### Step 4: Assign expected = value

```python
expected = string_series[string_series > 0]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected)
```


## Complete Example

```python
# Setup
# Fixtures: string_series

# Workflow
gen = (x > 0 for x in string_series)
result = string_series[gen]
result2 = string_series[iter(string_series > 0)]
expected = string_series[string_series > 0]
tm.assert_series_equal(result, expected)
tm.assert_series_equal(result2, expected)
```

## Next Steps


---

*Source: test_getitem.py:552 | Complexity: Intermediate | Last updated: 2026-06-02*