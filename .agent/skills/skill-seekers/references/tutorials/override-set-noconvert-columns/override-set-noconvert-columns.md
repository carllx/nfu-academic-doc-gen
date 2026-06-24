# How To: Override Set Noconvert Columns

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test override set noconvert columns

## Prerequisites

**Required Modules:**
- `datetime`
- `inspect`
- `io`
- `os`
- `pathlib`
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`


## Step-by-Step Guide

### Step 1: Assign data = 'a,b,c,d,e\n0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'

```python
data = 'a,b,c,d,e\n0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'
```

### Step 2: Assign parse_dates = value

```python
parse_dates = [[1, 2]]
```

### Step 3: Assign cols = value

```python
cols = {'a': [0, 0], 'c_d': [Timestamp('2014-01-01 09:00:00'), Timestamp('2014-01-02 10:00:00')]}
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(cols, columns=['c_d', 'a'])
```

### Step 5: Assign parser = MyTextFileReader(...)

```python
parser = MyTextFileReader()
```

### Step 6: Assign parser.options = value

```python
parser.options = {'usecols': [0, 2, 3], 'parse_dates': parse_dates, 'delimiter': ','}
```

### Step 7: Assign parser.engine = 'c'

```python
parser.engine = 'c'
```

### Step 8: Assign parser._engine = MyCParserWrapper(...)

```python
parser._engine = MyCParserWrapper(StringIO(data), **parser.options)
```

### Step 9: Assign result = parser.read(...)

```python
result = parser.read()
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign self._currow = 0

```python
self._currow = 0
```

### Step 12: Assign self.squeeze = False

```python
self.squeeze = False
```

### Step 13: Assign self.usecols = list(...)

```python
self.usecols = list(self.usecols)
```

### Step 14: Call self.usecols.reverse()

```python
self.usecols.reverse()
```


## Complete Example

```python
# Workflow
class MyTextFileReader(TextFileReader):

    def __init__(self) -> None:
        self._currow = 0
        self.squeeze = False

class MyCParserWrapper(CParserWrapper):

    def _set_noconvert_columns(self):
        if self.usecols_dtype == 'integer':
            self.usecols = list(self.usecols)
            self.usecols.reverse()
        return CParserWrapper._set_noconvert_columns(self)
data = 'a,b,c,d,e\n0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'
parse_dates = [[1, 2]]
cols = {'a': [0, 0], 'c_d': [Timestamp('2014-01-01 09:00:00'), Timestamp('2014-01-02 10:00:00')]}
expected = DataFrame(cols, columns=['c_d', 'a'])
parser = MyTextFileReader()
parser.options = {'usecols': [0, 2, 3], 'parse_dates': parse_dates, 'delimiter': ','}
parser.engine = 'c'
parser._engine = MyCParserWrapper(StringIO(data), **parser.options)
result = parser.read()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common_basic.py:43 | Complexity: Advanced | Last updated: 2026-06-02*