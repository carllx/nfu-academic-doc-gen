# How To: To Records With Na Record

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records with na record

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['a', 'b'], [np.nan, np.nan], ['e', 'f']], columns=[np.nan, 'right'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign unknown = unknown.to_records(...)

```python
df['record'] = df[[np.nan, 'right']].to_records()
```

### Step 3: Assign expected = '   NaN right         record\n0    a     b      [0, a, b]\n1  NaN   NaN  [1, nan, nan]\n2    e     f      [2, e, f]'

```python
expected = '   NaN right         record\n0    a     b      [0, a, b]\n1  NaN   NaN  [1, nan, nan]\n2    e     f      [2, e, f]'
```

### Step 4: Assign result = repr(...)

```python
result = repr(df)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame([['a', 'b'], [np.nan, np.nan], ['e', 'f']], columns=[np.nan, 'right'])
df['record'] = df[[np.nan, 'right']].to_records()
expected = '   NaN right         record\n0    a     b      [0, a, b]\n1  NaN   NaN  [1, nan, nan]\n2    e     f      [2, e, f]'
result = repr(df)
assert result == expected
```

## Next Steps


---

*Source: test_repr.py:412 | Complexity: Intermediate | Last updated: 2026-06-02*