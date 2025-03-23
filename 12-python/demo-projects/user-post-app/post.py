class Post:
    def __init__(self, author, message) -> None:
        self.author = author
        self.message = message
    
    def get_post_info(self):
        print(f"---\nPost: \"{self.message}\" written by {self.author}.\n")