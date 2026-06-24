# How To: Convert Nested

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test convert nested

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas._config.config`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`
- `pandas.plotting`
- `pandas.tseries.offsets`
- `pandas.plotting._matplotlib`

**Setup Required:**
```python
# Fixtures: dtc
```

## Step-by-Step Guide

### Step 1: Assign inner = value

```python
inner = [Timestamp('2017-01-01'), Timestamp('2017-01-02')]
```

**Verification:**
```python
assert (np.array(result) == expected).all()
```

### Step 2: Assign data = value

```python
data = [inner, inner]
```

### Step 3: Assign result = dtc.convert(...)

```python
result = dtc.convert(data, None, None)
```

### Step 4: Assign expected = value

```python
expected = [dtc.convert(x, None, None) for x in data]
```

**Verification:**
```python
assert (np.array(result) == expected).all()
```


## Complete Example

```python
# Setup
# Fixtures: dtc

# Workflow
inner = [Timestamp('2017-01-01'), Timestamp('2017-01-02')]
data = [inner, inner]
result = dtc.convert(data, None, None)
expected = [dtc.convert(x, None, None) for x in data]
assert (np.array(result) == expected).all()
```

## Next Steps


---

*Source: test_converter.py:279 | Complexity: Intermediate | Last updated: 2026-06-02*