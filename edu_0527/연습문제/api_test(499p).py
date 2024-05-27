import requests
import plotly.express as px
import matplotlib.pyplot as plt


# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts, repo_names = [], [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_names.append(repo_name)
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(repo_names, stars, color='blue')
ax.set_title(title, fontsize=24)
ax.set_xlabel("repo links",fontsize=8)
ax.set_ylabel("stars",fontsize=16)
ax.tick_params(axis='x', labelrotation=90)
plt.show()

# fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
#         hover_name=hover_texts)
# fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
#         yaxis_title_font_size=20)
# fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
# fig.show()