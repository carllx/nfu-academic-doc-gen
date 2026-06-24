# How To: Append Overlapping Interval Levels

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append overlapping interval levels

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ivl1 = pd.IntervalIndex.from_breaks(...)

```python
ivl1 = pd.IntervalIndex.from_breaks([0.0, 1.0, 2.0])
```

### Step 2: Assign ivl2 = pd.IntervalIndex.from_breaks(...)

```python
ivl2 = pd.IntervalIndex.from_breaks([0.5, 1.5, 2.5])
```

### Step 3: Assign mi1 = MultiIndex.from_product(...)

```python
mi1 = MultiIndex.from_product([ivl1, ivl1])
```

### Step 4: Assign mi2 = MultiIndex.from_product(...)

```python
mi2 = MultiIndex.from_product([ivl2, ivl2])
```

### Step 5: Assign result = mi1.append(...)

```python
result = mi1.append(mi2)
```

### Step 6: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples([(pd.Interval(0.0, 1.0), pd.Interval(0.0, 1.0)), (pd.Interval(0.0, 1.0), pd.Interval(1.0, 2.0)), (pd.Interval(1.0, 2.0), pd.Interval(0.0, 1.0)), (pd.Interval(1.0, 2.0), pd.Interval(1.0, 2.0)), (pd.Interval(0.5, 1.5), pd.Interval(0.5, 1.5)), (pd.Interval(0.5, 1.5), pd.Interval(1.5, 2.5)), (pd.Interval(1.5, 2.5), pd.Interval(0.5, 1.5)), (pd.Interval(1.5, 2.5), pd.Interval(1.5, 2.5))])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
ivl1 = pd.IntervalIndex.from_breaks([0.0, 1.0, 2.0])
ivl2 = pd.IntervalIndex.from_breaks([0.5, 1.5, 2.5])
mi1 = MultiIndex.from_product([ivl1, ivl1])
mi2 = MultiIndex.from_product([ivl2, ivl2])
result = mi1.append(mi2)
expected = MultiIndex.from_tuples([(pd.Interval(0.0, 1.0), pd.Interval(0.0, 1.0)), (pd.Interval(0.0, 1.0), pd.Interval(1.0, 2.0)), (pd.Interval(1.0, 2.0), pd.Interval(0.0, 1.0)), (pd.Interval(1.0, 2.0), pd.Interval(1.0, 2.0)), (pd.Interval(0.5, 1.5), pd.Interval(0.5, 1.5)), (pd.Interval(0.5, 1.5), pd.Interval(1.5, 2.5)), (pd.Interval(1.5, 2.5), pd.Interval(0.5, 1.5)), (pd.Interval(1.5, 2.5), pd.Interval(1.5, 2.5))])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_reshape.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*