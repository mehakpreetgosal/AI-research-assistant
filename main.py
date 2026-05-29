from search import search_topic
from summarizer import summarize

topic = input("Enter research topic: ")

results = search_topic(topic)

print("\nTop Sources:\n")

for i, r in enumerate(results, start=1):
    print(f"{i}. {r['title']}")
    print(r['url'])
    print()

summary = summarize(results, topic)

print("\n===== AI Research Report =====\n")
print(summary)