# How To: To Timestamp Quarterly Bug

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to timestamp quarterly bug

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign years = np.arange.repeat(...)

```python
years = np.arange(1960, 2000).repeat(4)
```

**Verification:**
```python
assert stamps.freq == expected.freq
```

### Step 2: Assign quarters = np.tile(...)

```python
quarters = np.tile(list(range(1, 5)), 40)
```

### Step 3: Assign pindex = PeriodIndex.from_fields(...)

```python
pindex = PeriodIndex.from_fields(year=years, quarter=quarters)
```

### Step 4: Assign stamps = pindex.to_timestamp(...)

```python
stamps = pindex.to_timestamp('D', 'end')
```

### Step 5: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([x.to_timestamp('D', 'end') for x in pindex])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(stamps, expected)
```

**Verification:**
```python
assert stamps.freq == expected.freq
```


## Complete Example

```python
# Workflow
years = np.arange(1960, 2000).repeat(4)
quarters = np.tile(list(range(1, 5)), 40)
pindex = PeriodIndex.from_fields(year=years, quarter=quarters)
stamps = pindex.to_timestamp('D', 'end')
expected = DatetimeIndex([x.to_timestamp('D', 'end') for x in pindex])
tm.assert_index_equal(stamps, expected)
assert stamps.freq == expected.freq
```

## Next Steps


---

*Source: test_to_timestamp.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*