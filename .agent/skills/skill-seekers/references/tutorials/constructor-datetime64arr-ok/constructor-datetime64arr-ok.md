# How To: Constructor Datetime64Arr Ok

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor datetime64arr ok

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: box
```

## Step-by-Step Guide

### Step 1: Assign data = date_range(...)

```python
data = date_range('2017', periods=4, freq='ME')
```

### Step 2: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(data, freq='D')
```

### Step 3: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(['2017-01-31', '2017-02-28', '2017-03-31', '2017-04-30'], freq='D')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign data = value

```python
data = data._values
```

### Step 6: Assign data = Series(...)

```python
data = Series(data)
```


## Complete Example

```python
# Setup
# Fixtures: box

# Workflow
data = date_range('2017', periods=4, freq='ME')
if box is None:
    data = data._values
elif box == 'series':
    data = Series(data)
result = PeriodIndex(data, freq='D')
expected = PeriodIndex(['2017-01-31', '2017-02-28', '2017-03-31', '2017-04-30'], freq='D')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:299 | Complexity: Intermediate | Last updated: 2026-06-02*