# How To: Constructor Arrays Negative Year

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor arrays negative year

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign years = np.arange.repeat(...)

```python
years = np.arange(1960, 2000, dtype=np.int64).repeat(4)
```

### Step 2: Assign quarters = np.tile(...)

```python
quarters = np.tile(np.array([1, 2, 3, 4], dtype=np.int64), 40)
```

### Step 3: Assign msg = 'Constructing PeriodIndex from fields is deprecated'

```python
msg = 'Constructing PeriodIndex from fields is deprecated'
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pindex.year, Index(years))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pindex.quarter, Index(quarters))
```

### Step 6: Assign alt = PeriodIndex.from_fields(...)

```python
alt = PeriodIndex.from_fields(year=years, quarter=quarters)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(alt, pindex)
```

### Step 8: Assign pindex = PeriodIndex(...)

```python
pindex = PeriodIndex(year=years, quarter=quarters)
```


## Complete Example

```python
# Workflow
years = np.arange(1960, 2000, dtype=np.int64).repeat(4)
quarters = np.tile(np.array([1, 2, 3, 4], dtype=np.int64), 40)
msg = 'Constructing PeriodIndex from fields is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    pindex = PeriodIndex(year=years, quarter=quarters)
tm.assert_index_equal(pindex.year, Index(years))
tm.assert_index_equal(pindex.quarter, Index(quarters))
alt = PeriodIndex.from_fields(year=years, quarter=quarters)
tm.assert_index_equal(alt, pindex)
```

## Next Steps


---

*Source: test_constructors.py:210 | Complexity: Advanced | Last updated: 2026-06-02*