# How To: Euro Decimal Format

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test euro decimal format

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'Id;Number1;Number2;Text1;Text2;Number3\n1;1521,1541;187101,9543;ABC;poi;4,738797819\n2;121,12;14897,76;DEF;uyt;0,377320872\n3;878,158;108013,434;GHI;rez;2,735694704'

```python
data = 'Id;Number1;Number2;Text1;Text2;Number3\n1;1521,1541;187101,9543;ABC;poi;4,738797819\n2;121,12;14897,76;DEF;uyt;0,377320872\n3;878,158;108013,434;GHI;rez;2,735694704'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), sep=';', decimal=',')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1521.1541, 187101.9543, 'ABC', 'poi', 4.738797819], [2, 121.12, 14897.76, 'DEF', 'uyt', 0.377320872], [3, 878.158, 108013.434, 'GHI', 'rez', 2.735694704]], columns=['Id', 'Number1', 'Number2', 'Text1', 'Text2', 'Number3'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'Id;Number1;Number2;Text1;Text2;Number3\n1;1521,1541;187101,9543;ABC;poi;4,738797819\n2;121,12;14897,76;DEF;uyt;0,377320872\n3;878,158;108013,434;GHI;rez;2,735694704'
result = parser.read_csv(StringIO(data), sep=';', decimal=',')
expected = DataFrame([[1, 1521.1541, 187101.9543, 'ABC', 'poi', 4.738797819], [2, 121.12, 14897.76, 'DEF', 'uyt', 0.377320872], [3, 878.158, 108013.434, 'GHI', 'rez', 2.735694704]], columns=['Id', 'Number1', 'Number2', 'Text1', 'Text2', 'Number3'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_decimal.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*