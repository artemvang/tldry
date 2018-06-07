# TLDRy!

[![PyPI version](https://badge.fury.io/py/p2tg.svg)](https://badge.fury.io/py/p2tg)

Lightweight and fast library for automatic summary extraction from russian and english texts.

# Installation

```bash
pip install tldry
```
or directly from reposiroty:
```bash
pip install git+https://github.com/vangaa/tldry
```

# Usage

Let's try to summarize Matrix synopsis:

```python
from tldry import TLDRy
import requests

summarizer = TLDRy(
    language='english', # russian and english are available
    min_sent_len=2, # minimal sentence size
    min_df=2, # minimal sentence frequency (like docuemnt frequency in TF-IDF)
)

text = requests.get('https://paste.in.ua/3404/raw/').text

print('\n$$$\n'.join(summarizer.summarize(text, topn=3)))
```
#### Result:
```
Morpheus tries to guide Neo out of the building but when he is instructed to get on a scaffolding and take it to the roof Neo rejects Morpheus's advice, allowing himself to be taken by the Agents.
$$$
Morpheus explains that he's been searching for Neo his entire life and asks if Neo feels like "Alice in Wonderland, falling down the rabbit hole." He explains to Neo that they exist in the Matrix, a false reality that has been constructed for humans to hide the truth.
$$$
Morpheus and Tank are amazed at Neo's ability to ingest information, but Morpheus wants to test Neo.
$$$
Cypher offers Neo a drink and says that he knows what Neo is thinking, "Why, oh why didn't I take the blue pill?" Neo laughs but is unsettled.
$$$
Morpheus, who is above Neo in the walls, breaks through the wall and lands on the agent, yelling to Trinity to get Neo out of the building.
```
