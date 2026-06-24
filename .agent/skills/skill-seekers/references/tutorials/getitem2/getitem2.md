# How To: Getitem2

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign df = float_frame.copy(...)

```python
df = float_frame.copy()
```

### Step 2: Assign unknown = np.random.default_rng.standard_normal(...)

```python
df['$10'] = np.random.default_rng(2).standard_normal(len(df))
```

### Step 3: Assign ad = np.random.default_rng.standard_normal(...)

```python
ad = np.random.default_rng(2).standard_normal(len(df))
```

### Step 4: Assign unknown = ad

```python
df['@awesome_domain'] = ad
```

### Step 5: Assign res = value

```python
res = df['@awesome_domain']
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ad, res.values)
```

### Step 7: Call df.__getitem__()

```python
df.__getitem__('df["$10"]')
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
df = float_frame.copy()
df['$10'] = np.random.default_rng(2).standard_normal(len(df))
ad = np.random.default_rng(2).standard_normal(len(df))
df['@awesome_domain'] = ad
with pytest.raises(KeyError, match=re.escape('\'df["$10"]\'')):
    df.__getitem__('df["$10"]')
res = df['@awesome_domain']
tm.assert_numpy_array_equal(ad, res.values)
```

## Next Steps


---

*Source: test_indexing.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*