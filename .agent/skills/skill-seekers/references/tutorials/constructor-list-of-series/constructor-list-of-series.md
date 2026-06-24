# How To: Constructor List Of Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor list of series

## Prerequisites

**Required Modules:**
- `collections`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [OrderedDict([['a', 1.5], ['b', 3.0], ['c', 4.0]]), OrderedDict([['a', 1.5], ['b', 3.0], ['c', 6.0]])]
```

### Step 2: Assign sdict = OrderedDict(...)

```python
sdict = OrderedDict(zip(['x', 'y'], data))
```

### Step 3: Assign idx = Index(...)

```python
idx = Index(['a', 'b', 'c'])
```

### Step 4: Assign data2 = value

```python
data2 = [Series([1.5, 3, 4], idx, dtype='O', name='x'), Series([1.5, 3, 6], idx, name='y')]
```

### Step 5: Assign result = DataFrame(...)

```python
result = DataFrame(data2)
```

### Step 6: Assign expected = DataFrame.from_dict(...)

```python
expected = DataFrame.from_dict(sdict, orient='index')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign data2 = value

```python
data2 = [Series([1.5, 3, 4], idx, dtype='O', name='x'), Series([1.5, 3, 6], idx)]
```

### Step 9: Assign result = DataFrame(...)

```python
result = DataFrame(data2)
```

### Step 10: Assign sdict = OrderedDict(...)

```python
sdict = OrderedDict(zip(['x', 'Unnamed 0'], data))
```

### Step 11: Assign expected = DataFrame.from_dict(...)

```python
expected = DataFrame.from_dict(sdict, orient='index')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign data = value

```python
data = [OrderedDict([['a', 1.5], ['b', 3], ['c', 4], ['d', 6]]), OrderedDict([['a', 1.5], ['b', 3], ['d', 6]]), OrderedDict([['a', 1.5], ['d', 6]]), OrderedDict(), OrderedDict([['a', 1.5], ['b', 3], ['c', 4]]), OrderedDict([['b', 3], ['c', 4], ['d', 6]])]
```

### Step 14: Assign data = value

```python
data = [Series(d) for d in data]
```

### Step 15: Assign result = DataFrame(...)

```python
result = DataFrame(data)
```

### Step 16: Assign sdict = OrderedDict(...)

```python
sdict = OrderedDict(zip(range(len(data)), data))
```

### Step 17: Assign expected = DataFrame.from_dict(...)

```python
expected = DataFrame.from_dict(sdict, orient='index')
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected.reindex(result.index))
```

### Step 19: Assign result2 = DataFrame(...)

```python
result2 = DataFrame(data, index=np.arange(6, dtype=np.int64))
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, result2)
```

### Step 21: Assign result = DataFrame(...)

```python
result = DataFrame([Series(dtype=object)])
```

### Step 22: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=[0])
```

### Step 23: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 24: Assign data = value

```python
data = [OrderedDict([['a', 1.5], ['b', 3.0], ['c', 4.0]]), OrderedDict([['a', 1.5], ['b', 3.0], ['c', 6.0]])]
```

### Step 25: Assign sdict = OrderedDict(...)

```python
sdict = OrderedDict(zip(range(len(data)), data))
```

### Step 26: Assign idx = Index(...)

```python
idx = Index(['a', 'b', 'c'])
```

### Step 27: Assign data2 = value

```python
data2 = [Series([1.5, 3, 4], idx, dtype='O'), Series([1.5, 3, 6], idx)]
```

### Step 28: Assign result = DataFrame(...)

```python
result = DataFrame(data2)
```

### Step 29: Assign expected = DataFrame.from_dict(...)

```python
expected = DataFrame.from_dict(sdict, orient='index')
```

### Step 30: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = [OrderedDict([['a', 1.5], ['b', 3.0], ['c', 4.0]]), OrderedDict([['a', 1.5], ['b', 3.0], ['c', 6.0]])]
sdict = OrderedDict(zip(['x', 'y'], data))
idx = Index(['a', 'b', 'c'])
data2 = [Series([1.5, 3, 4], idx, dtype='O', name='x'), Series([1.5, 3, 6], idx, name='y')]
result = DataFrame(data2)
expected = DataFrame.from_dict(sdict, orient='index')
tm.assert_frame_equal(result, expected)
data2 = [Series([1.5, 3, 4], idx, dtype='O', name='x'), Series([1.5, 3, 6], idx)]
result = DataFrame(data2)
sdict = OrderedDict(zip(['x', 'Unnamed 0'], data))
expected = DataFrame.from_dict(sdict, orient='index')
tm.assert_frame_equal(result, expected)
data = [OrderedDict([['a', 1.5], ['b', 3], ['c', 4], ['d', 6]]), OrderedDict([['a', 1.5], ['b', 3], ['d', 6]]), OrderedDict([['a', 1.5], ['d', 6]]), OrderedDict(), OrderedDict([['a', 1.5], ['b', 3], ['c', 4]]), OrderedDict([['b', 3], ['c', 4], ['d', 6]])]
data = [Series(d) for d in data]
result = DataFrame(data)
sdict = OrderedDict(zip(range(len(data)), data))
expected = DataFrame.from_dict(sdict, orient='index')
tm.assert_frame_equal(result, expected.reindex(result.index))
result2 = DataFrame(data, index=np.arange(6, dtype=np.int64))
tm.assert_frame_equal(result, result2)
result = DataFrame([Series(dtype=object)])
expected = DataFrame(index=[0])
tm.assert_frame_equal(result, expected)
data = [OrderedDict([['a', 1.5], ['b', 3.0], ['c', 4.0]]), OrderedDict([['a', 1.5], ['b', 3.0], ['c', 6.0]])]
sdict = OrderedDict(zip(range(len(data)), data))
idx = Index(['a', 'b', 'c'])
data2 = [Series([1.5, 3, 4], idx, dtype='O'), Series([1.5, 3, 6], idx)]
result = DataFrame(data2)
expected = DataFrame.from_dict(sdict, orient='index')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_dict.py:45 | Complexity: Advanced | Last updated: 2026-06-02*