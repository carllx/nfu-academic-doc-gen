# How To: Reset Index With Drop

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index with drop

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['bar', 'bar', 'baz', 'baz', 'qux', 'qux', 'foo', 'foo'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

**Verification:**
```python
assert isinstance(deleveled, DataFrame)
```

### Step 2: Assign tuples = zip(...)

```python
tuples = zip(*arrays)
```

**Verification:**
```python
assert len(deleveled.columns) == len(ser.index.levels) + 1
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

**Verification:**
```python
assert deleveled.index.name == ser.index.name
```

### Step 4: Assign data = np.random.default_rng.standard_normal(...)

```python
data = np.random.default_rng(2).standard_normal(8)
```

**Verification:**
```python
assert isinstance(deleveled, Series)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(data, index=index)
```

**Verification:**
```python
assert deleveled.index.name == ser.index.name
```

### Step 6: Assign unknown = value

```python
ser.iloc[3] = np.nan
```

### Step 7: Assign deleveled = ser.reset_index(...)

```python
deleveled = ser.reset_index()
```

**Verification:**
```python
assert isinstance(deleveled, DataFrame)
```

### Step 8: Assign deleveled = ser.reset_index(...)

```python
deleveled = ser.reset_index(drop=True)
```

**Verification:**
```python
assert isinstance(deleveled, Series)
```


## Complete Example

```python
# Workflow
arrays = [['bar', 'bar', 'baz', 'baz', 'qux', 'qux', 'foo', 'foo'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
data = np.random.default_rng(2).standard_normal(8)
ser = Series(data, index=index)
ser.iloc[3] = np.nan
deleveled = ser.reset_index()
assert isinstance(deleveled, DataFrame)
assert len(deleveled.columns) == len(ser.index.levels) + 1
assert deleveled.index.name == ser.index.name
deleveled = ser.reset_index(drop=True)
assert isinstance(deleveled, Series)
assert deleveled.index.name == ser.index.name
```

## Next Steps


---

*Source: test_reset_index.py:144 | Complexity: Advanced | Last updated: 2026-06-02*