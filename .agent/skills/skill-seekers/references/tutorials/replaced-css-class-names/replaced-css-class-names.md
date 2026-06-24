# How To: Replaced Css Class Names

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replaced css class names

## Prerequisites

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`


## Step-by-Step Guide

### Step 1: Assign css = value

```python
css = {'row_heading': 'ROWHEAD', 'index_name': 'IDXNAME', 'row': 'ROW', 'row_trim': 'ROWTRIM', 'level': 'LEVEL', 'data': 'DATA', 'blank': 'BLANK'}
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign midx = MultiIndex.from_product(...)

```python
midx = MultiIndex.from_product([['a', 'b'], ['c', 'd']])
```

### Step 3: Assign styler_mi = Styler.set_table_styles(...)

```python
styler_mi = Styler(DataFrame(np.arange(16).reshape(4, 4), index=midx, columns=midx), uuid_len=0).set_table_styles(css_class_names=css)
```

### Step 4: Assign styler_mi.index.names = value

```python
styler_mi.index.names = ['n1', 'n2']
```

### Step 5: Call styler_mi.hide()

```python
styler_mi.hide(styler_mi.index[1:], axis=0)
```

### Step 6: Call styler_mi.hide()

```python
styler_mi.hide(styler_mi.columns[1:], axis=1)
```

### Step 7: Call styler_mi.map_index()

```python
styler_mi.map_index(lambda v: 'color: red;', axis=0)
```

### Step 8: Call styler_mi.map_index()

```python
styler_mi.map_index(lambda v: 'color: green;', axis=1)
```

### Step 9: Call styler_mi.map()

```python
styler_mi.map(lambda v: 'color: blue;')
```

### Step 10: Assign expected = dedent(...)

```python
expected = dedent('    <style type="text/css">\n    #T__ROW0_col0 {\n      color: blue;\n    }\n    #T__LEVEL0_ROW0, #T__LEVEL1_ROW0 {\n      color: red;\n    }\n    #T__LEVEL0_col0, #T__LEVEL1_col0 {\n      color: green;\n    }\n    </style>\n    <table id="T_">\n      <thead>\n        <tr>\n          <th class="BLANK" >&nbsp;</th>\n          <th class="IDXNAME LEVEL0" >n1</th>\n          <th id="T__LEVEL0_col0" class="col_heading LEVEL0 col0" >a</th>\n        </tr>\n        <tr>\n          <th class="BLANK" >&nbsp;</th>\n          <th class="IDXNAME LEVEL1" >n2</th>\n          <th id="T__LEVEL1_col0" class="col_heading LEVEL1 col0" >c</th>\n        </tr>\n        <tr>\n          <th class="IDXNAME LEVEL0" >n1</th>\n          <th class="IDXNAME LEVEL1" >n2</th>\n          <th class="BLANK col0" >&nbsp;</th>\n        </tr>\n      </thead>\n      <tbody>\n        <tr>\n          <th id="T__LEVEL0_ROW0" class="ROWHEAD LEVEL0 ROW0" >a</th>\n          <th id="T__LEVEL1_ROW0" class="ROWHEAD LEVEL1 ROW0" >c</th>\n          <td id="T__ROW0_col0" class="DATA ROW0 col0" >0</td>\n        </tr>\n      </tbody>\n    </table>\n    ')
```

### Step 11: Assign result = styler_mi.to_html(...)

```python
result = styler_mi.to_html()
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
css = {'row_heading': 'ROWHEAD', 'index_name': 'IDXNAME', 'row': 'ROW', 'row_trim': 'ROWTRIM', 'level': 'LEVEL', 'data': 'DATA', 'blank': 'BLANK'}
midx = MultiIndex.from_product([['a', 'b'], ['c', 'd']])
styler_mi = Styler(DataFrame(np.arange(16).reshape(4, 4), index=midx, columns=midx), uuid_len=0).set_table_styles(css_class_names=css)
styler_mi.index.names = ['n1', 'n2']
styler_mi.hide(styler_mi.index[1:], axis=0)
styler_mi.hide(styler_mi.columns[1:], axis=1)
styler_mi.map_index(lambda v: 'color: red;', axis=0)
styler_mi.map_index(lambda v: 'color: green;', axis=1)
styler_mi.map(lambda v: 'color: blue;')
expected = dedent('    <style type="text/css">\n    #T__ROW0_col0 {\n      color: blue;\n    }\n    #T__LEVEL0_ROW0, #T__LEVEL1_ROW0 {\n      color: red;\n    }\n    #T__LEVEL0_col0, #T__LEVEL1_col0 {\n      color: green;\n    }\n    </style>\n    <table id="T_">\n      <thead>\n        <tr>\n          <th class="BLANK" >&nbsp;</th>\n          <th class="IDXNAME LEVEL0" >n1</th>\n          <th id="T__LEVEL0_col0" class="col_heading LEVEL0 col0" >a</th>\n        </tr>\n        <tr>\n          <th class="BLANK" >&nbsp;</th>\n          <th class="IDXNAME LEVEL1" >n2</th>\n          <th id="T__LEVEL1_col0" class="col_heading LEVEL1 col0" >c</th>\n        </tr>\n        <tr>\n          <th class="IDXNAME LEVEL0" >n1</th>\n          <th class="IDXNAME LEVEL1" >n2</th>\n          <th class="BLANK col0" >&nbsp;</th>\n        </tr>\n      </thead>\n      <tbody>\n        <tr>\n          <th id="T__LEVEL0_ROW0" class="ROWHEAD LEVEL0 ROW0" >a</th>\n          <th id="T__LEVEL1_ROW0" class="ROWHEAD LEVEL1 ROW0" >c</th>\n          <td id="T__ROW0_col0" class="DATA ROW0 col0" >0</td>\n        </tr>\n      </tbody>\n    </table>\n    ')
result = styler_mi.to_html()
assert result == expected
```

## Next Steps


---

*Source: test_html.py:477 | Complexity: Advanced | Last updated: 2026-06-02*