# How To: Filter Bad Shapes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter bad shapes

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.arange(8), 'B': list('aabbbbcc'), 'C': np.arange(8)})
```

### Step 2: Assign s = value

```python
s = df['B']
```

### Step 3: Assign g_df = df.groupby(...)

```python
g_df = df.groupby('B')
```

### Step 4: Assign g_s = s.groupby(...)

```python
g_s = s.groupby(s)
```

### Step 5: Assign f = value

```python
f = lambda x: x
```

### Step 6: Assign msg = 'filter function returned a DataFrame, but expected a scalar bool'

```python
msg = 'filter function returned a DataFrame, but expected a scalar bool'
```

### Step 7: Assign msg = 'the filter must return a boolean result'

```python
msg = 'the filter must return a boolean result'
```

### Step 8: Assign f = value

```python
f = lambda x: x == 1
```

### Step 9: Assign msg = 'filter function returned a DataFrame, but expected a scalar bool'

```python
msg = 'filter function returned a DataFrame, but expected a scalar bool'
```

### Step 10: Assign msg = 'the filter must return a boolean result'

```python
msg = 'the filter must return a boolean result'
```

### Step 11: Assign f = value

```python
f = lambda x: np.outer(x, x)
```

### Step 12: Assign msg = "can't multiply sequence by non-int of type 'str'"

```python
msg = "can't multiply sequence by non-int of type 'str'"
```

### Step 13: Assign msg = 'the filter must return a boolean result'

```python
msg = 'the filter must return a boolean result'
```

### Step 14: Call g_df.filter()

```python
g_df.filter(f)
```

### Step 15: Call g_s.filter()

```python
g_s.filter(f)
```

### Step 16: Call g_df.filter()

```python
g_df.filter(f)
```

### Step 17: Call g_s.filter()

```python
g_s.filter(f)
```

### Step 18: Call g_df.filter()

```python
g_df.filter(f)
```

### Step 19: Call g_s.filter()

```python
g_s.filter(f)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': np.arange(8), 'B': list('aabbbbcc'), 'C': np.arange(8)})
s = df['B']
g_df = df.groupby('B')
g_s = s.groupby(s)
f = lambda x: x
msg = 'filter function returned a DataFrame, but expected a scalar bool'
with pytest.raises(TypeError, match=msg):
    g_df.filter(f)
msg = 'the filter must return a boolean result'
with pytest.raises(TypeError, match=msg):
    g_s.filter(f)
f = lambda x: x == 1
msg = 'filter function returned a DataFrame, but expected a scalar bool'
with pytest.raises(TypeError, match=msg):
    g_df.filter(f)
msg = 'the filter must return a boolean result'
with pytest.raises(TypeError, match=msg):
    g_s.filter(f)
f = lambda x: np.outer(x, x)
msg = "can't multiply sequence by non-int of type 'str'"
with pytest.raises(TypeError, match=msg):
    g_df.filter(f)
msg = 'the filter must return a boolean result'
with pytest.raises(TypeError, match=msg):
    g_s.filter(f)
```

## Next Steps


---

*Source: test_filters.py:137 | Complexity: Advanced | Last updated: 2026-06-02*