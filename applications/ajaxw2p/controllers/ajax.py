def plans():
  args = request.args
  if len(args) is 0:
    plan = '2g'
  else:
    plan = args[0].lower()

  if plan == '2g':
    return '{"status": 200, ' + '\"denominations2G\": ' + str(response.denominations2G) + '}'
  elif plan == '3g':
    return '{"status": 200, ' + '\"denominations3G\": ' + str(response.denominations3G) + '}'
  else:
    return '{"status": 200, ' + '\"denominationsFullTalktime\": ' + str(response.denominationsFullTalktime) + '}'   
