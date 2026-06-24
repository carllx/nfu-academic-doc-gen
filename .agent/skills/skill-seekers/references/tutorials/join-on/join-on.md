# How To: Join On

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join on

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: target_source, infer_string
```

## Step-by-Step Guide

### Step 1: Assign unknown = target_source

```python
target, source = target_source
```

**Verification:**
```python
assert np.isnan(joined['two']['c'])
```

### Step 2: Assign merged = target.join(...)

```python
merged = target.join(source, on='C')
```

**Verification:**
```python
assert np.isnan(joined['three']['c'])
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(merged['MergedA'], target['A'], check_names=False)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(merged['MergedD'], target['D'], check_names=False)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'key': ['a', 'a', 'b', 'b', 'c']})
```

### Step 6: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'value': [0, 1, 2]}, index=['a', 'b', 'c'])
```

### Step 7: Assign joined = df.join(...)

```python
joined = df.join(df2, on='key')
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'key': ['a', 'a', 'b', 'b', 'c'], 'value': [0, 0, 1, 1, 2]})
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(joined, expected)
```

### Step 10: Assign df_a = DataFrame(...)

```python
df_a = DataFrame([[1], [2], [3]], index=['a', 'b', 'c'], columns=['one'])
```

### Step 11: Assign df_b = DataFrame(...)

```python
df_b = DataFrame([['foo'], ['bar']], index=[1, 2], columns=['two'])
```

### Step 12: Assign df_c = DataFrame(...)

```python
df_c = DataFrame([[1], [2]], index=[1, 2], columns=['three'])
```

### Step 13: Assign joined = df_a.join(...)

```python
joined = df_a.join(df_b, on='one')
```

### Step 14: Assign joined = joined.join(...)

```python
joined = joined.join(df_c, on='one')
```

**Verification:**
```python
assert np.isnan(joined['two']['c'])
```

### Step 15: Assign source_copy = source.copy(...)

```python
source_copy = source.copy()
```

### Step 16: Assign msg = "You are trying to merge on float64 and object|str columns for key 'A'. If you wish to proceed you should use pd.concat"

```python
msg = "You are trying to merge on float64 and object|str columns for key 'A'. If you wish to proceed you should use pd.concat"
```

### Step 17: Call target.join()

```python
target.join(source, on='E')
```

### Step 18: Call target.join()

```python
target.join(source_copy, on='A')
```


## Complete Example

```python
# Setup
# Fixtures: target_source, infer_string

# Workflow
target, source = target_source
merged = target.join(source, on='C')
tm.assert_series_equal(merged['MergedA'], target['A'], check_names=False)
tm.assert_series_equal(merged['MergedD'], target['D'], check_names=False)
df = DataFrame({'key': ['a', 'a', 'b', 'b', 'c']})
df2 = DataFrame({'value': [0, 1, 2]}, index=['a', 'b', 'c'])
joined = df.join(df2, on='key')
expected = DataFrame({'key': ['a', 'a', 'b', 'b', 'c'], 'value': [0, 0, 1, 1, 2]})
tm.assert_frame_equal(joined, expected)
df_a = DataFrame([[1], [2], [3]], index=['a', 'b', 'c'], columns=['one'])
df_b = DataFrame([['foo'], ['bar']], index=[1, 2], columns=['two'])
df_c = DataFrame([[1], [2]], index=[1, 2], columns=['three'])
joined = df_a.join(df_b, on='one')
joined = joined.join(df_c, on='one')
assert np.isnan(joined['two']['c'])
assert np.isnan(joined['three']['c'])
with pytest.raises(KeyError, match="^'E'$"):
    target.join(source, on='E')
source_copy = source.copy()
msg = "You are trying to merge on float64 and object|str columns for key 'A'. If you wish to proceed you should use pd.concat"
with pytest.raises(ValueError, match=msg):
    target.join(source_copy, on='A')
```

## Next Steps


---

*Source: test_join.py:129 | Complexity: Advanced | Last updated: 2026-06-02*