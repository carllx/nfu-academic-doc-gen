# How To: Interleave With Tzaware

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interleave with tzaware

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: timezone_frame
```

## Step-by-Step Guide

### Step 1: Assign result = value

```python
result = timezone_frame.assign(D='foo').values
```

### Step 2: Assign expected = value

```python
expected = np.array([[Timestamp('2013-01-01 00:00:00'), Timestamp('2013-01-02 00:00:00'), Timestamp('2013-01-03 00:00:00')], [Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern'), NaT, Timestamp('2013-01-03 00:00:00-0500', tz='US/Eastern')], [Timestamp('2013-01-01 00:00:00+0100', tz='CET'), NaT, Timestamp('2013-01-03 00:00:00+0100', tz='CET')], ['foo', 'foo', 'foo']], dtype=object).T
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 4: Assign result = value

```python
result = timezone_frame.values
```

### Step 5: Assign expected = value

```python
expected = np.array([[Timestamp('2013-01-01 00:00:00'), Timestamp('2013-01-02 00:00:00'), Timestamp('2013-01-03 00:00:00')], [Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern'), NaT, Timestamp('2013-01-03 00:00:00-0500', tz='US/Eastern')], [Timestamp('2013-01-01 00:00:00+0100', tz='CET'), NaT, Timestamp('2013-01-03 00:00:00+0100', tz='CET')]], dtype=object).T
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: timezone_frame

# Workflow
result = timezone_frame.assign(D='foo').values
expected = np.array([[Timestamp('2013-01-01 00:00:00'), Timestamp('2013-01-02 00:00:00'), Timestamp('2013-01-03 00:00:00')], [Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern'), NaT, Timestamp('2013-01-03 00:00:00-0500', tz='US/Eastern')], [Timestamp('2013-01-01 00:00:00+0100', tz='CET'), NaT, Timestamp('2013-01-03 00:00:00+0100', tz='CET')], ['foo', 'foo', 'foo']], dtype=object).T
tm.assert_numpy_array_equal(result, expected)
result = timezone_frame.values
expected = np.array([[Timestamp('2013-01-01 00:00:00'), Timestamp('2013-01-02 00:00:00'), Timestamp('2013-01-03 00:00:00')], [Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern'), NaT, Timestamp('2013-01-03 00:00:00-0500', tz='US/Eastern')], [Timestamp('2013-01-01 00:00:00+0100', tz='CET'), NaT, Timestamp('2013-01-03 00:00:00+0100', tz='CET')]], dtype=object).T
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_values.py:124 | Complexity: Intermediate | Last updated: 2026-06-02*