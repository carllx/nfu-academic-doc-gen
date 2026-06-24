# How To: Partial Set Empty Frame No Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial set empty frame no index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: Series(1, index=range(4))}, columns=['A', 'B', 0])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['A', 'B'])
```

### Step 3: Assign unknown = Series(...)

```python
df[0] = Series(1, index=range(4))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['A', 'B'])
```

### Step 6: Assign unknown = Series(...)

```python
df.loc[:, 0] = Series(1, index=range(4))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
expected = DataFrame({0: Series(1, index=range(4))}, columns=['A', 'B', 0])
df = DataFrame(columns=['A', 'B'])
df[0] = Series(1, index=range(4))
tm.assert_frame_equal(df, expected)
df = DataFrame(columns=['A', 'B'])
df.loc[:, 0] = Series(1, index=range(4))
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_partial.py:148 | Complexity: Intermediate | Last updated: 2026-06-02*