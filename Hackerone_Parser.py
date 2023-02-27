import requests
import pandas as pd
from pandas import json_normalize
import json


endCursor="MjYwMA"
 
url = "https://hackerone.com:443/graphql"
cookies = {"h1_device_id": "a8fc56f9-790f-4089-ad57-2eb90ce35247", "_ga": "GA1.2.69509536.1639082405", "__Host-session": "UDBjQ3R4MEwremltTDEvYytMWnlFSnF2eEZJVTZ6QnUweDlKTEdYNHlNUXlwS2N4eFlVYlordUJzZVNuMmcrUTFJYm1sQS90WTlyWWFjZGZNWFBpRDRkSjZhTEp4MFpQRml5SFBvc2Z0cmdBSlVEMGVXWEFFY1l1N2dKeElvL205YlpCbHo3L1FGTHNSWjc1Q09rckNEeldtMkRZdDYvbk5CYitjYitYNVBaZ3VrUTdYTklucGxGTGhOQzZsOWFPNVRna0FTeUEwbXFpYllqN1oxRFMzNHV5dDZEY2QvODdFYW9YOElFRWE0Q0U3VEVtVjdaNktlU1FMQXE2Y3ozb0FybUV6c3dVeGJITE83TWRSSE5ibVMrTnVEampwSXV5ZWdOSktiNFF1VFU9LS1uTUVwNVppSFk3cmkvMnE3cUx3M2RnPT0%3D--3641e0b3bf61650c4f12d553db798b9efaa9d847"}
headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"", "Accept": "*/*", "X-Auth-Token": "----", "Content-Type": "application/json", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Sec-Ch-Ua-Platform": "\"macOS\"", "Origin": "https://hackerone.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://hackerone.com/hacktivity", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"}
jsonn={"operationName": "HacktivityPageQuery", "query": "query HacktivityPageQuery($querystring: String, $orderBy: HacktivityItemOrderInput, $secureOrderBy: FiltersHacktivityItemFilterOrder, $where: FiltersHacktivityItemFilterInput, $count: Int, $cursor: String, $maxShownVoters: Int) {\n  me {\n    id\n    __typename\n  }\n  hacktivity_items(first: $count, after: $cursor, query: $querystring, order_by: $orderBy, secure_order_by: $secureOrderBy, where: $where) {\n    total_count\n    ...HacktivityList\n    __typename\n  }\n}\n\nfragment HacktivityList on HacktivityItemConnection {\n  total_count\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  edges {\n    node {\n      ... on HacktivityItemInterface {\n        id\n        databaseId: _id\n        ...HacktivityItem\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment HacktivityItem on HacktivityItemUnion {\n  type: __typename\n  ... on HacktivityItemInterface {\n    id\n    votes {\n      total_count\n      __typename\n    }\n    voters: votes(last: $maxShownVoters) {\n      edges {\n        node {\n          id\n          user {\n            id\n            username\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    upvoted: upvoted_by_current_user\n    __typename\n  }\n  ... on Undisclosed {\n    id\n    ...HacktivityItemUndisclosed\n    __typename\n  }\n  ... on Disclosed {\n    id\n    ...HacktivityItemDisclosed\n    __typename\n  }\n  ... on HackerPublished {\n    id\n    ...HacktivityItemHackerPublished\n    __typename\n  }\n}\n\nfragment HacktivityItemUndisclosed on Undisclosed {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    id\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  latest_disclosable_action\n  latest_disclosable_activity_at\n  requires_view_privilege\n  total_awarded_amount\n  currency\n  __typename\n}\n\nfragment TeamLinkWithMiniProfile on Team {\n  id\n  handle\n  name\n  __typename\n}\n\nfragment UserLinkWithMiniProfile on User {\n  id\n  username\n  __typename\n}\n\nfragment HacktivityItemDisclosed on Disclosed {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    id\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  report {\n    id\n    databaseId: _id\n    title\n    substate\n    url\n    __typename\n  }\n  latest_disclosable_action\n  latest_disclosable_activity_at\n  total_awarded_amount\n  severity_rating\n  currency\n  __typename\n}\n\nfragment HacktivityItemHackerPublished on HackerPublished {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    id\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  report {\n    id\n    url\n    title\n    substate\n    __typename\n  }\n  latest_disclosable_activity_at\n  severity_rating\n  __typename\n}\n", "variables": {"count": 700, "cursor": endCursor, "maxShownVoters": 1, "orderBy": {"direction": "DESC", "field": "popular"}, "querystring": "", "secureOrderBy": None, "where": {"report": {"disclosed_at": {"_is_null": False}}}}}

response = requests.post(url, headers=headers, cookies=cookies, json=jsonn)

jsonresponse = response.text

data = json.loads(jsonresponse)

endCursor = data['data']['hacktivity_items']['pageInfo']['endCursor']

print("first cursor: " + endCursor)

