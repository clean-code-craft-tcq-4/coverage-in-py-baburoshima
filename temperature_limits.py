PASSIVE = "PASSIVE_COOLING"
HI_ACTIVE = "HI_ACTIVE_COOLING"
MED_ACTIVE = "MED_ACTIVE_COOLING"

coolingType = PASSIVE, HI_ACTIVE,MED_ACTIVE

temperature_limits = {PASSIVE:(0,35),
                    HI_ACTIVE:(0,45),
                    MED_ACTIVE:(0,40),}

def get_temperature_breachlimits(coolingTypeInput):
  if coolingTypeInput in coolingType:
    return temperature_limits[coolingTypeInput]
  else:
    return None