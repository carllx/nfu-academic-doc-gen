# How To: Astype Duplicate Col Series Arg

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype duplicate col series arg

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign vals = np.random.default_rng.standard_normal(...)

```python
vals = np.random.default_rng(2).standard_normal((3, 4))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(vals, columns=['A', 'B', 'C', 'A'])
```

### Step 3: Assign dtypes = value

```python
dtypes = df.dtypes
```

### Step 4: Assign unknown = str

```python
dtypes.iloc[0] = str
```

### Step 5: Assign unknown = 'Float64'

```python
dtypes.iloc[2] = 'Float64'
```

### Step 6: Assign result = df.astype(...)

```python
result = df.astype(dtypes)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: Series(vals[:, 0].astype(str), dtype='str'), 1: vals[:, 1], 2: pd.array(vals[:, 2], dtype='Float64'), 3: vals[:, 3]})
```

### Step 8: Assign expected.columns = value

```python
expected.columns = df.columns
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
vals = np.random.default_rng(2).standard_normal((3, 4))
df = DataFrame(vals, columns=['A', 'B', 'C', 'A'])
dtypes = df.dtypes
dtypes.iloc[0] = str
dtypes.iloc[2] = 'Float64'
result = df.astype(dtypes)
expected = DataFrame({0: Series(vals[:, 0].astype(str), dtype='str'), 1: vals[:, 1], 2: pd.array(vals[:, 2], dtype='Float64'), 3: vals[:, 3]})
expected.columns = df.columns
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:277 | Complexity: Advanced | Last updated: 2026-06-02*