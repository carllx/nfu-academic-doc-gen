# How To: Stat Method

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test stat method

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: pandasmethname, kwargs
```

## Step-by-Step Guide

### Step 1: Assign s = pd.Series(...)

```python
s = pd.Series(data=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, np.nan, np.nan], dtype='Float64')
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign pandasmeth = getattr(...)

```python
pandasmeth = getattr(s, pandasmethname)
```

### Step 3: Assign result = pandasmeth(...)

```python
result = pandasmeth(**kwargs)
```

### Step 4: Assign s2 = pd.Series(...)

```python
s2 = pd.Series(data=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], dtype='float64')
```

### Step 5: Assign pandasmeth = getattr(...)

```python
pandasmeth = getattr(s2, pandasmethname)
```

### Step 6: Assign expected = pandasmeth(...)

```python
expected = pandasmeth(**kwargs)
```

**Verification:**
```python
assert expected == result
```


## Complete Example

```python
# Setup
# Fixtures: pandasmethname, kwargs

# Workflow
s = pd.Series(data=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, np.nan, np.nan], dtype='Float64')
pandasmeth = getattr(s, pandasmethname)
result = pandasmeth(**kwargs)
s2 = pd.Series(data=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6], dtype='float64')
pandasmeth = getattr(s2, pandasmethname)
expected = pandasmeth(**kwargs)
assert expected == result
```

## Next Steps


---

*Source: test_function.py:90 | Complexity: Intermediate | Last updated: 2026-06-02*