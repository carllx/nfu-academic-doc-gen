# How To: Where Mismatched Nat

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where mismatched nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.frequencies`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

**Verification:**
```python
assert expected[1] is tdnat
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range('2013-01-01', periods=3, tz=tz)
```

### Step 3: Assign cond = np.array(...)

```python
cond = np.array([True, False, True])
```

### Step 4: Assign tdnat = np.timedelta64(...)

```python
tdnat = np.timedelta64('NaT', 'ns')
```

### Step 5: Assign expected = Index(...)

```python
expected = Index([dti[0], tdnat, dti[2]], dtype=object)
```

**Verification:**
```python
assert expected[1] is tdnat
```

### Step 6: Assign result = dti.where(...)

```python
result = dti.where(cond, tdnat)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
tz = tz_aware_fixture
dti = date_range('2013-01-01', periods=3, tz=tz)
cond = np.array([True, False, True])
tdnat = np.timedelta64('NaT', 'ns')
expected = Index([dti[0], tdnat, dti[2]], dtype=object)
assert expected[1] is tdnat
result = dti.where(cond, tdnat)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*