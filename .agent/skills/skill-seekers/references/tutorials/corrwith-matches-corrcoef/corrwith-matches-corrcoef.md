# How To: Corrwith Matches Corrcoef

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corrwith matches corrcoef

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.arange(10000), columns=['a'])
```

**Verification:**
```python
assert c1 < 1
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.arange(10000) ** 2, columns=['a'])
```

### Step 3: Assign c1 = value

```python
c1 = df1.corrwith(df2)['a']
```

### Step 4: Assign c2 = value

```python
c2 = np.corrcoef(df1['a'], df2['a'])[0][1]
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(c1, c2)
```

**Verification:**
```python
assert c1 < 1
```


## Complete Example

```python
# Workflow
df1 = DataFrame(np.arange(10000), columns=['a'])
df2 = DataFrame(np.arange(10000) ** 2, columns=['a'])
c1 = df1.corrwith(df2)['a']
c2 = np.corrcoef(df1['a'], df2['a'])[0][1]
tm.assert_almost_equal(c1, c2)
assert c1 < 1
```

## Next Steps


---

*Source: test_cov_corr.py:364 | Complexity: Intermediate | Last updated: 2026-06-02*