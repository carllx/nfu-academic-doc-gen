# How To: Concat With All Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat with all na

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.extension.array_with_attr`


## Step-by-Step Guide

### Step 1: Assign arr = FloatAttrArray(...)

```python
arr = FloatAttrArray(np.array([np.nan, np.nan], dtype='float64'), attr='test')
```

**Verification:**
```python
assert result['col'].array.attr == 'test'
```

### Step 2: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'col': arr, 'key': [0, 1]})
```

**Verification:**
```python
assert result['col'].array.attr == 'test'
```

### Step 3: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame({'key': [0, 1], 'col2': [1, 2]})
```

**Verification:**
```python
assert result['col'].array.attr == 'test'
```

### Step 4: Assign result = pd.merge(...)

```python
result = pd.merge(df1, df2, on='key')
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'col': arr, 'key': [0, 1], 'col2': [1, 2]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert result['col'].array.attr == 'test'
```

### Step 7: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'col': arr, 'key': [0, 1]})
```

### Step 8: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame({'key': [0, 2], 'col2': [1, 2]})
```

### Step 9: Assign result = pd.merge(...)

```python
result = pd.merge(df1, df2, on='key')
```

### Step 10: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'col': arr.take([0]), 'key': [0], 'col2': [1]})
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert result['col'].array.attr == 'test'
```

### Step 12: Assign result = pd.concat(...)

```python
result = pd.concat([df1.set_index('key'), df2.set_index('key')], axis=1)
```

### Step 13: Assign expected = pd.DataFrame.set_index(...)

```python
expected = pd.DataFrame({'col': arr.take([0, 1, -1]), 'col2': [1, np.nan, 2], 'key': [0, 1, 2]}).set_index('key')
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert result['col'].array.attr == 'test'
```


## Complete Example

```python
# Workflow
arr = FloatAttrArray(np.array([np.nan, np.nan], dtype='float64'), attr='test')
df1 = pd.DataFrame({'col': arr, 'key': [0, 1]})
df2 = pd.DataFrame({'key': [0, 1], 'col2': [1, 2]})
result = pd.merge(df1, df2, on='key')
expected = pd.DataFrame({'col': arr, 'key': [0, 1], 'col2': [1, 2]})
tm.assert_frame_equal(result, expected)
assert result['col'].array.attr == 'test'
df1 = pd.DataFrame({'col': arr, 'key': [0, 1]})
df2 = pd.DataFrame({'key': [0, 2], 'col2': [1, 2]})
result = pd.merge(df1, df2, on='key')
expected = pd.DataFrame({'col': arr.take([0]), 'key': [0], 'col2': [1]})
tm.assert_frame_equal(result, expected)
assert result['col'].array.attr == 'test'
result = pd.concat([df1.set_index('key'), df2.set_index('key')], axis=1)
expected = pd.DataFrame({'col': arr.take([0, 1, -1]), 'col2': [1, np.nan, 2], 'key': [0, 1, 2]}).set_index('key')
tm.assert_frame_equal(result, expected)
assert result['col'].array.attr == 'test'
```

## Next Steps


---

*Source: test_array_with_attr.py:8 | Complexity: Advanced | Last updated: 2026-06-02*