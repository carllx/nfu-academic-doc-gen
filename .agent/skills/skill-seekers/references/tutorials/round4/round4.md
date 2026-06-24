# How To: Round4

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round4

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(['2016-10-17 12:00:00.001501031'], dtype='M8[ns]')
```

### Step 2: Assign result = index.round(...)

```python
result = index.round('10ns')
```

### Step 3: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2016-10-17 12:00:00.001501030'], dtype='M8[ns]')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign ts = '2016-10-17 12:00:00.001501031'

```python
ts = '2016-10-17 12:00:00.001501031'
```

### Step 6: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([ts], dtype='M8[ns]')
```

### Step 7: Call dti.round()

```python
dti.round('1010ns')
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
index = DatetimeIndex(['2016-10-17 12:00:00.001501031'], dtype='M8[ns]')
result = index.round('10ns')
expected = DatetimeIndex(['2016-10-17 12:00:00.001501030'], dtype='M8[ns]')
tm.assert_index_equal(result, expected)
ts = '2016-10-17 12:00:00.001501031'
dti = DatetimeIndex([ts], dtype='M8[ns]')
with tm.assert_produces_warning(False):
    dti.round('1010ns')
```

## Next Steps


---

*Source: test_round.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*