coolingType = "PASSIVE_COOLING", "HI_ACTIVE_COOLING","MED_ACTIVE_COOLING"

temperature_limits = {"PASSIVE_COOLING":(0,35),
                    "HI_ACTIVE_COOLING":(0,45),
                    "MED_ACTIVE_COOLING":(0,40),}

def get_temperature_breachlimits(coolingType):
  return temperature_limits[coolingType]