import temperature_limits as limits
import AlertAction as action

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit, upperLimit = limits.get_temperature_breachlimits(coolingType)
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, coolingType, temperatureInC):
  breachType =\
    classify_temperature_breach(coolingType, temperatureInC)
  Action = action.get_Alertaction(alertTarget,breachType)
  return Action

