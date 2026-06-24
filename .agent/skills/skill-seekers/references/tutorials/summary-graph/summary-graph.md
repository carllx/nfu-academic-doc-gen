# How To: Summary Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test summary graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign original_graph = self.build_original_graph(...)

```python
original_graph = self.build_original_graph()
```

**Verification:**
```python
assert nx.is_isomorphic(summary_graph, relabeled_summary_graph)
```

### Step 2: Assign summary_graph = self.build_summary_graph(...)

```python
summary_graph = self.build_summary_graph()
```

### Step 3: Assign relationship_attributes = value

```python
relationship_attributes = ('type',)
```

### Step 4: Assign generated_summary_graph = nx.snap_aggregation(...)

```python
generated_summary_graph = nx.snap_aggregation(original_graph, self.node_attributes)
```

### Step 5: Assign relabeled_summary_graph = self.deterministic_labels(...)

```python
relabeled_summary_graph = self.deterministic_labels(generated_summary_graph)
```

**Verification:**
```python
assert nx.is_isomorphic(summary_graph, relabeled_summary_graph)
```


## Complete Example

```python
# Workflow
original_graph = self.build_original_graph()
summary_graph = self.build_summary_graph()
relationship_attributes = ('type',)
generated_summary_graph = nx.snap_aggregation(original_graph, self.node_attributes)
relabeled_summary_graph = self.deterministic_labels(generated_summary_graph)
assert nx.is_isomorphic(summary_graph, relabeled_summary_graph)
```

## Next Steps


---

*Source: test_summarization.py:268 | Complexity: Intermediate | Last updated: 2026-06-02*