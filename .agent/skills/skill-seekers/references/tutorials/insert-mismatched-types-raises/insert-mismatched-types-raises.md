# How To: Insert Mismatched Types Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test insert mismatched types raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture, item
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

**Verification:**
```python
assert item.item() == 0
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range('2019-11-04', periods=9, freq='-1D', name=9, tz=tz)
```

### Step 3: Assign result = dti.insert(...)

```python
result = dti.insert(1, item)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert item.item() == 0
```

### Step 5: Assign expected = Index(...)

```python
expected = Index([dti[0], 0] + list(dti[1:]), dtype=object, name=9)
```

### Step 6: Assign expected = Index(...)

```python
expected = Index([dti[0], item] + list(dti[1:]), dtype=object, name=9)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture, item

# Workflow
tz = tz_aware_fixture
dti = date_range('2019-11-04', periods=9, freq='-1D', name=9, tz=tz)
result = dti.insert(1, item)
if isinstance(item, np.ndarray):
    assert item.item() == 0
    expected = Index([dti[0], 0] + list(dti[1:]), dtype=object, name=9)
else:
    expected = Index([dti[0], item] + list(dti[1:]), dtype=object, name=9)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_insert.py:229 | Complexity: Intermediate | Last updated: 2026-06-02*