from fastapi import FastAPI, HTTPException

app = FastAPI()



text_posts = {
    1: {
        "title": "Getting Started with Python",
        "content": "Python is a versatile programming language that is easy to learn and widely used in web development, data science, and automation."
    },
    2: {
        "title": "Understanding Frontend Development",
        "content": "Frontend development focuses on building user interfaces using HTML, CSS, and JavaScript to create engaging user experiences."
    },
    3: {
        "title": "Why Clean Code Matters",
        "content": "Writing clean and readable code makes maintenance easier and helps teams collaborate more effectively over time."
    },
    4: {
        "title": "Tips for Learning Programming Faster",
        "content": "Consistent practice, building small projects, and reading other people’s code can significantly speed up the learning process."
    },
    5: {
        "title": "Introduction to REST APIs",
        "content": "REST APIs allow different systems to communicate with each other over HTTP using standard request methods."
    },
    6: {
        "title": "Common Mistakes New Developers Make",
        "content": "New developers often rush through concepts instead of understanding fundamentals, which can slow progress later."
    },
    7: {
        "title": "The Importance of Version Control",
        "content": "Version control systems like Git help track changes, manage collaboration, and prevent code loss."
    },
    8: {
        "title": "How to Stay Motivated While Coding",
        "content": "Setting small goals and celebrating progress can help maintain motivation during long coding sessions."
    },
    9: {
        "title": "Debugging Techniques That Work",
        "content": "Effective debugging involves understanding the problem, checking logs, and testing small changes step by step."
    },
    10: {
        "title": "Building Real-World Projects",
        "content": "Creating real-world projects helps reinforce concepts and builds a strong portfolio for job opportunities."
    }
}



@app.get("/get-all-posts")
def get_all_posts(limit : int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/get-post/{id}")
def get_post(id: int):

    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found.")
    return text_posts.get(id)