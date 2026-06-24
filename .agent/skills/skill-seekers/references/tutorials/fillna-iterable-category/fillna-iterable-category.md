# How To: Fillna Iterable Category

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fillna iterable category

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: named
```

## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(np.array([Point(0, 0), Point(0, 1), None], dtype=object))
```

### Step 2: Assign result = cat.fillna(...)

```python
result = cat.fillna(Point(0, 0))
```

### Step 3: Assign expected = Categorical(...)

```python
expected = Categorical([Point(0, 0), Point(0, 1), Point(0, 0)])
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 5: Assign cat = Categorical(...)

```python
cat = Categorical(np.array([Point(1, 0), Point(0, 1), None], dtype=object))
```

### Step 6: Assign msg = 'Cannot setitem on a Categorical with a new category'

```python
msg = 'Cannot setitem on a Categorical with a new category'
```

### Step 7: Assign Point = collections.namedtuple(...)

```python
Point = collections.namedtuple('Point', 'x y')
```

### Step 8: Assign Point = value

```python
Point = lambda *args: args
```

### Step 9: Call cat.fillna()

```python
cat.fillna(Point(0, 0))
```


## Complete Example

```python
# Setup
# Fixtures: named

# Workflow
if named:
    Point = collections.namedtuple('Point', 'x y')
else:
    Point = lambda *args: args
cat = Categorical(np.array([Point(0, 0), Point(0, 1), None], dtype=object))
result = cat.fillna(Point(0, 0))
expected = Categorical([Point(0, 0), Point(0, 1), Point(0, 0)])
tm.assert_categorical_equal(result, expected)
cat = Categorical(np.array([Point(1, 0), Point(0, 1), None], dtype=object))
msg = 'Cannot setitem on a Categorical with a new category'
with pytest.raises(TypeError, match=msg):
    cat.fillna(Point(0, 0))
```

## Next Steps


---

*Source: test_missing.py:95 | Complexity: Advanced | Last updated: 2026-06-02*