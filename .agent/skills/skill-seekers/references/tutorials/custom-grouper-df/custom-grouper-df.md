# How To: Custom Grouper Df

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom grouper df

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._typing`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: index, unit
```

## Step-by-Step Guide

### Step 1: Assign b = Grouper(...)

```python
b = Grouper(freq=Minute(5), closed='right', label='right')
```

**Verification:**
```python
assert len(r.columns) == 10
```

### Step 2: Assign dti = index.as_unit(...)

```python
dti = index.as_unit(unit)
```

**Verification:**
```python
assert len(r.index) == 2593
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((len(dti), 10)), index=dti, dtype='float64')
```

### Step 4: Assign r = df.groupby.agg(...)

```python
r = df.groupby(b).agg('sum')
```

**Verification:**
```python
assert len(r.columns) == 10
```


## Complete Example

```python
# Setup
# Fixtures: index, unit

# Workflow
b = Grouper(freq=Minute(5), closed='right', label='right')
dti = index.as_unit(unit)
df = DataFrame(np.random.default_rng(2).random((len(dti), 10)), index=dti, dtype='float64')
r = df.groupby(b).agg('sum')
assert len(r.columns) == 10
assert len(r.index) == 2593
```

## Next Steps


---

*Source: test_datetime_index.py:108 | Complexity: Intermediate | Last updated: 2026-06-02*