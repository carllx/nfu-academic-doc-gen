# How To: Agg Relabel Partial Functions

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test agg relabel partial functions

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [1, 2, 1, 2], 'B': [1, 2, 3, 4], 'C': [3, 4, 5, 6]})
```

### Step 2: Assign msg = 'using Series.[mean|min]'

```python
msg = 'using Series.[mean|min]'
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': [1.5, 1.5, 1.0]}, index=pd.Index(['foo', 'bar', 'cat']))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign msg = 'using Series.[mean|min|max|sum]'

```python
msg = 'using Series.[mean|min|max|sum]'
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': [1.0, 1.0, np.nan, np.nan, np.nan, np.nan], 'B': [np.nan, np.nan, 4.0, np.nan, 10.0, 1.0], 'C': [np.nan, np.nan, np.nan, 3.0, np.nan, np.nan]}, index=pd.Index(['foo', 'bar', 'cat', 'dat', 'f', 'kk']))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df.agg(...)

```python
result = df.agg(foo=('A', np.mean), bar=('A', 'mean'), cat=('A', min))
```

### Step 9: Assign result = df.agg(...)

```python
result = df.agg(foo=('A', min), bar=('A', np.min), cat=('B', max), dat=('C', 'min'), f=('B', np.sum), kk=('B', lambda x: min(x)))
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': [1, 2, 1, 2], 'B': [1, 2, 3, 4], 'C': [3, 4, 5, 6]})
msg = 'using Series.[mean|min]'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.agg(foo=('A', np.mean), bar=('A', 'mean'), cat=('A', min))
expected = pd.DataFrame({'A': [1.5, 1.5, 1.0]}, index=pd.Index(['foo', 'bar', 'cat']))
tm.assert_frame_equal(result, expected)
msg = 'using Series.[mean|min|max|sum]'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.agg(foo=('A', min), bar=('A', np.min), cat=('B', max), dat=('C', 'min'), f=('B', np.sum), kk=('B', lambda x: min(x)))
expected = pd.DataFrame({'A': [1.0, 1.0, np.nan, np.nan, np.nan, np.nan], 'B': [np.nan, np.nan, 4.0, np.nan, 10.0, 1.0], 'C': [np.nan, np.nan, np.nan, 3.0, np.nan, np.nan]}, index=pd.Index(['foo', 'bar', 'cat', 'dat', 'f', 'kk']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply_relabeling.py:49 | Complexity: Advanced | Last updated: 2026-06-02*