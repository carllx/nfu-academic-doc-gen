# How To: Tuple Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tuple index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign col = np.arange(...)

```python
col = np.arange(10)
```

### Step 2: Assign idx = value

```python
idx = [(0.0, 1.0), (2.0, 3.0), (4.0, 5.0)]
```

### Step 3: Assign data = np.random.default_rng.standard_normal.reshape(...)

```python
data = np.random.default_rng(2).standard_normal(30).reshape((3, 10))
```

### Step 4: Assign DF = DataFrame(...)

```python
DF = DataFrame(data, index=idx, columns=col)
```

### Step 5: Call _check_roundtrip()

```python
_check_roundtrip(DF, tm.assert_frame_equal, path=setup_path)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
col = np.arange(10)
idx = [(0.0, 1.0), (2.0, 3.0), (4.0, 5.0)]
data = np.random.default_rng(2).standard_normal(30).reshape((3, 10))
DF = DataFrame(data, index=idx, columns=col)
with tm.assert_produces_warning(pd.errors.PerformanceWarning):
    _check_roundtrip(DF, tm.assert_frame_equal, path=setup_path)
```

## Next Steps


---

*Source: test_round_trip.py:288 | Complexity: Intermediate | Last updated: 2026-06-02*