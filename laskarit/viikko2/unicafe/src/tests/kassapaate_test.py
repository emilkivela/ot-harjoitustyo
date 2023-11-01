import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_alustuksessa_kassan_rahamaara_on_oikea(self):
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    def test_alustuksessa_myytyjen_edullisten_maara_on_oikea(self):
        self.assertEqual(str(self.kassa.edulliset), "0")

    def test_alustuksessa_myytyjen_maukkaiden_maara_on_oikea(self):
        self.assertEqual(str(self.kassa.maukkaat), "0")
    
    def test_jos_maksu_kateisella_riittava_rahamaara_kasvaa_edullisen_hinnan_verran(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100240")
    
    def test_jos_maksu_kateisella_riittava_rahamaara_kasvaa_maukkaan_hinnan_verran(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100400")
    
    def test_jos_maksu_kateisella_riittava_vaihtoraha_oikein_edullisella(self):
        self.assertEqual(str(self.kassa.syo_edullisesti_kateisella(250)), "10")
    
    def test_jos_maksu_kateisella_riittava_vaihtoraha_oikein_maukkaalla(self):
        self.assertEqual(str(self.kassa.syo_maukkaasti_kateisella(450)), "50")
    
    def test_jos_maksu_kateisella_riittava_ostettujen_edullisten_lounaiden_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassa.edulliset), "1")
    
    def test_jos_maksu_kateisella_riittava_maukkaiden_lounaiden_maara_kasvaa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassa.maukkaat), "1")
    
    def test_jos_maksu_kateisella_ei_riittava_ostettujen_edullisten_lounaiden_maara_ei_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassa.edulliset), "0")
    
    def test_jos_maksu_kateisella_ei_riittava_ostettujen_maukkaiden_lounaiden_maara_ei_kasva(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(str(self.kassa.edulliset), "0")
    
    def test_jos_maksu_kateisella_ei_riittava_rahat_palautetaan_edullisista(self):
        self.assertEqual(str(self.kassa.syo_edullisesti_kateisella(200)), "200")
    
    def test_jos_maksu_ei_riittava_rahat_palautetaan_maukkaista(self):
        self.assertEqual(str(self.kassa.syo_maukkaasti_kateisella(350)), "350")

    def test_jos_maksu_kortilla_riittava_edulliseen_lounaaseen_palautetaan_True(self):
        self.assertEqual(str(self.kassa.syo_edullisesti_kortilla(self.kortti)), "True")        

    def test_jos_maksu_kortilla_riittava_maukkaseen_lounaaseen_palautetaan_True(self):
        self.assertEqual(str(self.kassa.syo_maukkaasti_kortilla(self.kortti)), "True")    
    
    def test_jos_maksu_kortilla_ei_riittava_edulliseen_lounaaseen_palautetaan_False(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.syo_edullisesti_kortilla(self.kortti)), "False")    
    
    def test_jos_maksu_kortilla_ei_riittava_maukkaaseen_lounaaseen_palautetaan_False(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.syo_maukkaasti_kortilla(self.kortti)), "False")   
    
    def test_jos_maksu_kortilla_riittava_kortilta_veloitetaan_edullisen_hinta(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti.saldo), "760")
    
    def test_jos_maksu_kortilla_riittava_kortilta_veloitetaan_maukkaan_hinta(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti.saldo), "600")
    
    def test_jos_maksu_kortilla_riittava_edulliseen_kassa_ei_kasva(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_jos_maksu_kortilla_riittava_maukkaaseen_kassa_ei_kasva(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_jos_maksu_kortilla_riittava_edullisten_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.edulliset), "1")
    
    def test_jos_maksu_kortilla_riittava_maukkaiden_maara_kasvaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.maukkaat), "1")
    
    def test_jos_maksu_kortilla_ei_riittava_edulliseen_edullisten_maara_muuttumaton(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.edulliset), "0")

    def test_jos_maksu_kortilla_ei_riittava_maukkaaseen_lounaaseen_maukkaiden_maara_muuttumaton(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kassa.maukkaat), "2")

    def test_ladattaessa_rahaa_kortille_kortin_saldo_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(str(self.kortti.saldo), "1200"),

    def test_ladattaessa_rahaa_kortille_kassan_rahamaara_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100200") 
    
    def test_ladattaessa_negatiivinen_summa_kortille_kortin_saldo_ei_muutu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -200)
        self.assertEqual(str(self.kortti.saldo), "1000")
    
    def test_kassassa_rahaa_euroina_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)