# How To: Multiindex With Datatime Level Preserves Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex with datatime level preserves freq

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.index`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(range(2), name='A')
```

**Verification:**
```python
assert result.freq == dti.freq
```

### Step 2: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2020-01-01', periods=7, freq='D', name='B')
```

### Step 3: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([idx, dti])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((14, 2)), index=mi)
```

### Step 5: Assign result = value

```python
result = df.loc[0].index
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, dti)
```

**Verification:**
```python
assert result.freq == dti.freq
```


## Complete Example

```python
# Workflow
idx = Index(range(2), name='A')
dti = pd.date_range('2020-01-01', periods=7, freq='D', name='B')
mi = MultiIndex.from_product([idx, dti])
df = DataFrame(np.random.default_rng(2).standard_normal((14, 2)), index=mi)
result = df.loc[0].index
tm.assert_index_equal(result, dti)
assert result.freq == dti.freq
```

## Next Steps


---

*Source: test_multiindex.py:114 | Complexity: Intermediate | Last updated: 2026-06-02*