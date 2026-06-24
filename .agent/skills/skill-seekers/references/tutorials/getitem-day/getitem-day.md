# How To: Getitem Day

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem day

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx_range
```

## Step-by-Step Guide

### Step 1: Assign idx = idx_range(...)

```python
idx = idx_range(start='2013/01/01', freq='D', periods=400)
```

### Step 2: Assign values = value

```python
values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9h', '2013/02/01 09:00']
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).random(len(idx)), index=idx)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser['2013/01'], ser[0:31])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser['2013/02'], ser[31:59])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser['2014'], ser[365:])
```

### Step 7: Assign invalid = value

```python
invalid = ['2013/02/01 9h', '2013/02/01 09:00']
```

### Step 8: idx[val]

```python
idx[val]
```

### Step 9: ser[val]

```python
ser[val]
```


## Complete Example

```python
# Setup
# Fixtures: idx_range

# Workflow
idx = idx_range(start='2013/01/01', freq='D', periods=400)
values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9h', '2013/02/01 09:00']
for val in values:
    with pytest.raises(IndexError, match='only integers, slices'):
        idx[val]
ser = Series(np.random.default_rng(2).random(len(idx)), index=idx)
tm.assert_series_equal(ser['2013/01'], ser[0:31])
tm.assert_series_equal(ser['2013/02'], ser[31:59])
tm.assert_series_equal(ser['2014'], ser[365:])
invalid = ['2013/02/01 9h', '2013/02/01 09:00']
for val in invalid:
    with pytest.raises(KeyError, match=val):
        ser[val]
```

## Next Steps


---

*Source: test_indexing.py:209 | Complexity: Advanced | Last updated: 2026-06-02*