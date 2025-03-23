class User:
    def __init__(self, email_adress, name, password, current_job_title) -> None:
        self.email = email_adress
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password
    
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
    
    def get_user_info(self):
        print(f"---\nUsername: {self.name}\nE-Mail: {self.email}\nJob Title: {self.current_job_title}")