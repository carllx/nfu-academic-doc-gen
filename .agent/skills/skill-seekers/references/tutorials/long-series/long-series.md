# How To: Long Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test long series

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `re`
- `shutil`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas.io.formats`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign n = 1000

```python
n = 1000
```

**Verification:**
```python
assert nmatches == 1
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).integers(-50, 50, n), index=[f's{x:04d}' for x in range(n)], dtype='int64')
```

### Step 3: Assign str_rep = str(...)

```python
str_rep = str(s)
```

### Step 4: Assign nmatches = len(...)

```python
nmatches = len(re.findall('dtype', str_rep))
```

**Verification:**
```python
assert nmatches == 1
```


## Complete Example

```python
# Workflow
n = 1000
s = Series(np.random.default_rng(2).integers(-50, 50, n), index=[f's{x:04d}' for x in range(n)], dtype='int64')
str_rep = str(s)
nmatches = len(re.findall('dtype', str_rep))
assert nmatches == 1
```

## Next Steps


---

*Source: test_format.py:1121 | Complexity: Intermediate | Last updated: 2026-06-02*