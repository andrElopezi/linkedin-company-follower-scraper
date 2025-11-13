thonimport requests
from bs4 import BeautifulSoup
import json

class LinkedInScraper:
    def __init__(self, company_url):
        self.company_url = company_url

    def get_page(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(self.company_url, headers=headers)
        return response.text if response.status_code == 200 else None

    def extract_post_content(self, page_content):
        soup = BeautifulSoup(page_content, "html.parser")
        posts = []
        for post in soup.find_all("div", class_="post-content"):
            post_data = {
                "postContent": post.get_text(),
                "author": post.find("span", class_="author").get_text() if post.find("span", class_="author") else "Unknown",
                "publicationDate": post.find("span", class_="date").get_text() if post.find("span", class_="date") else "Unknown",
                "likes": int(post.find("span", class_="likes").get_text() if post.find("span", class_="likes") else 0),
                "comments": int(post.find("span", class_="comments").get_text() if post.find("span", class_="comments") else 0),
                "shares": int(post.find("span", class_="shares").get_text() if post.find("span", class_="shares") else 0),
            }
            posts.append(post_data)
        return posts

    def get_follower_count(self, page_content):
        soup = BeautifulSoup(page_content, "html.parser")
        follower_count = soup.find("span", class_="follower-count")
        return int(follower_count.get_text()) if follower_count else 0

    def scrape(self):
        page_content = self.get_page()
        if page_content:
            posts = self.extract_post_content(page_content)
            followers = self.get_follower_count(page_content)
            return {
                "companyUrl": self.company_url,
                "companyName": self.company_url.split("/")[-1],  # Assuming company name is part of the URL
                "followers": followers,
                "posts": posts
            }
        return None