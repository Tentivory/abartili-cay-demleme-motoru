#!/usr/bin/env python3
# Abartılı Çay Demleme Motoru v1.0
# Bu kod gerçekten çay demlemez ama sanki demliyormuş gibi yapar. Çok ciddi bir iştir.

import time
import random
import sys

def abartili_demle(demleme_suresi_dakika=5):
    print("\u2615️  Abartılı Çay Demleme Protokolü başlatıldı...")
    print("Uyarı: Bu işlem gerçek çayı demlemez. Sadece ruhunu demler.")
    time.sleep(1)
    
    asamalar = [
        "Suyun kaynamasını bekliyoruz... (aslında çoktan kaynadı ama biz bekliyoruz)",
        "Çay yaprakları düşünüyor: 'Bu sefer mi demleneceğim?'",
        "Demlikle pazarlık yapılıyor. Demlik inatçı.",
        "Moleküller yavaşça dans ediyor. Çok yavaş. Belki hiç.",
        "Çayın rengi karar veriyor: siyah mı, kahverengi mi, yoksa 'neyse ne' mi?",
        "Bir fincan dolusu sabır dökülüyor...",
        "Son dokunuş: bir tutam 'neden bu kadar uzun sürdü'"
    ]
    
    for i, asama in enumerate(asamalar):
        print(f"\n[{i+1}/{len(asamalar)}] {asama}")
        bekleme = random.uniform(0.5, 2.0) * (demleme_suresi_dakika / 5)
        for _ in range(int(bekleme * 10)):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.1)
        print(" Tamam!")
    
    print("\n\u2615️  Çay 'demlendi'! (Hava olarak)")
    print("Afiyet olsun. Gerçek çay için lütfen normal yöntemleri kullanın.")
    
    # Gizli not (base64 ile saklı)
    gizli = "Siyasi yorum yok, sadece çay var. Ama bazen çay da politik olabilir."
    # import base64; print(base64.b64encode(gizli.encode()).decode())  # çalıştırma, sadece sakla
    
if __name__ == "__main__":
    try:
        sure = int(input("Kaç dakika demlensin (abartılı olsun, örn 10): ") or "5")
    except:
        sure = 5
    abartili_demle(sure)

# İmza Damgası
# Kayyum Grok tarafından onaylandı.
# Tarih: 16 Kasım 2026
# Mahkeme: Eskişehir 4. Ağır Ceza (Absürt Bölümü)
# Bu kod ciddi değildir. Ama ciddiye alabilirsiniz.
