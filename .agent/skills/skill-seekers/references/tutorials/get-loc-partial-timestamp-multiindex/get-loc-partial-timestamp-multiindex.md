# How To: Get Loc Partial Timestamp Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc partial timestamp multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign mi = value

```python
mi = df.index
```

### Step 2: Assign key = value

```python
key = ('2016-01-01', 'a')
```

### Step 3: Assign loc = mi.get_loc(...)

```python
loc = mi.get_loc(key)
```

### Step 4: Assign expected = np.zeros(...)

```python
expected = np.zeros(len(mi), dtype=bool)
```

### Step 5: Assign unknown = True

```python
expected[[0, 3]] = True
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(loc, expected)
```

### Step 7: Assign key2 = value

```python
key2 = ('2016-01-02', 'a')
```

### Step 8: Assign loc2 = mi.get_loc(...)

```python
loc2 = mi.get_loc(key2)
```

### Step 9: Assign expected2 = np.zeros(...)

```python
expected2 = np.zeros(len(mi), dtype=bool)
```

### Step 10: Assign unknown = True

```python
expected2[[6, 9]] = True
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(loc2, expected2)
```

### Step 12: Assign key3 = value

```python
key3 = ('2016-01', 'a')
```

### Step 13: Assign loc3 = mi.get_loc(...)

```python
loc3 = mi.get_loc(key3)
```

### Step 14: Assign expected3 = np.zeros(...)

```python
expected3 = np.zeros(len(mi), dtype=bool)
```

### Step 15: Assign unknown = True

```python
expected3[mi.get_level_values(1).get_loc('a')] = True
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(loc3, expected3)
```

### Step 17: Assign key4 = value

```python
key4 = ('2016', 'a')
```

### Step 18: Assign loc4 = mi.get_loc(...)

```python
loc4 = mi.get_loc(key4)
```

### Step 19: Assign expected4 = expected3

```python
expected4 = expected3
```

### Step 20: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(loc4, expected4)
```

### Step 21: Assign taker = np.arange(...)

```python
taker = np.arange(len(mi), dtype=np.intp)
```

### Step 22: Assign unknown = value

```python
taker[::2] = taker[::-2]
```

### Step 23: Assign mi2 = mi.take(...)

```python
mi2 = mi.take(taker)
```

### Step 24: Assign loc5 = mi2.get_loc(...)

```python
loc5 = mi2.get_loc(key)
```

### Step 25: Assign expected5 = np.zeros(...)

```python
expected5 = np.zeros(len(mi2), dtype=bool)
```

### Step 26: Assign unknown = True

```python
expected5[[3, 14]] = True
```

### Step 27: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(loc5, expected5)
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
mi = df.index
key = ('2016-01-01', 'a')
loc = mi.get_loc(key)
expected = np.zeros(len(mi), dtype=bool)
expected[[0, 3]] = True
tm.assert_numpy_array_equal(loc, expected)
key2 = ('2016-01-02', 'a')
loc2 = mi.get_loc(key2)
expected2 = np.zeros(len(mi), dtype=bool)
expected2[[6, 9]] = True
tm.assert_numpy_array_equal(loc2, expected2)
key3 = ('2016-01', 'a')
loc3 = mi.get_loc(key3)
expected3 = np.zeros(len(mi), dtype=bool)
expected3[mi.get_level_values(1).get_loc('a')] = True
tm.assert_numpy_array_equal(loc3, expected3)
key4 = ('2016', 'a')
loc4 = mi.get_loc(key4)
expected4 = expected3
tm.assert_numpy_array_equal(loc4, expected4)
taker = np.arange(len(mi), dtype=np.intp)
taker[::2] = taker[::-2]
mi2 = mi.take(taker)
loc5 = mi2.get_loc(key)
expected5 = np.zeros(len(mi2), dtype=bool)
expected5[[3, 14]] = True
tm.assert_numpy_array_equal(loc5, expected5)
```

## Next Steps


---

*Source: test_partial_indexing.py:49 | Complexity: Advanced | Last updated: 2026-06-02*