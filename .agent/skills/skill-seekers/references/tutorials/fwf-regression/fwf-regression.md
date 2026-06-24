# How To: Fwf Regression

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fwf regression

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.parsers`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign tz_list = value

```python
tz_list = [1, 10, 20, 30, 60, 80, 100]
```

### Step 2: Assign widths = value

```python
widths = [16] + [8] * len(tz_list)
```

### Step 3: Assign names = value

```python
names = ['SST'] + [f'T{z:03d}' for z in tz_list[1:]]
```

### Step 4: Assign data = '  2009164202000   9.5403  9.4105  8.6571  7.8372  6.0612  5.8843  5.5192\n2009164203000   9.5435  9.2010  8.6167  7.8176  6.0804  5.8728  5.4869\n2009164204000   9.5873  9.1326  8.4694  7.5889  6.0422  5.8526  5.4657\n2009164205000   9.5810  9.0896  8.4009  7.4652  6.0322  5.8189  5.4379\n2009164210000   9.6034  9.0897  8.3822  7.4905  6.0908  5.7904  5.4039\n'

```python
data = '  2009164202000   9.5403  9.4105  8.6571  7.8372  6.0612  5.8843  5.5192\n2009164203000   9.5435  9.2010  8.6167  7.8176  6.0804  5.8728  5.4869\n2009164204000   9.5873  9.1326  8.4694  7.5889  6.0422  5.8526  5.4657\n2009164205000   9.5810  9.0896  8.4009  7.4652  6.0322  5.8189  5.4379\n2009164210000   9.6034  9.0897  8.3822  7.4905  6.0908  5.7904  5.4039\n'
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[9.5403, 9.4105, 8.6571, 7.8372, 6.0612, 5.8843, 5.5192], [9.5435, 9.201, 8.6167, 7.8176, 6.0804, 5.8728, 5.4869], [9.5873, 9.1326, 8.4694, 7.5889, 6.0422, 5.8526, 5.4657], [9.581, 9.0896, 8.4009, 7.4652, 6.0322, 5.8189, 5.4379], [9.6034, 9.0897, 8.3822, 7.4905, 6.0908, 5.7904, 5.4039]], index=DatetimeIndex(['2009-06-13 20:20:00', '2009-06-13 20:30:00', '2009-06-13 20:40:00', '2009-06-13 20:50:00', '2009-06-13 21:00:00']), columns=['SST', 'T010', 'T020', 'T030', 'T060', 'T080', 'T100'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(data), index_col=0, header=None, names=names, widths=widths, parse_dates=True, date_format='%Y%j%H%M%S')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(data), index_col=0, header=None, names=names, widths=widths, parse_dates=True, date_parser=lambda s: datetime.strptime(s, '%Y%j%H%M%S'))
```


## Complete Example

```python
# Workflow
tz_list = [1, 10, 20, 30, 60, 80, 100]
widths = [16] + [8] * len(tz_list)
names = ['SST'] + [f'T{z:03d}' for z in tz_list[1:]]
data = '  2009164202000   9.5403  9.4105  8.6571  7.8372  6.0612  5.8843  5.5192\n2009164203000   9.5435  9.2010  8.6167  7.8176  6.0804  5.8728  5.4869\n2009164204000   9.5873  9.1326  8.4694  7.5889  6.0422  5.8526  5.4657\n2009164205000   9.5810  9.0896  8.4009  7.4652  6.0322  5.8189  5.4379\n2009164210000   9.6034  9.0897  8.3822  7.4905  6.0908  5.7904  5.4039\n'
with tm.assert_produces_warning(FutureWarning, match="use 'date_format' instead"):
    result = read_fwf(StringIO(data), index_col=0, header=None, names=names, widths=widths, parse_dates=True, date_parser=lambda s: datetime.strptime(s, '%Y%j%H%M%S'))
expected = DataFrame([[9.5403, 9.4105, 8.6571, 7.8372, 6.0612, 5.8843, 5.5192], [9.5435, 9.201, 8.6167, 7.8176, 6.0804, 5.8728, 5.4869], [9.5873, 9.1326, 8.4694, 7.5889, 6.0422, 5.8526, 5.4657], [9.581, 9.0896, 8.4009, 7.4652, 6.0322, 5.8189, 5.4379], [9.6034, 9.0897, 8.3822, 7.4905, 6.0908, 5.7904, 5.4039]], index=DatetimeIndex(['2009-06-13 20:20:00', '2009-06-13 20:30:00', '2009-06-13 20:40:00', '2009-06-13 20:50:00', '2009-06-13 21:00:00']), columns=['SST', 'T010', 'T020', 'T030', 'T060', 'T080', 'T100'])
tm.assert_frame_equal(result, expected)
result = read_fwf(StringIO(data), index_col=0, header=None, names=names, widths=widths, parse_dates=True, date_format='%Y%j%H%M%S')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read_fwf.py:269 | Complexity: Advanced | Last updated: 2026-06-02*