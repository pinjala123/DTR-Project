#!/usr/bin/python
import os
import json
import re
command="aws sqs receive-message --region us-west-2 --queue-url https://sqs.us-west-2.amazonaws.com/652061908131/nike-edf-dtr  --attribute-names All --message-attribute-names All --max-number-of-messages 1"

line=os.popen(command).read()
print "%s" % line
#parsed_json = json.loads(line)
#print(parsed_json ['Messages'][0]['Body'])
  # temp=json.loads(parsed_json)
  # print (temp ['Records'][0]['s3']['object']['key'])
if (len(line) > 1):
    image = json.loads(line)
    #for temp in image:
      #for temp1 in temp["build_images"]:
    #print image["Messages"][0]["Body"]["Records"][0]["s3"]["object"]["key"]
    temp=image['Messages'][0]['Body']
    time=image['Messages'][0]["Attributes"]["SentTimestamp"]
    print time
    image1 = json.loads(temp)
    print image1
    temp2=image1['Records'][0]['s3']['object']['key']
    print temp2