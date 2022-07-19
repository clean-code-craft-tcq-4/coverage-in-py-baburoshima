import AlertAction_definitions as definitons 

def get_Alertaction(alertTarget, breachType):
  alertAction = None
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
    alertAction = definitons.targetType[alertTarget]
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)
    alertAction = definitons.targetType[alertTarget]
  return alertAction

def send_to_controller(breachType):
  message = f'{definitons.controllerHeader}, {breachType}'
  print(message)
  return message, definitons.controllerHeader

def send_to_email(breachType):
  EmailMessage = None
  if breachType == 'TOO_LOW':
    EmailMessage = f'To: {definitons.recepient}' + '\n' + 'Hi, the temperature is too low'
    print(EmailMessage)
  elif breachType == 'TOO_HIGH':
    EmailMessage = f'To: {definitons.recepient}' + '\n' + 'Hi, the temperature is too high'
    print(EmailMessage)
  return definitons.recepient , EmailMessage
