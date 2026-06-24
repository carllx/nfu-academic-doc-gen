# How To: Davis Birank With Personalization

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: test davis birank with personalization

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign answer = value

```python
answer = {'Laura Mandeville': 0.29, 'Olivia Carleton': 0.02, 'Frances Anderson': 0.06, 'Pearl Oglethorpe': 0.04, 'Katherina Rogers': 0.04, 'Flora Price': 0.02, 'Dorothy Murchison': 0.03, 'Helen Lloyd': 0.04, 'Theresa Anderson': 0.08, 'Eleanor Nye': 0.05, 'Evelyn Jefferson': 0.09, 'Sylvia Avondale': 0.05, 'Charlotte McDowd': 0.06, 'Verne Sanderson': 0.04, 'Myra Liddel': 0.03, 'Brenda Rogers': 0.08, 'Ruth DeSand': 0.05, 'Nora Fayette': 0.05, 'E8': 0.11, 'E7': 0.1, 'E10': 0.04, 'E9': 0.07, 'E13': 0.03, 'E3': 0.11, 'E12': 0.04, 'E11': 0.03, 'E2': 0.1, 'E5': 0.11, 'E6': 0.1, 'E14': 0.03, 'E4': 0.06, 'E1': 0.1}
```


## Complete Example

```python
# Workflow
answer = {'Laura Mandeville': 0.29, 'Olivia Carleton': 0.02, 'Frances Anderson': 0.06, 'Pearl Oglethorpe': 0.04, 'Katherina Rogers': 0.04, 'Flora Price': 0.02, 'Dorothy Murchison': 0.03, 'Helen Lloyd': 0.04, 'Theresa Anderson': 0.08, 'Eleanor Nye': 0.05, 'Evelyn Jefferson': 0.09, 'Sylvia Avondale': 0.05, 'Charlotte McDowd': 0.06, 'Verne Sanderson': 0.04, 'Myra Liddel': 0.03, 'Brenda Rogers': 0.08, 'Ruth DeSand': 0.05, 'Nora Fayette': 0.05, 'E8': 0.11, 'E7': 0.1, 'E10': 0.04, 'E9': 0.07, 'E13': 0.03, 'E3': 0.11, 'E12': 0.04, 'E11': 0.03, 'E2': 0.1, 'E5': 0.11, 'E6': 0.1, 'E14': 0.03, 'E4': 0.06, 'E1': 0.1}
```

## Next Steps


---

*Source: test_link_analysis.py:121 | Complexity: Beginner | Last updated: 2026-06-02*