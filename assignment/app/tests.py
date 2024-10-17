from django.test import SimpleTestCase

# Create your tests here.

class TestNearHundredView(SimpleTestCase):

  def test_nhv_110(self):
    response = self.client.get('/near-hundred/110')
    self.assertContains(response, True)
  
  def test_nhv_90(self):
    response = self.client.get('/near-hundred/90')
    self.assertContains(response, True)
  def test_nhv_89(self):
    response = self.client.get('/near-hundred/89')
    self.assertContains(response, False)
  def test_nhv_111(self):
    response = self.client.get('/near-hundred/11')
    self.assertContains(response, False)

class TestStringSplosionView(SimpleTestCase):
  def test_ssv_code(self):
    response = self.client.get('/string-splosion/Code')
    self.assertContains(response, 'CCoCodCode')

  def test_ssv_python(self):
    response = self.client.get('/string-splosion/Python')
    self.assertContains(response, 'PPyPytPythPythoPython')

  def test_ssv_lorem(self):
    response = self.client.get('/string-splosion/lorem')
    self.assertContains(response, 'lorem')
  
  def test_ssv_jojo(self):
    response = self.client.get('/string-splosion/jojo')
    self.assertContains(response, 'jjojojjojo')

class TestCatDogView(SimpleTestCase):
  def test_cdv_1(self):
    response = self.client.get('/cat-dog/catdog')
    self.assertContains(response, True)

  def test_cdv_2(self):
    response = self.client.get('/cat-dog/dog')
    self.assertContains(response, False)

  def test_cdv_3(self):
    response = self.client.get('/cat-dog/cat')
    self.assertContains(response, False)
  
  def test_cdv_4(self):
    response = self.client.get('/cat-dog/cadogcatdodogcacat')
    self.assertContains(response, True)

class TestLoneSumView(SimpleTestCase):
  def test_lsv_1(self):
    response = self.client.get('/lone-sum/1/1/1')
    self.assertContains(response, 0)
  
  def test_lsv_2(self):
    response = self.client.get('/lone-sum/1/1/3')
    self.assertContains(response, 3)
  
  def test_lsv_3(self):
    response = self.client.get('/lone-sum/3/6/9')
    self.assertContains(response, 18)
  
  def test_lsv_4(self):
    response = self.client.get('/lone-sum/68/4/4')
    self.assertContains(response, 68)