# How To: Concat With Various Multiindex Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat with various multiindex dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: mi1_list, mi2_list
```

## Step-by-Step Guide

### Step 1: Assign mi1 = MultiIndex.from_product(...)

```python
mi1 = MultiIndex.from_product(mi1_list)
```

### Step 2: Assign mi2 = MultiIndex.from_product(...)

```python
mi2 = MultiIndex.from_product(mi2_list)
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.zeros((1, len(mi1))), columns=mi1)
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.zeros((1, len(mi2))), columns=mi2)
```

### Step 5: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame(np.zeros((1, len(expected_mi))), columns=expected_mi)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected_df, result_df)
```

### Step 7: Assign expected_mi = MultiIndex(...)

```python
expected_mi = MultiIndex(levels=[mi1_list[0], list(mi1_list[1])], codes=[[0, 0, 0, 0], [0, 1, 0, 1]])
```

### Step 8: Assign expected_mi = MultiIndex(...)

```python
expected_mi = MultiIndex(levels=[mi1_list[0] + mi2_list[0], list(mi1_list[1]) + list(mi2_list[1])], codes=[[0, 0, 1, 1], [0, 1, 2, 3]])
```

### Step 9: Assign result_df = concat(...)

```python
result_df = concat((df1, df2), axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: mi1_list, mi2_list

# Workflow
mi1 = MultiIndex.from_product(mi1_list)
mi2 = MultiIndex.from_product(mi2_list)
df1 = DataFrame(np.zeros((1, len(mi1))), columns=mi1)
df2 = DataFrame(np.zeros((1, len(mi2))), columns=mi2)
if mi1_list[0] == mi2_list[0]:
    expected_mi = MultiIndex(levels=[mi1_list[0], list(mi1_list[1])], codes=[[0, 0, 0, 0], [0, 1, 0, 1]])
else:
    expected_mi = MultiIndex(levels=[mi1_list[0] + mi2_list[0], list(mi1_list[1]) + list(mi2_list[1])], codes=[[0, 0, 1, 1], [0, 1, 2, 3]])
expected_df = DataFrame(np.zeros((1, len(expected_mi))), columns=expected_mi)
with tm.assert_produces_warning(None):
    result_df = concat((df1, df2), axis=1)
tm.assert_frame_equal(expected_df, result_df)
```

## Next Steps


---

*Source: test_index.py:295 | Complexity: Advanced | Last updated: 2026-06-02*