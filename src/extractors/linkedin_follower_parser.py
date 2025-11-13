thondef parse_follower_count(page_content):
soup = BeautifulSoup(page_content, "html.parser")
follower_count = soup.find("span", class_="follower-count")
return int(follower_count.get_text()) if follower_count else 0