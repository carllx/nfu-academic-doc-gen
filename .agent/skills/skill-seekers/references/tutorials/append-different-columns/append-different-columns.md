# How To: Append Different Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append different columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'bools': np.random.default_rng(2).standard_normal(10) > 0, 'ints': np.random.default_rng(2).integers(0, 10, 10), 'floats': np.random.default_rng(2).standard_normal(10), 'strings': ['foo', 'bar'] * 5})
```

**Verification:**
```python
assert isna(appended['strings'][0:4]).all()
```

### Step 2: Assign a = value

```python
a = df[:5].loc[:, ['bools', 'ints', 'floats']]
```

**Verification:**
```python
assert isna(appended['bools'][5:]).all()
```

### Step 3: Assign b = value

```python
b = df[5:].loc[:, ['strings', 'ints', 'floats']]
```

### Step 4: Assign appended = a._append(...)

```python
appended = a._append(b, sort=sort)
```

**Verification:**
```python
assert isna(appended['strings'][0:4]).all()
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
df = DataFrame({'bools': np.random.default_rng(2).standard_normal(10) > 0, 'ints': np.random.default_rng(2).integers(0, 10, 10), 'floats': np.random.default_rng(2).standard_normal(10), 'strings': ['foo', 'bar'] * 5})
a = df[:5].loc[:, ['bools', 'ints', 'floats']]
b = df[5:].loc[:, ['strings', 'ints', 'floats']]
appended = a._append(b, sort=sort)
assert isna(appended['strings'][0:4]).all()
assert isna(appended['bools'][5:]).all()
```

## Next Steps


---

*Source: test_append.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*