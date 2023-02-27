
import json
import pandas as pd


# Opening JSON file
json_file = open('jsonveri1.json')

# returns JSON object as
# a dictionary
data = json.load(json_file)


"""
df = pd.read_json (r'jsonveri1.json')
df.to_csv (r'son3.csv', index = None)

"""
# Iterating through the json
# list
for i in data["data"]["hacktivity_items"]["edges"]:
    print("databaseId: " + i['node']['databaseId'])
    print("type: " + i['node']['type'])
    print("total_count: " + str(i['node']['votes']['total_count']))
    print("Handle: " + i['node']['team']['handle'])
    print("reporter: " + i['node']['reporter']['username'])
    
    try:
        print("title: " + i['node']['report']['title'])
    except:
        print("title: " + "null")

    try:
          print("substate: " + i['node']['report']['substate'])
    except:
          print("substate: " + "null")
          
    try:
          print("url: " + i['node']['report']['url'])
    except:
          print("url: " + "null")
          
          
    print("last: " + i['node']['latest_disclosable_action'])
    print("last_activty_time: " + i['node']['latest_disclosable_activity_at'])
 #  print("requires_view_privilege: " + i['node']['requires_view_privilege'])
 #  print("bounty: " + i['node']['total_awarded_amount'])

    try:
        print("requires_view_privilege: " + str(i['node']['requires_view_privilege']))
    except:
        print("requires_view_privilege: " + "null")
#finally:
    
    try:
        print("severity_rating: " + str(i['node']['severity_rating']))
    except:
        print("severity_rating: " + "null")

    print("bounty: " + str(i['node']['total_awarded_amount']))
    print("currency: " + i['node']['currency'])


    
 #   print("Usernames: ")
 #   for node in i['node']["voters"]["edges"]:
 #       print("\t" + node["node"]["user"]["username"])
    
    print('\n')
 # print("Handle: " + i['node']['team']['handle'])
       #for node in i['node']["team"]["handle"]:
       #    print("\t" +  node["team"]["handle"])

        

# Closing file
json_file.close()


#Almak istedğim veriler."databaseId":"1424889" "username":"bobrov" , "username":"ms-13"
# "__typename":"Vote" "__typename":"Undisclosed"
# "handle":"irccloud","name":"IRCCloud"
#"Activities::BountyAwarded" "latest_disclosable_activity_at":"2021-12-13T09:52:54.635Z" "total_awarded_amount":250.0,"currency":"USD"

