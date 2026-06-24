# How To: Asof

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asof

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign N = 3

```python
N = 3
```

**Verification:**
```python
assert isinstance(result, tm.SubclassedSeries)
```

### Step 2: Assign rng = pd.date_range(...)

```python
rng = pd.date_range('1/1/1990', periods=N, freq='53s')
```

### Step 3: Assign s = tm.SubclassedSeries(...)

```python
s = tm.SubclassedSeries({'A': [np.nan, np.nan, np.nan]}, index=rng)
```

### Step 4: Assign result = s.asof(...)

```python
result = s.asof(rng[-2:])
```

**Verification:**
```python
assert isinstance(result, tm.SubclassedSeries)
```


## Complete Example

```python
# Workflow
N = 3
rng = pd.date_range('1/1/1990', periods=N, freq='53s')
s = tm.SubclassedSeries({'A': [np.nan, np.nan, np.nan]}, index=rng)
result = s.asof(rng[-2:])
assert isinstance(result, tm.SubclassedSeries)
```

## Next Steps


---

*Source: test_subclass.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*