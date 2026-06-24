# How To: Diff Timedelta64 With Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff timedelta64 with nat

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.reshape.astype(...)

```python
arr = np.arange(6).reshape(3, 2).astype('timedelta64[ns]')
```

**Verification:**
```python
assert expected[0].isna().all()
```

### Step 2: Assign unknown = np.timedelta64(...)

```python
arr[:, 0] = np.timedelta64('NaT', 'ns')
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(arr)
```

### Step 4: Assign result = df.diff(...)

```python
result = df.diff(1, axis=0)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: df[0], 1: [pd.NaT, pd.Timedelta(2), pd.Timedelta(2)]})
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign result = df.diff(...)

```python
result = df.diff(0)
```

### Step 8: Assign expected = value

```python
expected = df - df
```

**Verification:**
```python
assert expected[0].isna().all()
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 10: Assign result = df.diff(...)

```python
result = df.diff(-1, axis=1)
```

### Step 11: Assign expected = value

```python
expected = df * np.nan
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.arange(6).reshape(3, 2).astype('timedelta64[ns]')
arr[:, 0] = np.timedelta64('NaT', 'ns')
df = DataFrame(arr)
result = df.diff(1, axis=0)
expected = DataFrame({0: df[0], 1: [pd.NaT, pd.Timedelta(2), pd.Timedelta(2)]})
tm.assert_equal(result, expected)
result = df.diff(0)
expected = df - df
assert expected[0].isna().all()
tm.assert_equal(result, expected)
result = df.diff(-1, axis=1)
expected = df * np.nan
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:52 | Complexity: Advanced | Last updated: 2026-06-02*