# How To: Append With Diff Col Name Types Raises Value Error

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append with diff col name types raises value error

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 1)))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'a': np.random.default_rng(2).standard_normal(10)})
```

### Step 3: Assign df3 = DataFrame(...)

```python
df3 = DataFrame({(1, 2): np.random.default_rng(2).standard_normal(10)})
```

### Step 4: Assign df4 = DataFrame(...)

```python
df4 = DataFrame({('1', 2): np.random.default_rng(2).standard_normal(10)})
```

### Step 5: Assign df5 = DataFrame(...)

```python
df5 = DataFrame({('1', 2, object): np.random.default_rng(2).standard_normal(10)})
```

### Step 6: Assign name = 'df_diff_valerror'

```python
name = 'df_diff_valerror'
```

### Step 7: Call store.append()

```python
store.append(name, df)
```

### Step 8: Assign msg = re.escape(...)

```python
msg = re.escape('cannot match existing table structure for [0] on appending data')
```

### Step 9: Call store.append()

```python
store.append(name, d)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 1)))
df2 = DataFrame({'a': np.random.default_rng(2).standard_normal(10)})
df3 = DataFrame({(1, 2): np.random.default_rng(2).standard_normal(10)})
df4 = DataFrame({('1', 2): np.random.default_rng(2).standard_normal(10)})
df5 = DataFrame({('1', 2, object): np.random.default_rng(2).standard_normal(10)})
with ensure_clean_store(setup_path) as store:
    name = 'df_diff_valerror'
    store.append(name, df)
    for d in (df2, df3, df4, df5):
        msg = re.escape('cannot match existing table structure for [0] on appending data')
        with pytest.raises(ValueError, match=msg):
            store.append(name, d)
```

## Next Steps


---

*Source: test_errors.py:166 | Complexity: Advanced | Last updated: 2026-06-02*