import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alustetaan_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.15")
    
    def test_rahan_ottaminen_kortilta_toimii(self):
        self.maksukortti.ota_rahaa(4)
        self.assertEqual(str(self.maksukortti), "saldo: 0.06")

    def test_saldo_ei_muutu_joe_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_ota_rahaa_palauttaa_True_jos_toimii(self):
        self.assertEqual(str(self.maksukortti.ota_rahaa(2)), "True")

    def test_ota_rahaa_palauttaa_False_jos_ei_toimi(self):
        self.assertEqual(str(self.maksukortti.ota_rahaa(20)), "False")

