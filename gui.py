import tkinter as tk
from tkinter import scrolledtext
from search import search_topic
from summarizer import summarize

# Main Window
root = tk.Tk()
root.title("AI Research Assistant")
root.geometry("800x600")

# Heading
title_label = tk.Label(
    root,
    text="AI Research Assistant",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

# Input Box
topic_entry = tk.Entry(root, width=60, font=("Arial", 14))
topic_entry.pack(pady=10)

# Output Area
output_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=90,
    height=25,
    font=("Arial", 11)
)
output_area.pack(pady=10)

# Search Function
def start_research():

    topic = topic_entry.get()

    if topic.strip() == "":
        output_area.insert(tk.END, "Please enter a topic.\n")
        return

    output_area.delete(1.0, tk.END)
    output_area.insert(tk.END, "Researching...\n\n")

    try:
        results = search_topic(topic)

        output_area.insert(tk.END, "Top Sources:\n\n")

        for i, r in enumerate(results, start=1):
            output_area.insert(
                tk.END,
                f"{i}. {r['title']}\n{r['url']}\n\n"
            )

        summary = summarize(results, topic)

        output_area.insert(
            tk.END,
            "\n=== AI SUMMARY ===\n\n"
        )

        output_area.insert(tk.END, summary)

    except Exception as e:
        output_area.insert(tk.END, f"\nError:\n{e}")

# Search Button
search_button = tk.Button(
    root,
    text="Research",
    command=start_research,
    font=("Arial", 12),
    bg="blue",
    fg="white"
)
search_button.pack(pady=10)

# Run App
root.mainloop()