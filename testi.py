paylod_activity={"activity": "TEST","activity_date": 1444403649404}
for x in range(1,99):
  key = 'key%s'% x
  value ='value%s'% x
  paylod_activity[key] = value
request_payload = {} 
request_payload["log_payload"] = paylod_activity
print request_payload	

