# How To: Concat Empty Dataframe Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat empty dataframe dtypes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(columns=list('abc'))
```

**Verification:**
```python
assert result['a'].dtype == np.bool_
```

### Step 2: Assign unknown = unknown.astype(...)

```python
df['a'] = df['a'].astype(np.bool_)
```

**Verification:**
```python
assert result['b'].dtype == np.int32
```

### Step 3: Assign unknown = unknown.astype(...)

```python
df['b'] = df['b'].astype(np.int32)
```

**Verification:**
```python
assert result['c'].dtype == np.float64
```

### Step 4: Assign unknown = unknown.astype(...)

```python
df['c'] = df['c'].astype(np.float64)
```

**Verification:**
```python
assert result['a'].dtype == np.object_
```

### Step 5: Assign result = concat(...)

```python
result = concat([df, df])
```

**Verification:**
```python
assert result['b'].dtype == np.float64
```

### Step 6: Assign result = concat(...)

```python
result = concat([df, df.astype(np.float64)])
```

**Verification:**
```python
assert result['c'].dtype == np.float64
```


## Complete Example

```python
# Workflow
df = DataFrame(columns=list('abc'))
df['a'] = df['a'].astype(np.bool_)
df['b'] = df['b'].astype(np.int32)
df['c'] = df['c'].astype(np.float64)
result = concat([df, df])
assert result['a'].dtype == np.bool_
assert result['b'].dtype == np.int32
assert result['c'].dtype == np.float64
result = concat([df, df.astype(np.float64)])
assert result['a'].dtype == np.object_
assert result['b'].dtype == np.float64
assert result['c'].dtype == np.float64
```

## Next Steps


---

*Source: test_empty.py:227 | Complexity: Intermediate | Last updated: 2026-06-02*