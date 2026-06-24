# How To: Davis Birank

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: test davis birank

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign answer = value

```python
answer = {'Laura Mandeville': 0.07, 'Olivia Carleton': 0.04, 'Frances Anderson': 0.05, 'Pearl Oglethorpe': 0.04, 'Katherina Rogers': 0.06, 'Flora Price': 0.04, 'Dorothy Murchison': 0.04, 'Helen Lloyd': 0.06, 'Theresa Anderson': 0.07, 'Eleanor Nye': 0.05, 'Evelyn Jefferson': 0.07, 'Sylvia Avondale': 0.07, 'Charlotte McDowd': 0.05, 'Verne Sanderson': 0.05, 'Myra Liddel': 0.05, 'Brenda Rogers': 0.07, 'Ruth DeSand': 0.05, 'Nora Fayette': 0.07, 'E8': 0.11, 'E7': 0.09, 'E10': 0.07, 'E9': 0.1, 'E13': 0.05, 'E3': 0.07, 'E12': 0.07, 'E11': 0.06, 'E2': 0.05, 'E5': 0.08, 'E6': 0.08, 'E14': 0.05, 'E4': 0.06, 'E1': 0.05}
```


## Complete Example

```python
# Workflow
answer = {'Laura Mandeville': 0.07, 'Olivia Carleton': 0.04, 'Frances Anderson': 0.05, 'Pearl Oglethorpe': 0.04, 'Katherina Rogers': 0.06, 'Flora Price': 0.04, 'Dorothy Murchison': 0.04, 'Helen Lloyd': 0.06, 'Theresa Anderson': 0.07, 'Eleanor Nye': 0.05, 'Evelyn Jefferson': 0.07, 'Sylvia Avondale': 0.07, 'Charlotte McDowd': 0.05, 'Verne Sanderson': 0.05, 'Myra Liddel': 0.05, 'Brenda Rogers': 0.07, 'Ruth DeSand': 0.05, 'Nora Fayette': 0.07, 'E8': 0.11, 'E7': 0.09, 'E10': 0.07, 'E9': 0.1, 'E13': 0.05, 'E3': 0.07, 'E12': 0.07, 'E11': 0.06, 'E2': 0.05, 'E5': 0.08, 'E6': 0.08, 'E14': 0.05, 'E4': 0.06, 'E1': 0.05}
```

## Next Steps


---

*Source: test_link_analysis.py:76 | Complexity: Beginner | Last updated: 2026-06-02*