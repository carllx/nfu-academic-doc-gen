# How To: Indexing With Duplicate Datetimeindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing with duplicate datetimeindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: rand_series_with_duplicate_datetimeindex
```

## Step-by-Step Guide

### Step 1: Assign ts = rand_series_with_duplicate_datetimeindex

```python
ts = rand_series_with_duplicate_datetimeindex
```

**Verification:**
```python
assert ts[datetime(2000, 1, 6)] == 0
```

### Step 2: Assign uniques = ts.index.unique(...)

```python
uniques = ts.index.unique()
```

### Step 3: Assign key = datetime(...)

```python
key = datetime(2000, 1, 6)
```

### Step 4: Assign unknown = 0

```python
ts[datetime(2000, 1, 6)] = 0
```

**Verification:**
```python
assert ts[datetime(2000, 1, 6)] == 0
```

### Step 5: Assign result = value

```python
result = ts[date]
```

### Step 6: Assign mask = value

```python
mask = ts.index == date
```

### Step 7: Assign total = unknown.sum(...)

```python
total = (ts.index == date).sum()
```

### Step 8: Assign expected = value

```python
expected = ts[mask]
```

### Step 9: Assign cp = ts.copy(...)

```python
cp = ts.copy()
```

### Step 10: Assign unknown = 0

```python
cp[date] = 0
```

### Step 11: Assign expected = Series(...)

```python
expected = Series(np.where(mask, 0, ts), index=ts.index)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(cp, expected)
```

### Step 13: ts[key]

```python
ts[key]
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 15: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected.iloc[0])
```


## Complete Example

```python
# Setup
# Fixtures: rand_series_with_duplicate_datetimeindex

# Workflow
ts = rand_series_with_duplicate_datetimeindex
uniques = ts.index.unique()
for date in uniques:
    result = ts[date]
    mask = ts.index == date
    total = (ts.index == date).sum()
    expected = ts[mask]
    if total > 1:
        tm.assert_series_equal(result, expected)
    else:
        tm.assert_almost_equal(result, expected.iloc[0])
    cp = ts.copy()
    cp[date] = 0
    expected = Series(np.where(mask, 0, ts), index=ts.index)
    tm.assert_series_equal(cp, expected)
key = datetime(2000, 1, 6)
with pytest.raises(KeyError, match=re.escape(repr(key))):
    ts[key]
ts[datetime(2000, 1, 6)] = 0
assert ts[datetime(2000, 1, 6)] == 0
```

## Next Steps


---

*Source: test_datetime.py:283 | Complexity: Advanced | Last updated: 2026-06-02*