while True:

	jsonn={"operationName": "HacktivityPageQuery", "query": "query HacktivityPageQuery($querystring: String, $orderBy: HacktivityItemOrderInput, $secureOrderBy: FiltersHacktivityItemFilterOrder, $where: FiltersHacktivityItemFilterInput, $count: Int, $cursor: String, $maxShownVoters: Int) {\n  me {\n    id\n    __typename\n  }\n  hacktivity_items(first: $count, after: $cursor, query: $querystring, order_by: $orderBy, secure_order_by: $secureOrderBy, where: $where) {\n    total_count\n    ...HacktivityList\n    __typename\n  }\n}\n\nfragment HacktivityList on HacktivityItemConnection {\n  total_count\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  edges {\n    node {\n      ... on HacktivityItemInterface {\n        id\n        databaseId: _id\n        ...HacktivityItem\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment HacktivityItem on HacktivityItemUnion {\n  type: __typename\n  ... on HacktivityItemInterface {\n    id\n    votes {\n      total_count\n      __typename\n    }\n    voters: votes(last: $maxShownVoters) {\n      edges {\n        node {\n          id\n          user {\n            id\n            username\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    upvoted: upvoted_by_current_user\n    __typename\n  }\n  ... on Undisclosed {\n    id\n    ...HacktivityItemUndisclosed\n    __typename\n  }\n  ... on Disclosed {\n    id\n    ...HacktivityItemDisclosed\n    __typename\n  }\n  ... on HackerPublished {\n    id\n    ...HacktivityItemHackerPublished\n    __typename\n  }\n}\n\nfragment HacktivityItemUndisclosed on Undisclosed {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    id\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  latest_disclosable_action\n  latest_disclosable_activity_at\n  requires_view_privilege\n  total_awarded_amount\n  currency\n  __typename\n}\n\nfragment TeamLinkWithMiniProfile on Team {\n  id\n  handle\n  name\n  __typename\n}\n\nfragment UserLinkWithMiniProfile on User {\n  id\n  username\n  __typename\n}\n\nfragment HacktivityItemDisclosed on Disclosed {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    id\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  report {\n    id\n    databaseId: _id\n    title\n    substate\n    url\n    __typename\n  }\n  latest_disclosable_action\n  latest_disclosable_activity_at\n  total_awarded_amount\n  severity_rating\n  currency\n  __typename\n}\n\nfragment HacktivityItemHackerPublished on HackerPublished {\n  id\n  reporter {\n    id\n    username\n    ...UserLinkWithMiniProfile\n    __typename\n  }\n  team {\n    id\n    handle\n    name\n    medium_profile_picture: profile_picture(size: medium)\n    url\n    ...TeamLinkWithMiniProfile\n    __typename\n  }\n  report {\n    id\n    url\n    title\n    substate\n    __typename\n  }\n  latest_disclosable_activity_at\n  severity_rating\n  __typename\n}\n", "variables": {"count": 700, "cursor": endCursor, "maxShownVoters": 1, "orderBy": {"direction": "DESC", "field": "popular"}, "querystring": "", "secureOrderBy": None, "where": {"report": {"disclosed_at": {"_is_null": False}}}}}

	response = requests.post(url, headers=headers, cookies=cookies, json=jsonn)

	jsonresponse = response.text

	data = json.loads(jsonresponse)

	for i in data["data"]["hacktivity_items"]["edges"]:
	
	
		print(i['node']['databaseId'], end=";" )
		
		try:
			print(i['node']['reporter']['username'], end=";")
		except:
			print("null" , end=";")

		try:
			print(i['node']['latest_disclosable_activity_at'], end=";")
		except:
			print("null" , end=";")

		try:
			print(i['node']['team']['handle'], end=";")
		except:
			print("null" , end=";")

		try:
			print(str(i['node']['votes']['total_count']), end=";")
		except:
			print("null" , end=";")

		try:
			print(i['node']['type'], end=";")
		except:
			print("null" , end=";")

		try:
			print(i['node']['currency'], end=";") 
		except:
			print("null" , end=";")

		try:
			print(str(i['node']['total_awarded_amount']) , end=";") 
		except:
			print("null" , end=";")

		try:
			print(i['node']['latest_disclosable_action'] , end=";") 
		except:
			print("null" , end=";")

		try:
			print(i['node']['report']['title'] , end=";")
		except:
			print("null" , end=";")

		try:
			print(i['node']['report']['substate'] , end=";")
		except:
			print("null" , end=";")

		try:
			print(i['node']['report']['url'] , end=";")
		except:
			print("null" , end=";")

		try:
			print(str(i['node']['requires_view_privilege']) , end=";")
		except:
			print("null" , end=";")
#finally:

		try:
			print(str(i['node']['severity_rating']) , end=";")
		except:
			print("null" , end=";")

		print('\n')



	endCursor = data['data']['hacktivity_items']['pageInfo']['endCursor']

df=pd.json_normalize(data, max_level=1)
df.to_csv('sonuc.csv')

response = requests.post(url, headers=headers, cookies=cookies, json=jsonn)





