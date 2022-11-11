import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    # alku
    def test_rahamaara_on_alussa_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_lounaiden_maara_alussa_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myytyjen_maukkaiden_lounaiden_maara_alussa_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    # syo_edullisesti_kateisella
    def test_syo_edullisesti_kateisella_kasvattaa_kassan_rahamaaraa_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kassan_rahamaara_ei_muutu_kun_edullinen_kateismaksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_vaihtorahan_suuruus_oikea_kun_syo_edullisesti_kateisella_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    
    def test_kaikki_rahat_palautetaan_kun_edullinen_kateismaksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_syo_edullisesti_kateisella_kasvattaa_myytyjen_lounaiden_maaraa_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)    

    def test_myytyjen_edullisten_lounaiden_maara_ei_muutu_kun_kateismaksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

    # syo_maukkaasti_kateisella
    def test_syo_maukkaasti_kateisella_kasvattaa_kassan_rahamaaraa_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_kassan_rahamaara_ei_muutu_kun_maukas_kateismaksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_vaihtorahan_suuruus_oikea_kun_syo_maukkaasti_kateisella_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kaikki_rahat_palautetaan_kun_maukas_kateismaksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_syo_maukkaasti_kateisella_kasvattaa_myytyjen_lounaiden_maaraa_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_myytyjen_maukkaiden_lounaiden_maara_ei_muutu_kun_kateismaksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    # syo_edullisesti_kortilla
    def test_syo_edullisesti_kortilla_palauttaa_True_kun_kortilla_tarpeeksi_saldoa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_syo_edullisesti_kortilla_palauttaa_False_kun_kortilla_ei_tarpeeksi_saldoa(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    
    def test_syo_edullisesti_kortilla_veloittaa_summan_kortilta_kun_rahaa_riittavasti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_syo_edullisesti_ei_muuta_kortin_rahamaaraa_kun_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_syo_edullisesti_kortilla_kasvattaa_myytyjen_lounaiden_maaraa_kun_kortilla_tarpeeksi_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisten_lounaiden_maara_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_edullisesti_kortilla_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # syo_maukkaasti_kortilla
    def test_syo_maukkaasti_kortilla_palauttaa_True_kun_kortilla_tarpeeksi_saldoa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_palauttaa_False_kun_kortilla_ei_tarpeeksi_saldoa(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    
    def test_syo_maukkaasti_kortilla_kasvattaa_myytyjen_lounaiden_maaraa_kun_kortilla_tarpeeksi_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaiden_lounaiden_maara_ei_muutu_kun_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_veloittaa_summan_kortilta_kun_rahaa_riittavasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_maukkaasti_ei_muuta_kortin_rahamaaraa_kun_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_syo_maukkaasti_kortilla_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    # lataa_rahaa_kortille
    def test_lataa_rahaa_kortille_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
    
    def test_lataa_rahaa_kortille_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
    
    def test_kortin_saldo_ei_muutu_jos_ladattava_summa_on_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kassassa_oleva_rahamaara_ei_muutu_jos_kortille_ladattava_summa_on_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)