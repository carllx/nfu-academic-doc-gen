# How To: Collaborative Filtering Birank

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test collaborative filtering birank

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign elist = value

```python
elist = [('u1', 'p1', 5), ('u2', 'p1', 5), ('u2', 'p2', 4), ('u3', 'p1', 3), ('u3', 'p3', 2)]
```

**Verification:**
```python
assert u1_birank_results['p2'] > u1_birank_results['p3']
```

### Step 2: Assign item_recommendation_graph = nx.DiGraph(...)

```python
item_recommendation_graph = nx.DiGraph()
```

**Verification:**
```python
assert u1_birank_results_unweighted['p2'] == pytest.approx(u1_birank_results_unweighted['p3'], rel=2e-06)
```

### Step 3: Call item_recommendation_graph.add_weighted_edges_from()

```python
item_recommendation_graph.add_weighted_edges_from(elist, weight='rating')
```

### Step 4: Assign product_nodes = value

```python
product_nodes = ('p1', 'p2', 'p3')
```

### Step 5: Assign u1_query = value

```python
u1_query = {product: rating for _, product, rating in item_recommendation_graph.edges(nbunch='u1', data='rating')}
```

### Step 6: Assign u1_birank_results = bipartite.birank(...)

```python
u1_birank_results = bipartite.birank(item_recommendation_graph, product_nodes, alpha=0.8, beta=1.0, top_personalization=u1_query, weight='rating')
```

**Verification:**
```python
assert u1_birank_results['p2'] > u1_birank_results['p3']
```

### Step 7: Assign u1_birank_results_unweighted = bipartite.birank(...)

```python
u1_birank_results_unweighted = bipartite.birank(item_recommendation_graph, product_nodes, alpha=0.8, beta=1.0, top_personalization=u1_query, weight=None)
```

**Verification:**
```python
assert u1_birank_results_unweighted['p2'] == pytest.approx(u1_birank_results_unweighted['p3'], rel=2e-06)
```


## Complete Example

```python
# Workflow
elist = [('u1', 'p1', 5), ('u2', 'p1', 5), ('u2', 'p2', 4), ('u3', 'p1', 3), ('u3', 'p3', 2)]
item_recommendation_graph = nx.DiGraph()
item_recommendation_graph.add_weighted_edges_from(elist, weight='rating')
product_nodes = ('p1', 'p2', 'p3')
u1_query = {product: rating for _, product, rating in item_recommendation_graph.edges(nbunch='u1', data='rating')}
u1_birank_results = bipartite.birank(item_recommendation_graph, product_nodes, alpha=0.8, beta=1.0, top_personalization=u1_query, weight='rating')
assert u1_birank_results['p2'] > u1_birank_results['p3']
u1_birank_results_unweighted = bipartite.birank(item_recommendation_graph, product_nodes, alpha=0.8, beta=1.0, top_personalization=u1_query, weight=None)
assert u1_birank_results_unweighted['p2'] == pytest.approx(u1_birank_results_unweighted['p3'], rel=2e-06)
```

## Next Steps


---

*Source: test_link_analysis.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*