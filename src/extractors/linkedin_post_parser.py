thondef parse_post(post_element):
post_data = {
"postContent": post_element.get_text(),
"author": post_element.find("span", class_="author").get_text() if post_element.find("span", class_="author") else "Unknown",
"publicationDate": post_element.find("span", class_="date").get_text() if post_element.find("span", class_="date") else "Unknown",
"likes": int(post_element.find("span", class_="likes").get_text() if post_element.find("span", class_="likes") else 0),
"comments": int(post_element.find("span", class_="comments").get_text() if post_element.find("span", class_="comments") else 0),
"shares": int(post_element.find("span", class_="shares").get_text() if post_element.find("span", class_="shares") else 0),
}
return post_data