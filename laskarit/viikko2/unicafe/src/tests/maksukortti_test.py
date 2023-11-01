import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 12.0)
    
    def test_saldo_vahenee_jos_raha_riittaa(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)
    
    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_true_kun_riittaa(self):
        self.assertEqual(str(self.maksukortti.ota_rahaa(200)), 'True')
    
    def test_ota_rahaa_palauttaa_false_kun_ei_riita(self):
        self.assertEqual(str(self.maksukortti.ota_rahaa(1200)), 'False')
    
    def test_saldo_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_palautus_merkkijonona(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")