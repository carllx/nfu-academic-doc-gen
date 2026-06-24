# How To: Intersection Cases

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection cases

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign base = period_range(...)

```python
base = period_range('6/1/2000', '6/30/2000', freq='D', name='idx')
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 2: Assign rng2 = period_range(...)

```python
rng2 = period_range('5/15/2000', '6/20/2000', freq='D', name='idx')
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 3: Assign expected2 = period_range(...)

```python
expected2 = period_range('6/1/2000', '6/20/2000', freq='D', name='idx')
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 4: Assign rng3 = period_range(...)

```python
rng3 = period_range('5/15/2000', '6/20/2000', freq='D', name='other')
```

**Verification:**
```python
assert result.freq == 'D'
```

### Step 5: Assign expected3 = period_range(...)

```python
expected3 = period_range('6/1/2000', '6/20/2000', freq='D', name=None)
```

**Verification:**
```python
assert len(result) == 0
```

### Step 6: Assign rng4 = period_range(...)

```python
rng4 = period_range('7/1/2000', '7/31/2000', freq='D', name='idx')
```

**Verification:**
```python
assert len(result) == 0
```

### Step 7: Assign expected4 = PeriodIndex(...)

```python
expected4 = PeriodIndex([], name='idx', freq='D')
```

### Step 8: Assign base = PeriodIndex(...)

```python
base = PeriodIndex(['2011-01-05', '2011-01-04', '2011-01-02', '2011-01-03'], freq='D', name='idx')
```

### Step 9: Assign rng2 = PeriodIndex(...)

```python
rng2 = PeriodIndex(['2011-01-04', '2011-01-02', '2011-02-02', '2011-02-03'], freq='D', name='idx')
```

### Step 10: Assign expected2 = PeriodIndex(...)

```python
expected2 = PeriodIndex(['2011-01-04', '2011-01-02'], freq='D', name='idx')
```

### Step 11: Assign rng3 = PeriodIndex(...)

```python
rng3 = PeriodIndex(['2011-01-04', '2011-01-02', '2011-02-02', '2011-02-03'], freq='D', name='other')
```

### Step 12: Assign expected3 = PeriodIndex(...)

```python
expected3 = PeriodIndex(['2011-01-04', '2011-01-02'], freq='D', name=None)
```

### Step 13: Assign rng4 = period_range(...)

```python
rng4 = period_range('7/1/2000', '7/31/2000', freq='D', name='idx')
```

### Step 14: Assign expected4 = PeriodIndex(...)

```python
expected4 = PeriodIndex([], freq='D', name='idx')
```

### Step 15: Assign rng = date_range(...)

```python
rng = date_range('6/1/2000', '6/15/2000', freq='min')
```

### Step 16: Assign result = unknown.intersection(...)

```python
result = rng[0:0].intersection(rng)
```

**Verification:**
```python
assert len(result) == 0
```

### Step 17: Assign result = rng.intersection(...)

```python
result = rng.intersection(rng[0:0])
```

**Verification:**
```python
assert len(result) == 0
```

### Step 18: Assign result = base.intersection(...)

```python
result = base.intersection(rng, sort=sort)
```

### Step 19: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 20: Assign result = base.intersection(...)

```python
result = base.intersection(rng, sort=sort)
```

### Step 21: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 22: Assign expected = expected.sort_values(...)

```python
expected = expected.sort_values()
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
base = period_range('6/1/2000', '6/30/2000', freq='D', name='idx')
rng2 = period_range('5/15/2000', '6/20/2000', freq='D', name='idx')
expected2 = period_range('6/1/2000', '6/20/2000', freq='D', name='idx')
rng3 = period_range('5/15/2000', '6/20/2000', freq='D', name='other')
expected3 = period_range('6/1/2000', '6/20/2000', freq='D', name=None)
rng4 = period_range('7/1/2000', '7/31/2000', freq='D', name='idx')
expected4 = PeriodIndex([], name='idx', freq='D')
for rng, expected in [(rng2, expected2), (rng3, expected3), (rng4, expected4)]:
    result = base.intersection(rng, sort=sort)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
base = PeriodIndex(['2011-01-05', '2011-01-04', '2011-01-02', '2011-01-03'], freq='D', name='idx')
rng2 = PeriodIndex(['2011-01-04', '2011-01-02', '2011-02-02', '2011-02-03'], freq='D', name='idx')
expected2 = PeriodIndex(['2011-01-04', '2011-01-02'], freq='D', name='idx')
rng3 = PeriodIndex(['2011-01-04', '2011-01-02', '2011-02-02', '2011-02-03'], freq='D', name='other')
expected3 = PeriodIndex(['2011-01-04', '2011-01-02'], freq='D', name=None)
rng4 = period_range('7/1/2000', '7/31/2000', freq='D', name='idx')
expected4 = PeriodIndex([], freq='D', name='idx')
for rng, expected in [(rng2, expected2), (rng3, expected3), (rng4, expected4)]:
    result = base.intersection(rng, sort=sort)
    if sort is None:
        expected = expected.sort_values()
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == 'D'
rng = date_range('6/1/2000', '6/15/2000', freq='min')
result = rng[0:0].intersection(rng)
assert len(result) == 0
result = rng.intersection(rng[0:0])
assert len(result) == 0
```

## Next Steps


---

*Source: test_setops.py:184 | Complexity: Advanced | Last updated: 2026-06-02*