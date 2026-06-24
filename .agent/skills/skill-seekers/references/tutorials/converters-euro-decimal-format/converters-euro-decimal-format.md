# How To: Converters Euro Decimal Format

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test converters euro decimal format

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `dateutil.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign converters = value

```python
converters = {}
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign data = 'Id;Number1;Number2;Text1;Text2;Number3\n1;1521,1541;187101,9543;ABC;poi;4,7387\n2;121,12;14897,76;DEF;uyt;0,3773\n3;878,158;108013,434;GHI;rez;2,7356'

```python
data = 'Id;Number1;Number2;Text1;Text2;Number3\n1;1521,1541;187101,9543;ABC;poi;4,7387\n2;121,12;14897,76;DEF;uyt;0,3773\n3;878,158;108013,434;GHI;rez;2,7356'
```

### Step 4: Assign unknown, unknown, unknown = value

```python
converters['Number1'] = converters['Number2'] = converters['Number3'] = lambda x: float(x.replace(',', '.'))
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), sep=';', converters=converters)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1521.1541, 187101.9543, 'ABC', 'poi', 4.7387], [2, 121.12, 14897.76, 'DEF', 'uyt', 0.3773], [3, 878.158, 108013.434, 'GHI', 'rez', 2.7356]], columns=['Id', 'Number1', 'Number2', 'Text1', 'Text2', 'Number3'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign msg = "The 'converters' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'converters' option is not supported with the 'pyarrow' engine"
```

### Step 9: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), sep=';', converters=converters)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
converters = {}
parser = all_parsers
data = 'Id;Number1;Number2;Text1;Text2;Number3\n1;1521,1541;187101,9543;ABC;poi;4,7387\n2;121,12;14897,76;DEF;uyt;0,3773\n3;878,158;108013,434;GHI;rez;2,7356'
converters['Number1'] = converters['Number2'] = converters['Number3'] = lambda x: float(x.replace(',', '.'))
if parser.engine == 'pyarrow':
    msg = "The 'converters' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), sep=';', converters=converters)
    return
result = parser.read_csv(StringIO(data), sep=';', converters=converters)
expected = DataFrame([[1, 1521.1541, 187101.9543, 'ABC', 'poi', 4.7387], [2, 121.12, 14897.76, 'DEF', 'uyt', 0.3773], [3, 878.158, 108013.434, 'GHI', 'rez', 2.7356]], columns=['Id', 'Number1', 'Number2', 'Text1', 'Text2', 'Number3'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_converters.py:78 | Complexity: Advanced | Last updated: 2026-06-02*