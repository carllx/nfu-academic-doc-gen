# How To: Getitem Scalar Categorical Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem scalar categorical index

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign cats = Categorical(...)

```python
cats = Categorical([Timestamp('12-31-1999'), Timestamp('12-31-2000')])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2], index=cats)
```

### Step 3: Assign expected = value

```python
expected = ser.iloc[0]
```

### Step 4: Assign result = value

```python
result = ser[cats[0]]
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
cats = Categorical([Timestamp('12-31-1999'), Timestamp('12-31-2000')])
ser = Series([1, 2], index=cats)
expected = ser.iloc[0]
result = ser[cats[0]]
assert result == expected
```

## Next Steps


---

*Source: test_getitem.py:170 | Complexity: Intermediate | Last updated: 2026-06-02*