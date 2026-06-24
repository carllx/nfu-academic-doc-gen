# How To: Categorical Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: categorical frame

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `decimal`
- `io`
- `json`
- `os`
- `sys`
- `time`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json`
- `pandas.arrays`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {c: np.random.default_rng(i).standard_normal(30) for i, c in enumerate(list('ABCD'))}
```

### Step 2: Assign cat = value

```python
cat = ['bah'] * 5 + ['bar'] * 5 + ['baz'] * 5 + ['foo'] * 15
```

### Step 3: Assign unknown = list(...)

```python
data['E'] = list(reversed(cat))
```

### Step 4: Assign unknown = np.arange(...)

```python
data['sort'] = np.arange(30, dtype='int64')
```


## Complete Example

```python
# Workflow
data = {c: np.random.default_rng(i).standard_normal(30) for i, c in enumerate(list('ABCD'))}
cat = ['bah'] * 5 + ['bar'] * 5 + ['baz'] * 5 + ['foo'] * 15
data['E'] = list(reversed(cat))
data['sort'] = np.arange(30, dtype='int64')
return DataFrame(data, index=pd.CategoricalIndex(cat, name='E'))
```

## Next Steps


---

*Source: test_pandas.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*