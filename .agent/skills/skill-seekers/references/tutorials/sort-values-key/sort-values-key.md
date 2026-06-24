# How To: Sort Values Key

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values key

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['bar', 'bar', 'baz', 'baz', 'qux', 'qux', 'foo', 'foo'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

### Step 2: Assign tuples = zip(...)

```python
tuples = zip(*arrays)
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

### Step 4: Assign index = index.sort_values(...)

```python
index = index.sort_values(key=lambda x: x.map(lambda entry: entry[2]))
```

### Step 5: Assign result = DataFrame(...)

```python
result = DataFrame(range(8), index=index)
```

### Step 6: Assign arrays = value

```python
arrays = [['foo', 'foo', 'bar', 'bar', 'qux', 'qux', 'baz', 'baz'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

### Step 7: Assign tuples = zip(...)

```python
tuples = zip(*arrays)
```

### Step 8: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(range(8), index=index)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [['bar', 'bar', 'baz', 'baz', 'qux', 'qux', 'foo', 'foo'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
index = index.sort_values(key=lambda x: x.map(lambda entry: entry[2]))
result = DataFrame(range(8), index=index)
arrays = [['foo', 'foo', 'bar', 'bar', 'qux', 'qux', 'baz', 'baz'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
expected = DataFrame(range(8), index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sorted.py:63 | Complexity: Advanced | Last updated: 2026-06-02*