rss_url = "https://animixplay.to/rss.xml"
features = "xml"


# def parse_soup(self):
#     soup = self.get_soup()
#     articles = soup.findAll("item")
#     for a in articles:
#         title = a.find("title").text
#         link = a.find("link").text
#         ep = a.find("ep").text
#         pub_date = a.find("pubDate").text
#         published = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
#         article = {
#             "title": title,
#             "link": link,
#             "published": published,
#             "ep": ep,
#         }
#         article_list.append(article)
#     return articles


# articles = WebScrapping(rss_url, features).parse_soup()

# title = "Management of a Novice Alchemist"
# arr = [
#     " ".join(x["title"].split()[:-2])
#     for x in articles
#     if search(title, " ".join(x["title"].split()[:-2]))
# ]
