# Day 39 — Personal Search Engine

Search engines always felt like black box magic to me.
Today I built a tiny one from scratch that demonstrates the real logic behind keyword matching, relevance scoring and documentation ranking and now they feel a lot less magical in a good way.

---

## The core idea

You index the documents (title + content), then search across them using a query. the engine splits your query into individual words, counts how many times each word appears in every document, and uses that count as a relevance score. higher the score = better match. And the results come back sorted.

It's a stripped-down version of what real search systems do.

---

## the part that actually made me think

```python
query_words = query.split()

for word in query_words:
    score += document["content"].count(word)
```

this is term frequency means how often a search term appears in a document. It's one of the foundational ideas behind information retrieval systems. I didn't know that's what it was called until after I wrote it.

then sorting by score:

```python
results.sort(key=lambda item: item["score"], reverse=True)
```

`lambda` here is just a quick inline function that tells `.sort()` what to sort by. used this concept in Day 36 too with `max()`

---

## what this connects to in the real world

real search engines even Google at its earliest started with term frequency logic. the more times a word appears in a document, the more relevant that document is to a query containing that word.

modern systems add a lot like TF-IDF, PageRank, semantic understanding but the base idea is the same loop I wrote today. relevance scoring is information retrieval, and information retrieval is literally what search is.

---

## how the ranking works

| document | query words found | relevance score |
|---|---|---|
| doc with 4 matches | 4 | 4 |
| doc with 1 match | 1 | 1 |
| doc with 0 matches | 0 | not shown |

zero-score documents don't appear in results at all, this is the same behavior as a real search engine.

---

*day 39  Built a search engine. Small one, but the logic is inspired by the way real search systems work.*
