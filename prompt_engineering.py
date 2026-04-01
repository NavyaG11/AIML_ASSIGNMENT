tasks = {
    "Resume": {
        "weak": "Write a resume",
        "strong": "Write a professional resume for a computer science student with skills in Python, ML, and projects."
    },
    "Business Idea": {
        "weak": "Give business idea",
        "strong": "Suggest a low-investment tech-based business idea suitable for college students in India."
    },
    "Study Plan": {
        "weak": "Make study plan",
        "strong": "Create a 4-week study plan to learn Python for beginners with daily tasks."
    }
}

for task, prompts in tasks.items():
    print(f"\nTask: {task}")
    print("Weak Prompt:", prompts["weak"])
    print("Strong Prompt:", prompts["strong"])
    print("\nWhy Strong is Better: More specific, clear, and goal-oriented.\n")