# How To: Melt Missing Columns Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test melt missing columns raises

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=list('abcd'))
```

### Step 2: Assign msg = 'The following id_vars or value_vars are not present in the DataFrame:'

```python
msg = 'The following id_vars or value_vars are not present in the DataFrame:'
```

### Step 3: Assign multi = df.copy(...)

```python
multi = df.copy()
```

### Step 4: Assign multi.columns = value

```python
multi.columns = [list('ABCD'), list('abcd')]
```

### Step 5: Call df.melt()

```python
df.melt(['a', 'b'], ['C', 'd'])
```

### Step 6: Call df.melt()

```python
df.melt(['A', 'b'], ['c', 'd'])
```

### Step 7: Call df.melt()

```python
df.melt(['a', 'b', 'not_here', 'or_there'], ['c', 'd'])
```

### Step 8: Call multi.melt()

```python
multi.melt([('E', 'a')], [('B', 'b')])
```

### Step 9: Call multi.melt()

```python
multi.melt(['A'], ['F'], col_level=0)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((5, 4)), columns=list('abcd'))
msg = 'The following id_vars or value_vars are not present in the DataFrame:'
with pytest.raises(KeyError, match=msg):
    df.melt(['a', 'b'], ['C', 'd'])
with pytest.raises(KeyError, match=msg):
    df.melt(['A', 'b'], ['c', 'd'])
with pytest.raises(KeyError, match=msg):
    df.melt(['a', 'b', 'not_here', 'or_there'], ['c', 'd'])
multi = df.copy()
multi.columns = [list('ABCD'), list('abcd')]
with pytest.raises(KeyError, match=msg):
    multi.melt([('E', 'a')], [('B', 'b')])
with pytest.raises(KeyError, match=msg):
    multi.melt(['A'], ['F'], col_level=0)
```

## Next Steps


---

*Source: test_melt.py:325 | Complexity: Advanced | Last updated: 2026-06-02*