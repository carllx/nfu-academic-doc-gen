# How To: Join Preserves Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join preserves freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=10, tz=tz)
```

**Verification:**
```python
assert result.freq == dti.freq
```

### Step 2: Assign result = unknown.join(...)

```python
result = dti[:5].join(dti[5:], how='outer')
```

**Verification:**
```python
assert result.freq is None
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, dti)
```

### Step 4: Assign result = unknown.join(...)

```python
result = dti[:5].join(dti[6:], how='outer')
```

**Verification:**
```python
assert result.freq is None
```

### Step 5: Assign expected = dti.delete(...)

```python
expected = dti.delete(5)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dti = date_range('2016-01-01', periods=10, tz=tz)
result = dti[:5].join(dti[5:], how='outer')
assert result.freq == dti.freq
tm.assert_index_equal(result, dti)
result = dti[:5].join(dti[6:], how='outer')
assert result.freq is None
expected = dti.delete(5)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*