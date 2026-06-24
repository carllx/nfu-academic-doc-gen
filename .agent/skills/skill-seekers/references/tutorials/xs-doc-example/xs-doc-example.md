# How To: Xs Doc Example

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs doc example

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

### Step 2: Assign tuples = list(...)

```python
tuples = list(zip(*arrays))
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples, names=['first', 'second'])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 8)), index=['A', 'B', 'C'], columns=index)
```

### Step 5: Assign result = df.xs(...)

```python
result = df.xs(('one', 'bar'), level=('second', 'first'), axis=1)
```

### Step 6: Assign expected = value

```python
expected = df.iloc[:, [0]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = DataFrame(np.random.default_rng(2).standard_normal((3, 8)), index=['A', 'B', 'C'], columns=index)
result = df.xs(('one', 'bar'), level=('second', 'first'), axis=1)
expected = df.iloc[:, [0]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*