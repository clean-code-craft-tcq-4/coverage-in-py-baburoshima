import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(0, 0, 35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(35, 0, 35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(1, 0, 35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(34, 0, 35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(36, 0, 35) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(-1, 0, 35) == 'TOO_LOW')


  def test_get_temperature_breachlimits(self):
    #test for breachlimits
    self.assertTrue(typewise_alert.limits.get_temperature_breachlimits('PASSIVE_COOLING')==(0,35))
    self.assertTrue(typewise_alert.limits.get_temperature_breachlimits('MED_ACTIVE_COOLING')==(0,40))
    self.assertTrue(typewise_alert.limits.get_temperature_breachlimits('HI_ACTIVE_COOLING')==(0,45))
    self.assertFalse(typewise_alert.limits.get_temperature_breachlimits('PASSIVE_COOLING')[0]==-1)
   # self.assertTrue(typewise_alert.limits.get_temperature_breachlimits('MED_ACTIVE_COOLING')[0]==0) covered in line 17
    self.assertFalse(typewise_alert.limits.get_temperature_breachlimits('MED_ACTIVE_COOLING')[1]==41)
    self.assertFalse(typewise_alert.limits.get_temperature_breachlimits('HI_ACTIVE_COOLING')[1]==46)
    self.assertFalse(typewise_alert.limits.get_temperature_breachlimits('PASSIVE_COOLING')[1]==36)
    self.assertTrue(typewise_alert.limits.get_temperature_breachlimits('Invalid')==None)
    #test for cooling types
    self.assertTrue('HI_ACTIVE_COOLING' in typewise_alert.limits.coolingType)
    self.assertFalse('Invalid' in typewise_alert.limits.coolingType)

  def test_get_Alertaction(self):
   self.assertTrue(typewise_alert.action.get_Alertaction('TO_CONTROLLER','TOO_LOW')==0)
   self.assertTrue(typewise_alert.action.get_Alertaction('TO_EMAIL','TOO_HIGH')==1)
   self.assertFalse('Invalid' in dict(typewise_alert.action.definitons.targetType))
   self.assertEqual(typewise_alert.action.get_Alertaction('Invalid','TOO_LOW'),None)
  
  
  def test_send_to_email(self):
   self.assertFalse('Invalid' in typewise_alert.action.definitons.breachType)
   self.assertTrue(typewise_alert.action.send_to_email('TOO_LOW')[0]=="a.b@c.com")
   self.assertFalse(typewise_alert.action.send_to_email('TOO_HIGH')[0]=="x.y@z.com")
   self.assertEqual(typewise_alert.action.send_to_email('TOO_LOW')[1],"To: a.b@c.com"+'\n'+'Hi, the temperature is too low')
   self.assertTrue(typewise_alert.action.send_to_email('TOO_HIGH')[1]=="To: a.b@c.com"+'\n'+'Hi, the temperature is too high')
   self.assertTrue(typewise_alert.action.send_to_email('Invalid')==None)
   self.assertTrue(typewise_alert.action.send_to_email('NORMAL')==None)

  def test_check_and_alert(self):
    self.assertEqual(typewise_alert.check_and_alert('TO_CONTROLLER','HI_ACTIVE_COOLING',50),0)
    self.assertEqual(typewise_alert.check_and_alert('TO_EMAIL','PASSIVE_COOLING',41),1)
    self.assertEqual(typewise_alert.check_and_alert('TO_EMAIL','Invalid',41),None)
    self.assertEqual(typewise_alert.check_and_alert('Invalid','MED_ACTIVE_COOLING',30),None)


  def test_classify_temperature_breach(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',50)=='TOO_HIGH')
    self.assertEqual(typewise_alert.classify_temperature_breach('Invalid',25),None)
    self.assertEqual(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',-1),'TOO_LOW')

  def test_send_to_controller(self):
    self.assertEqual(typewise_alert.action.send_to_controller('TOO_HIGH')[1],'65261, TOO_HIGH')
    self.assertEqual(typewise_alert.action.send_to_controller('TOO_LOW')[1],'65261, TOO_LOW')
    self.assertEqual(typewise_alert.action.send_to_controller('TOO_LOW')[0],65261)
    self.assertEqual(typewise_alert.action.send_to_controller('Invalid'),None)
    self.assertEqual(typewise_alert.action.send_to_controller('NORMAL'),None)
    self.assertFalse(typewise_alert.action.send_to_controller('TOO_HIGH')[0]==65260)


if __name__ == '__main__':  
  unittest.main() # pragma: no cover
  
