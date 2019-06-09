import requests
import json
import os

list_of_pull_requests = []


def get_pull_requests(username, repository):
    github_url = "https://api.github.com"
    r = requests.get(os.path.join(github_url, "repos", repository, "pulls"))
    js = json.loads(r.content)
    for pull in js:
        if username == pull['user']['login']:
            if 'title' in pull.keys():
                list_of_pull_requests.append(pull['title'])
    print(list_of_pull_requests)


def get_contributions(username, repository):
    github_url = "https://api.github.com"
    r = requests.get(os.path.join(github_url, "repos", repository, "contributors"))
    js = json.loads(r.content)
    for contributor in js:
        if username == contributor['login']:
            if 'contributions' in contributor.keys():
                number_of_commits = contributor['contributions']
                return "Total commits by {name}: {number}".format(name=username,
                                                                  number=number_of_commits)

