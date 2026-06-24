# How To: Ts Plot Format Coord

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ts plot format coord

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.indexes.timedeltas`
- `pandas.tests.plotting.common`
- `pandas.tseries.offsets`
- `matplotlib.pyplot`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`


## Step-by-Step Guide

### Step 1: Assign annual = Series(...)

```python
annual = Series(1, index=date_range('2014-01-01', periods=3, freq='YE-DEC'))
```

**Verification:**
```python
assert expected_string == ax.format_coord(first_x, first_y)
```

### Step 2: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

### Step 3: Call annual.plot()

```python
annual.plot(ax=ax)
```

### Step 4: Call check_format_of_first_point()

```python
check_format_of_first_point(ax, 't = 2014  y = 1.000000')
```

### Step 5: Assign daily = Series(...)

```python
daily = Series(1, index=date_range('2014-01-01', periods=3, freq='D'))
```

### Step 6: Call daily.plot()

```python
daily.plot(ax=ax)
```

### Step 7: Call check_format_of_first_point()

```python
check_format_of_first_point(ax, 't = 2014-01-01  y = 1.000000')
```

### Step 8: Assign first_line = value

```python
first_line = ax.get_lines()[0]
```

### Step 9: Assign first_x = value

```python
first_x = first_line.get_xdata()[0].ordinal
```

### Step 10: Assign first_y = value

```python
first_y = first_line.get_ydata()[0]
```

**Verification:**
```python
assert expected_string == ax.format_coord(first_x, first_y)
```


## Complete Example

```python
# Workflow
def check_format_of_first_point(ax, expected_string):
    first_line = ax.get_lines()[0]
    first_x = first_line.get_xdata()[0].ordinal
    first_y = first_line.get_ydata()[0]
    assert expected_string == ax.format_coord(first_x, first_y)
annual = Series(1, index=date_range('2014-01-01', periods=3, freq='YE-DEC'))
_, ax = mpl.pyplot.subplots()
annual.plot(ax=ax)
check_format_of_first_point(ax, 't = 2014  y = 1.000000')
daily = Series(1, index=date_range('2014-01-01', periods=3, freq='D'))
daily.plot(ax=ax)
check_format_of_first_point(ax, 't = 2014-01-01  y = 1.000000')
```

## Next Steps


---

*Source: test_datetimelike.py:176 | Complexity: Advanced | Last updated: 2026-06-02*