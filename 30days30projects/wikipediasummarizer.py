import wikipedia

def summarize(topic):
    try:
        summary = wikipedia.summary(topic, sentences=3)
        print(f"\n Summary of '{topic}':\n")
        print(summary)

    except Exception as e:
        print("\n An unexpected error occurred:", e)

if __name__ == "__main__":
    print(" Wikipedia Article Summarizer")
    topic = input("Topic: ")
    summarize(topic)
