# How To: Nan To Nat Conversions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nan to nat conversions

## Prerequisites

**Required Modules:**
- `collections`
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `fractions`
- `io`
- `itertools`
- `numbers`
- `re`
- `sys`
- `typing`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.core.dtypes`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.asarray(range(10), dtype='float64'), 'B': Timestamp('20010101')})
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 2: Assign unknown = value

```python
df.iloc[3:6, :] = np.nan
```

**Verification:**
```python
assert s[8] is pd.NaT
```

### Step 3: Assign result = value

```python
result = df.loc[4, 'B']
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 4: Assign s = unknown.copy(...)

```python
s = df['B'].copy()
```

### Step 5: Assign unknown = value

```python
s[8:9] = np.nan
```

**Verification:**
```python
assert s[8] is pd.NaT
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': np.asarray(range(10), dtype='float64'), 'B': Timestamp('20010101')})
df.iloc[3:6, :] = np.nan
result = df.loc[4, 'B']
assert result is pd.NaT
s = df['B'].copy()
s[8:9] = np.nan
assert s[8] is pd.NaT
```

## Next Steps


---

*Source: test_inference.py:1997 | Complexity: Intermediate | Last updated: 2026-06-02*