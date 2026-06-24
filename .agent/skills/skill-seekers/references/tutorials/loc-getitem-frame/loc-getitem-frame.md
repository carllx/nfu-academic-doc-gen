# How To: Loc Getitem Frame

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc getitem frame

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(10)})
```

### Step 2: Assign ser = pd.cut(...)

```python
ser = pd.cut(df.A, 5)
```

### Step 3: Assign unknown = ser

```python
df['B'] = ser
```

### Step 4: Assign df = df.set_index(...)

```python
df = df.set_index('B')
```

### Step 5: Assign result = value

```python
result = df.loc[4]
```

### Step 6: Assign expected = value

```python
expected = df.iloc[4:6]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df.loc[[4]]
```

### Step 9: Assign expected = value

```python
expected = df.iloc[4:6]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = df.loc[[4, 5]]
```

### Step 12: Assign expected = df.take(...)

```python
expected = df.take([4, 5, 4, 5])
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign msg = "None of \\[Index\\(\\[10\\], dtype='object', name='B'\\)\\] are in the \\[index\\]"

```python
msg = "None of \\[Index\\(\\[10\\], dtype='object', name='B'\\)\\] are in the \\[index\\]"
```

### Step 15: df.loc[10]

```python
df.loc[10]
```

### Step 16: df.loc[[10]]

```python
df.loc[[10]]
```

### Step 17: df.loc[[10, 4]]

```python
df.loc[[10, 4]]
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': range(10)})
ser = pd.cut(df.A, 5)
df['B'] = ser
df = df.set_index('B')
result = df.loc[4]
expected = df.iloc[4:6]
tm.assert_frame_equal(result, expected)
with pytest.raises(KeyError, match='10'):
    df.loc[10]
result = df.loc[[4]]
expected = df.iloc[4:6]
tm.assert_frame_equal(result, expected)
result = df.loc[[4, 5]]
expected = df.take([4, 5, 4, 5])
tm.assert_frame_equal(result, expected)
msg = "None of \\[Index\\(\\[10\\], dtype='object', name='B'\\)\\] are in the \\[index\\]"
with pytest.raises(KeyError, match=msg):
    df.loc[[10]]
with pytest.raises(KeyError, match='\\[10\\] not in index'):
    df.loc[[10, 4]]
```

## Next Steps


---

*Source: test_interval.py:90 | Complexity: Advanced | Last updated: 2026-06-02*