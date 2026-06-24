# How To: Apply

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: offset_types, expecteds
```

## Step-by-Step Guide

### Step 1: Assign sdt = datetime(...)

```python
sdt = datetime(2011, 1, 1, 9, 0)
```

### Step 2: Assign ndt = np.datetime64(...)

```python
ndt = np.datetime64('2011-01-01 09:00')
```

### Step 3: Assign expected = value

```python
expected = expecteds[offset_types.__name__]
```

### Step 4: Assign expected_norm = Timestamp(...)

```python
expected_norm = Timestamp(expected.date())
```

### Step 5: Call self._check_offsetfunc_works()

```python
self._check_offsetfunc_works(offset_types, '_apply', dt, expected)
```

### Step 6: Call self._check_offsetfunc_works()

```python
self._check_offsetfunc_works(offset_types, '_apply', dt, expected_norm, normalize=True)
```


## Complete Example

```python
# Setup
# Fixtures: offset_types, expecteds

# Workflow
sdt = datetime(2011, 1, 1, 9, 0)
ndt = np.datetime64('2011-01-01 09:00')
expected = expecteds[offset_types.__name__]
expected_norm = Timestamp(expected.date())
for dt in [sdt, ndt]:
    self._check_offsetfunc_works(offset_types, '_apply', dt, expected)
    self._check_offsetfunc_works(offset_types, '_apply', dt, expected_norm, normalize=True)
```

## Next Steps


---

*Source: test_offsets.py:305 | Complexity: Intermediate | Last updated: 2026-06-02*