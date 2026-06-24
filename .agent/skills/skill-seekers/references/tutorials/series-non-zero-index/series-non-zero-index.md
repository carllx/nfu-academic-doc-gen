# How To: Series Non Zero Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series non zero index

## Prerequisites

**Required Modules:**
- `json`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.json._normalize`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {0: {'id': 1, 'name': 'Foo', 'elements': {'a': 1}}, 1: {'id': 2, 'name': 'Bar', 'elements': {'b': 2}}, 2: {'id': 3, 'name': 'Baz', 'elements': {'c': 3}}}
```

### Step 2: Assign s = Series(...)

```python
s = Series(data)
```

### Step 3: Assign s.index = value

```python
s.index = [1, 2, 3]
```

### Step 4: Assign result = json_normalize(...)

```python
result = json_normalize(s)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'id': [1, 2, 3], 'name': ['Foo', 'Bar', 'Baz'], 'elements.a': [1.0, np.nan, np.nan], 'elements.b': [np.nan, 2.0, np.nan], 'elements.c': [np.nan, np.nan, 3.0]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = {0: {'id': 1, 'name': 'Foo', 'elements': {'a': 1}}, 1: {'id': 2, 'name': 'Bar', 'elements': {'b': 2}}, 2: {'id': 3, 'name': 'Baz', 'elements': {'c': 3}}}
s = Series(data)
s.index = [1, 2, 3]
result = json_normalize(s)
expected = DataFrame({'id': [1, 2, 3], 'name': ['Foo', 'Bar', 'Baz'], 'elements.a': [1.0, np.nan, np.nan], 'elements.b': [np.nan, 2.0, np.nan], 'elements.c': [np.nan, np.nan, 3.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_normalize.py:888 | Complexity: Intermediate | Last updated: 2026-06-02*