# How To: Nunique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nunique

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(np.random.default_rng(2).standard_normal(500))
```

**Verification:**
```python
assert result == 11
```

### Step 2: Assign unknown = value

```python
series[20:500] = np.nan
```

### Step 3: Assign unknown = 5000

```python
series[10:20] = 5000
```

### Step 4: Assign result = series.nunique(...)

```python
result = series.nunique()
```

**Verification:**
```python
assert result == 11
```


## Complete Example

```python
# Workflow
series = Series(np.random.default_rng(2).standard_normal(500))
series[20:500] = np.nan
series[10:20] = 5000
result = series.nunique()
assert result == 11
```

## Next Steps


---

*Source: test_nunique.py:9 | Complexity: Intermediate | Last updated: 2026-06-02*