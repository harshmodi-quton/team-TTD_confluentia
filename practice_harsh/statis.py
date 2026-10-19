TEXT= "Reinforcement learning is learning by trial and error. An agent tries actions in an environment, gets rewarded for good outcomes, and gradually learns what works. The agent follows a policy; the environment has a state."
from collections import Counter
import json
def word_stats(text):
    lst = [w.strip(",.;") for w in text.lower().split()]
    c = Counter(lst)
    c2 ={}
    for w in lst:
        if len(w) not in c2: 
            c2[len(w)]=[]
        c2[len(w)].append(w)

    report={
        "total_words": sum(c.values()),
        "distinct_words": len(c.keys()),
        "top_5" : c.most_common(5),
        "longest": c2[max(c2.keys())],
        "avg_length":  sum(c2.keys())/len(c.keys())

    }
    with open("report.json", "w" ) as f:
        json.dump(report, f, indent=2)
    with open("report.json" ) as g:
        te= json.load(g)
    print(te)

word_stats(TEXT)