# collections.Mapping sorunu için geçici çözüm
import collections.abc
import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    # Python 3.10+ için collections.Mapping'i collections.abc.Mapping olarak tanımlıyoruz
    collections.Mapping = collections.abc.Mapping

from experta import *
from random import choice

class DisProblemi(Fact):
    """Diş problemlerini tutan bir fakt"""
    pass

class DisSagligi(KnowledgeEngine):
    """Diş sağlığı uzman sistemi"""
    
    @Rule(DisProblemi(problem="dis_eti_kanamasi"))
    def dis_eti_kanamasi(self):
        print("Diş fırçalarken diş eti kanaması olursa, diş hastalığı vardır ve diş hekimine başvurmalısınız.")
    
    @Rule(DisProblemi(problem="uzun_sureli_dis_eti_kanamasi"))
    def uzun_sureli_dis_eti_kanamasi(self):
        print("Diş fırçalarken uzun süreli diş eti kanaması olursa, dişeti çekilmesi vardır ve diş hekimine başvurmalısınız.")
    
    @Rule(AND(DisProblemi(problem="dis_eti_cekilmesi"), DisProblemi(problem="dis_koku_gorunuyor")))
    def dis_eti_cekilmesi_ve_kok_gorunumu(self):
        print("Diş eti çekilmesi var ve diş kökü görünüyorsa, dolgu yaptırmalısınız.")
    
    @Rule(DisProblemi(problem="renk_degisimi"))
    def dis_renk_degisimi(self):
        print("Dişte yiyecek ve içeceklerden oluşan renk değişimi varsa, dişleri temizlemelisiniz.")
    
    @Rule(DisProblemi(problem="morarma"))
    def yeni_dis_morarma(self):
        print("Yeni diş çıkarken morarma görünüyorsa, diş hekimine başvurmalısınız.")
    
    @Rule(DisProblemi(problem="agrisiz_curuk"))
    def agrisiz_curuk(self):
        print("Dişte ağrı yapmayan çürük varsa, dolgu yaptırmalısınız.")
    
    @Rule(DisProblemi(problem="ileri_derece_curuk"))
    def ileri_derece_curuk(self):
        print("Dişteki çürük ileri derecedeyse, kanal tedavisi ve dolgu yaptırmalısınız.")


uzman = DisSagligi()
uzman.reset()
uzman.declare(DisProblemi(problem=choice(["dis_eti_kanamasi", "uzun_sureli_dis_eti_kanamasi", "dis_eti_cekilmesi_ve_kok_gorunumu", "dis_renk_degisimi", "yeni_dis_morarma", "agrisiz_curuk", "ileri_derece_curuk"])))
uzman.run()
