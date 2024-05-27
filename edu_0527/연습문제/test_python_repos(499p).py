# test_python_repos.py
# pytest 사용법
# pip install pytest
# 함수를 정의하고 test_를 붙인 테스트용 함수 생성
# test_ 함수에는 assert 함수()로 테스트할 함수 호출
# 터미널에 pytest 파일명 입력

import requests
def request(url, headers):
    r = requests.get(url, headers=headers)
    return r.status_code

def request_json(url, headers):
    r = requests.get(url, headers=headers)
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return len(repo_dicts)


# status_code 값이 200인지 단언하는 테스트 어서션
def test_repos():
    assert request("https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000", {"Accept": "application/vnd.github.v3+json"}) == 200

# 반환되는 항목이 40개인지 확인하는 테스트 어서션
def test_request_json():
    assert request_json("https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000", {"Accept": "application/vnd.github.v3+json"}) == 40
