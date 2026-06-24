# How To: Indexing With Datetime Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing with datetime tz

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(date_range('20130101', periods=3, tz='US/Eastern'), name='foo')
```

### Step 2: Assign dr = date_range(...)

```python
dr = date_range('20130110', periods=3)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': idx, 'B': dr})
```

### Step 4: Assign unknown = idx

```python
df['C'] = idx
```

### Step 5: Assign unknown = value

```python
df.iloc[1, 1] = pd.NaT
```

### Step 6: Assign unknown = value

```python
df.iloc[1, 2] = pd.NaT
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([Timestamp('2013-01-02 00:00:00-0500', tz='US/Eastern'), pd.NaT, pd.NaT], index=list('ABC'), dtype='object', name=1)
```

### Step 8: Assign result = value

```python
result = df.iloc[1]
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = df.loc[1]
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = Index(date_range('20130101', periods=3, tz='US/Eastern'), name='foo')
dr = date_range('20130110', periods=3)
df = DataFrame({'A': idx, 'B': dr})
df['C'] = idx
df.iloc[1, 1] = pd.NaT
df.iloc[1, 2] = pd.NaT
expected = Series([Timestamp('2013-01-02 00:00:00-0500', tz='US/Eastern'), pd.NaT, pd.NaT], index=list('ABC'), dtype='object', name=1)
result = df.iloc[1]
tm.assert_series_equal(result, expected)
result = df.loc[1]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:31 | Complexity: Advanced | Last updated: 2026-06-02*