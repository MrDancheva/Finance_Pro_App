import customtkinter as ctk
import json
import os
import sys
import requests
import threading
import urllib3
import time
import webbrowser
import xml.etree.ElementTree as ET
from datetime import datetime

# SSL Hatalarını Gizle
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==========================================
# 1. DİL SİSTEMİ
# ==========================================
METINLER = {
    "tr": {
        "app_title": "Finans Pro - Varlık Yönetim Sistemi",
        "ana_sayfa": "🏠 Ana Sayfa",
        "portfoyum": "💼 Portföyüm",
        "canli_piyasa": "📈 Canlı Piyasa",
        "hesap_makinesi": "🧮 Hesap Makinesi",
        "ayarlar": "⚙️ Ayarlar",
        "hakkimizda": "💬 Hakkımızda",
        "hos_geldiniz": "Hoş Geldiniz,",
        "finansal_durum": "Finansal Durum Özetiniz",
        "toplam_net_varlik": "TOPLAM NET VARLIK",
        "gizle": "🔒 Gizle",
        "portfoy_detaylari": "Portföy Detayları",
        "yeni_kisi": "+ Yeni Kişi",
        "kisi_sil": "- Kişi Sil",
        "hizli_ekle": "Hızlı Ekle:",
        "cuzdan": "Cüzdan (+)",
        "borc": "Borç (-)",
        "alacak": "Alacak (+)",
        "islem_kaydet": "💰 İşlemi Kaydet",
        "toplam_varlik": "TOPLAM VARLIK",
        "toplam_borc": "TOPLAM BORÇ",
        "toplam_alacak": "TOPLAM ALACAK",
        "kime": "Kime",
        "kimden": "Kimden",
        "aydinlik": "Aydınlık ☀️",
        "karanlik": "Karanlık 🌙",
        "canli_piyasa_title": "CANLI PİYASA",
        "dolar": "Dolar",
        "euro": "Euro",
        "gram_altin": "Gr. Altın",
        "yukleniyor": "Yükleniyor...",
        "ayarlar_title": "Ayarlar",
        "guvenlik": "GÜVENLİK",
        "kullanici_bilgileri": "👤 Kullanıcı Bilgileri",
        "ad_soyad": "Ad Soyad:",
        "sifre_sor": "Uygulama Açılışında Şifre Sor",
        "pin_kodu": "🔐 PIN Kodu",
        "mevcut": "Mevcut:",
        "goster": "🔓 Göster",
        "degistir": "✏️ Değiştir",
        "menu_kisayollari": "MENÜ KISAYOLLARI",
        "yeni_link_ekle": "➕ Yeni Link Ekle",
        "dil_secimi": "🌐 Dil Seçimi",
        "ayarlari_kaydet": "💾 AYARLARI KAYDET",
        "tum_verileri_sifirla": "⚠️ Tüm Verileri Sıfırla",
        "hakkimizda_title": "Hakkımızda",
        "gelistiriciler": "👨‍💻 Geliştiriciler",
        "ilk_kurulum_baslik": "Finans Pro'ya Hoş Geldiniz! 🎉",
        "ilk_kurulum_aciklama": "Size nasıl hitap edelim?",
        "ilk_kurulum_placeholder": "Adınız ve Soyadınız",
        "ilk_kurulum_devam": "Devam Et →",
        "kullanim_kilavuzu_title": "Kullanım Kılavuzu",
        "kullanim_kilavuzu_aciklama": "Finans Pro ile varlıklarınızı kolayca yönetin!",
        "basla": "🚀 Başla",
        "kisi_ekle_baslik": "Yeni Kişi Ekle",
        "kisi_ekle_aciklama": "Eklemek istediğiniz kişinin adını giriniz:",
        "kisi_sil_baslik": "Onay",
        "kisi_isim_eslesme_hatasi": "İsim eşleşmedi, silme iptal edildi.",
        "bakiye_duzenle": "Bakiye Düzenle",
        "gecerli_sayi_gir": "Geçerli bir sayı giriniz!",
        "silinecek_kisi_sec": "Silinecek kişi seçiniz!",
        "hata": "Hata",
        "basari": "Başarı",
        "pin_yanlis": "Yanlış PIN! Ayarlar kaydedilmedi.",
        "ad_soyad_bos": "Lütfen adınızı ve soyadınızı giriniz!",
        "varliklarim": "Varlıklarım",
        "alacaklarim": "Alacaklarım",
        "borclarim": "Borçlarım",
        "portfoyum_kisa": "Portföyüm",
        "canli_piyasa_kisa": "Canlı Piyasa",
        "hesap_makinesi_kisa": "Hesap Makinesi",
        "ayarlar_kisa": "Ayarlar",
    },
    "en": {
        "app_title": "Finance Pro - Asset Management System",
        "ana_sayfa": "🏠 Home",
        "portfoyum": "💼 My Portfolio",
        "canli_piyasa": "📈 Live Market",
        "hesap_makinesi": "🧮 Calculator",
        "ayarlar": "⚙️ Settings",
        "hakkimizda": "💬 About Us",
        "hos_geldiniz": "Welcome,",
        "finansal_durum": "Your Financial Summary",
        "toplam_net_varlik": "TOTAL NET WORTH",
        "gizle": "🔒 Hide",
        "portfoy_detaylari": "Portfolio Details",
        "yeni_kisi": "+ Add Person",
        "kisi_sil": "- Remove Person",
        "hizli_ekle": "Quick Add:",
        "cuzdan": "Wallet (+)",
        "borc": "Debt (-)",
        "alacak": "Receivable (+)",
        "islem_kaydet": "💰 Save Transaction",
        "toplam_varlik": "TOTAL ASSETS",
        "toplam_borc": "TOTAL DEBT",
        "toplam_alacak": "TOTAL RECEIVABLES",
        "kime": "To Whom",
        "kimden": "From Whom",
        "aydinlik": "Light ☀️",
        "karanlik": "Dark 🌙",
        "canli_piyasa_title": "LIVE MARKET",
        "dolar": "Dollar",
        "euro": "Euro",
        "gram_altin": "Gold (Gr)",
        "yukleniyor": "Loading...",
        "ayarlar_title": "Settings",
        "guvenlik": "SECURITY",
        "kullanici_bilgileri": "👤 User Information",
        "ad_soyad": "Full Name:",
        "sifre_sor": "Ask for Password on Startup",
        "pin_kodu": "🔐 PIN Code",
        "mevcut": "Current:",
        "goster": "🔓 Show",
        "degistir": "✏️ Change",
        "menu_kisayollari": "MENU SHORTCUTS",
        "yeni_link_ekle": "➕ Add New Link",
        "dil_secimi": "🌐 Language Selection",
        "ayarlari_kaydet": "💾 SAVE SETTINGS",
        "tum_verileri_sifirla": "⚠️ Reset All Data",
        "hakkimizda_title": "About Us",
        "gelistiriciler": "👨‍💻 Developers",
        "ilk_kurulum_baslik": "Welcome to Finance Pro! 🎉",
        "ilk_kurulum_aciklama": "How should we address you?",
        "ilk_kurulum_placeholder": "Your Full Name",
        "ilk_kurulum_devam": "Continue →",
        "kullanim_kilavuzu_title": "User Guide",
        "kullanim_kilavuzu_aciklama": "Manage your assets easily with Finance Pro!",
        "basla": "🚀 Start",
        "kisi_ekle_baslik": "Add New Person",
        "kisi_ekle_aciklama": "Enter the name of the person you want to add:",
        "kisi_sil_baslik": "Confirmation",
        "kisi_isim_eslesme_hatasi": "Name didn't match, deletion cancelled.",
        "bakiye_duzenle": "Edit Balance",
        "gecerli_sayi_gir": "Please enter a valid number!",
        "silinecek_kisi_sec": "Please select a person to delete!",
        "hata": "Error",
        "basari": "Success",
        "pin_yanlis": "Wrong PIN! Settings not saved.",
        "ad_soyad_bos": "Please enter your full name!",
        "varliklarim": "My Assets",
        "alacaklarim": "My Receivables",
        "borclarim": "My Debts",
        "portfoyum_kisa": "My Portfolio",
        "canli_piyasa_kisa": "Live Market",
        "hesap_makinesi_kisa": "Calculator",
        "ayarlar_kisa": "Settings",
    }
}

# ==========================================
# 2. AYARLAR VE RENK PALETİ
# ==========================================
ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("dark-blue")

# Renkler (Aydınlık, Karanlık)
RENK_SIDEBAR = ("#2c3e50", "#1a1a2e")       # Koyu Lacivert / Koyu Mor-Mavi
RENK_MAIN_BG = ("#ecf0f1", "#16213e")       # Buz Grisi / Koyu Mavi
RENK_KART_BG = ("#ffffff", "#0f3460")       # Beyaz / Lacivert
RENK_TEXT_ANA = ("#2c3e50", "#e8f1f5")      # Başlık Rengi
RENK_TEXT_SILIK = ("#7f8c8d", "#94a3b8")    # Alt Metin Rengi
RENK_TEXT_SIDEBAR = ("#ecf0f1", "#e8f1f5")  # Menü Yazıları

# Vurgu Renkleri
RENK_MAVI = ("#3498db", "#60a5fa")
RENK_AKTIF_BTN = ("#34495e", "#2563eb")
RENK_YESIL = ("#27ae60", "#22c55e")
RENK_KIRMIZI = ("#e74c3c", "#f87171")
RENK_SARI = ("#f39c12", "#fbbf24")
RENK_KART_HOVER = ("#bdc3c7", "#1e3a5f")

# Veri dosyası için kullanıcının dokümanlar klasörünü kullan (EXE uyumluluğu için)
if getattr(sys, 'frozen', False):
    # EXE olarak çalışıyorsa
    VERI_KLASORU = os.path.join(os.path.expanduser("~"), "Documents", "FinansPro")
else:
    # Python olarak çalışıyorsa
    VERI_KLASORU = os.path.dirname(os.path.abspath(__file__))

# Klasör yoksa oluştur
os.makedirs(VERI_KLASORU, exist_ok=True)
DOSYA_ADI = os.path.join(VERI_KLASORU, "birikimler_pro.json")

ParaBirimleri = {
    "TL (Türk Lirası)": "tl",
    "Gram Altın": "gram-altin",
    "Dolar ($)": "dolar",
    "Euro (€)": "euro",
    "Sterlin (£)": "sterlin",
    "Çeyrek Altın": "ceyrek",
    "Gümüş (Gr)": "gumus",
    "Bitcoin ($)": "btc"
}

# ==========================================
# 2. VERİ MOTORU
# ==========================================
class VeriMotoru:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def float_yap(self, veri):
        try: return float(veri)
        except: return 0.0

    def veri_getir(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Veriler çekiliyor...")
        kurlar = {k: 0 for k in ParaBirimleri.values()}
        kurlar["tl"] = 1.0
        tablo = []
        
        # TCMB
        try:
            r = requests.get("https://www.tcmb.gov.tr/kurlar/today.xml", timeout=5, verify=False)
            if r.status_code == 200:
                root = ET.fromstring(r.content)
                for currency in root.findall('Currency'):
                    kod = currency.get('Kod')
                    satis = currency.find('BanknoteSelling').text or currency.find('ForexSelling').text
                    fiyat = self.float_yap(satis)
                    if kod == "USD": kurlar["dolar"] = fiyat
                    elif kod == "EUR": kurlar["euro"] = fiyat
                    elif kod == "GBP": kurlar["sterlin"] = fiyat
                
                tablo.append({"isim": "ABD DOLARI (TCMB)", "alis": kurlar["dolar"]*0.99, "satis": kurlar["dolar"], "degisim": "-"})
                tablo.append({"isim": "EURO (TCMB)", "alis": kurlar["euro"]*0.99, "satis": kurlar["euro"], "degisim": "-"})
                tablo.append({"isim": "STERLİN (TCMB)", "alis": kurlar["sterlin"]*0.99, "satis": kurlar["sterlin"], "degisim": "-"})
        except: pass

        # BINANCE
        try:
            r = requests.get("https://api.binance.com/api/v3/ticker/price", timeout=5)
            data = r.json()
            btc_usd = 0; ons_usd = 0
            for item in data:
                if item["symbol"] == "BTCUSDT": btc_usd = self.float_yap(item["price"])
                elif item["symbol"] == "PAXGUSDT": ons_usd = self.float_yap(item["price"])

            if btc_usd > 0 and kurlar["dolar"] > 0:
                kurlar["btc"] = btc_usd * kurlar["dolar"]
                tablo.append({"isim": "BITCOIN", "alis": kurlar["btc"], "satis": kurlar["btc"], "degisim": "-"})

            if ons_usd > 0 and kurlar["dolar"] > 0:
                gram_tl = (ons_usd * kurlar["dolar"]) / 31.1035
                kurlar["gram-altin"] = gram_tl
                kurlar["ceyrek"] = gram_tl * 1.63
                kurlar["gumus"] = gram_tl / 80 
                tablo.append({"isim": "GRAM ALTIN", "alis": gram_tl*0.99, "satis": gram_tl, "degisim": "-"})
                tablo.append({"isim": "ÇEYREK ALTIN", "alis": kurlar["ceyrek"]*0.98, "satis": kurlar["ceyrek"], "degisim": "-"})
        except: pass

        if kurlar["dolar"] == 0:
            return {"tl": 1.0, "gram-altin": 3080.0, "dolar": 34.75, "sterlin": 44.00, "euro": 37.50, "ceyrek": 5200.0, "gumus": 35.0, "btc": 3300000.0}, []
        return kurlar, tablo

# ==========================================
# 3. YARDIMCI PENCERELER
# ==========================================
class OzelGirisPenceresi(ctk.CTkToplevel):
    def __init__(self, parent, baslik, mesaj, sifreli=False, dil="tr"):
        super().__init__(parent)
        self.girilen_deger = None
        self.title(baslik)
        self.geometry("350x220")
        self.configure(fg_color=RENK_MAIN_BG)
        self.attributes("-topmost", True)
        
        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 175
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 110
        self.geometry(f"+{x}+{y}")

        ctk.CTkLabel(self, text=mesaj, font=("Arial", 14), text_color=RENK_TEXT_ANA).pack(pady=20)
        self.entry = ctk.CTkEntry(self, width=250, show="*" if sifreli else "", fg_color=("white", "#2d3436"), text_color=RENK_TEXT_ANA)
        self.entry.pack(pady=10)
        self.entry.focus()
        self.entry.bind('<Return>', lambda e: self.onayla())

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=20)
        iptal_text = "İptal" if dil == "tr" else "Cancel"
        tamam_text = "Tamam" if dil == "tr" else "OK"
        ctk.CTkButton(btn_frame, text=iptal_text, command=self.destroy, fg_color=RENK_KIRMIZI, width=100).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text=tamam_text, command=self.onayla, fg_color=RENK_YESIL, width=100).pack(side="left", padx=10)

    def onayla(self):
        self.girilen_deger = self.entry.get()
        self.destroy()

class OzelUyariPenceresi(ctk.CTkToplevel):
    def __init__(self, parent, baslik, mesaj, tur="hata", dil="tr"):
        super().__init__(parent)
        self.title(baslik)
        self.geometry("400x200")
        self.configure(fg_color=RENK_MAIN_BG)
        self.attributes("-topmost", True)
        
        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 200
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 100
        self.geometry(f"+{x}+{y}")
        
        c = RENK_KIRMIZI if tur == "hata" else RENK_MAVI
        ctk.CTkLabel(self, text=mesaj, font=("Arial", 13), wraplength=350, text_color=RENK_TEXT_ANA).pack(pady=30, padx=20)
        tamam_text = "Tamam" if dil == "tr" else "OK"
        ctk.CTkButton(self, text=tamam_text, command=self.destroy, fg_color=c, width=120).pack(pady=10)

# ==========================================
# 4. ANA UYGULAMA
# ==========================================
class FinansProApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Dil ayarını yükle
        self.data = self.dosyadan_yukle()
        self.dil = self.data["__AYARLAR__"].get("dil", "tr")
        
        self.title(METINLER[self.dil]["app_title"] + " 1.1")
        self.geometry("1280x850")
        self.minsize(1024, 720)  # Minimum pencere boyutu
        
        # Icon ayarla
        try:
            self.iconbitmap("icon.ico")
        except:
            pass  # Icon bulunamazsa devam et

        self.veri_motoru = VeriMotoru()
        
        self.kurlar = {k: 0 for k in ParaBirimleri.values()}
        self.kurlar["tl"] = 1.0
        self.piyasa_tablosu = []
        self.aktif_sayfa = "home"
        self.veri_yukleniyor = False 
        
        self.container = ctk.CTkFrame(self, fg_color=RENK_MAIN_BG)
        self.container.pack(fill="both", expand=True)
        
        # İlk kurulum kontrolü
        if not self.data["__AYARLAR__"].get("kullanici_adi"):
            self.ilk_kurulum_ekrani()
        elif self.data["__AYARLAR__"].get("kullanim_kilavuzu_gosterilsin", True):
            self.kullanim_kilavuzu_ekrani()
        else:
            self.ana_ekrani_yukle()
            
        self.verileri_arkada_guncelle()

    # --- VERİ GÜNCELLEME ---
    def verileri_arkada_guncelle(self):
        if self.veri_yukleniyor: return
        self.veri_yukleniyor = True
        def is_parcacigi():
            try:
                self.kurlar, self.piyasa_tablosu = self.veri_motoru.veri_getir()
            except: pass
            finally: self.after(0, self.arayuzu_tazele)
        threading.Thread(target=is_parcacigi, daemon=True).start()

    def arayuzu_tazele(self):
        self.veri_yukleniyor = False
        if hasattr(self, 'frm_alt') and self.frm_alt.winfo_exists():
            for widget in self.frm_alt.winfo_children(): widget.destroy()
            style = {"font": ("Arial", 12), "text_color": "gray80", "anchor": "w"}
            ctk.CTkLabel(self.frm_alt, text=METINLER[self.dil]["canli_piyasa_title"], font=("Arial", 10, "bold"), text_color="gray60", anchor="w").pack(fill="x", pady=(0,5))
            vals = [(METINLER[self.dil]["dolar"], self.kurlar['dolar']), (METINLER[self.dil]["euro"], self.kurlar['euro']), (METINLER[self.dil]["gram_altin"], self.kurlar['gram-altin'])]
            for ad, val in vals:
                ctk.CTkLabel(self.frm_alt, text=f"{ad}: {val:,.2f} TL" if val>0 else f"{ad}: --", **style).pack(fill="x")

        if self.aktif_sayfa == "home": self.home_verilerini_guncelle()
        elif self.aktif_sayfa == "portfoy": self.dashboard_guncelle()
        elif self.aktif_sayfa == "piyasa": self.piyasa_verilerini_goster()

    # --- DOSYA İŞLEMLERİ ---
    def dosyadan_yukle(self):
        defaults = {
            "pin_aktif": False, "pin": "123456",
            "kullanici_adi": "",
            "kullanim_kilavuzu_gosterilsin": True,
            "son_secili_kullanici": "",
            "linkler": [
                {"ad": "Altınkaynak", "url": "https://www.altinkaynak.com"},
                {"ad": "Döviz.com", "url": "https://www.doviz.com"}
            ]
        }
        if not os.path.exists(DOSYA_ADI): return {"__AYARLAR__": defaults}
        with open(DOSYA_ADI, "r", encoding="utf-8") as f:
            try:
                d = json.load(f)
                if "__AYARLAR__" not in d: d["__AYARLAR__"] = defaults
                else:
                    # Eski format kontrolü ve dönüşümü
                    if "link1_ad" in d["__AYARLAR__"] or "link2_ad" in d["__AYARLAR__"]:
                        linkler = []
                        if d["__AYARLAR__"].get("link1_ad") and d["__AYARLAR__"].get("link1_url"):
                            linkler.append({"ad": d["__AYARLAR__"]["link1_ad"], "url": d["__AYARLAR__"]["link1_url"]})
                        if d["__AYARLAR__"].get("link2_ad") and d["__AYARLAR__"].get("link2_url"):
                            linkler.append({"ad": d["__AYARLAR__"]["link2_ad"], "url": d["__AYARLAR__"]["link2_url"]})
                        d["__AYARLAR__"]["linkler"] = linkler
                        d["__AYARLAR__"].pop("link1_ad", None)
                        d["__AYARLAR__"].pop("link1_url", None)
                        d["__AYARLAR__"].pop("link2_ad", None)
                        d["__AYARLAR__"].pop("link2_url", None)
                    
                    for k, v in defaults.items():
                        if k not in d["__AYARLAR__"]: d["__AYARLAR__"][k] = v
                return d
            except: return {"__AYARLAR__": defaults}

    def dosyaya_kaydet(self):
        with open(DOSYA_ADI, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    # --- EKRANLAR ---
    def ilk_kurulum_ekrani(self):
        for w in self.container.winfo_children(): w.destroy()
        frame = ctk.CTkFrame(self.container, corner_radius=20, fg_color=RENK_KART_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(frame, text="👋", font=("Arial", 60), text_color=RENK_TEXT_ANA).pack(pady=(40, 10))
        ctk.CTkLabel(frame, text="FİNANS PRO'YA HOŞ GELDİNİZ", font=("Arial", 24, "bold"), text_color=RENK_TEXT_ANA).pack(pady=10)
        ctk.CTkLabel(frame, text="Lütfen adınızı ve soyadınızı giriniz:", font=("Arial", 14), text_color=RENK_TEXT_SILIK).pack(pady=(20, 10))
        
        self.ent_kullanici_adi = ctk.CTkEntry(frame, width=300, height=40, justify="center", 
                                              fg_color=("white", "#2d3436"), text_color=RENK_TEXT_ANA,
                                              font=("Arial", 14), placeholder_text="Örn: Samet Can Ceylan, Buse Nur Çalı")
        self.ent_kullanici_adi.pack(pady=15, padx=40)
        self.ent_kullanici_adi.focus()
        self.ent_kullanici_adi.bind('<Return>', lambda e: self.ilk_kurulum_kaydet())
        
        ctk.CTkButton(frame, text="BAŞLA", command=self.ilk_kurulum_kaydet, 
                     width=250, height=45, fg_color=RENK_YESIL, hover_color="#27ae60",
                     font=("Arial", 16, "bold")).pack(pady=(10, 40), padx=40)
    
    def ilk_kurulum_kaydet(self):
        ad = self.ent_kullanici_adi.get().strip()
        if not ad:
            OzelUyariPenceresi(self, "Hata", "Lütfen adınızı ve soyadınızı giriniz!", dil=self.dil)
            return
        
        # Kullanıcı adını ayarlara kaydet
        self.data["__AYARLAR__"]["kullanici_adi"] = ad
        
        # Aynı isimle otomatik portföy kullanıcısı oluştur
        if ad not in self.data:
            self.data[ad] = {
                "varlik": {},
                "borc": {},
                "alacak": {}
            }
        
        # Son seçili kullanıcıyı da bu olarak ayarla
        self.data["__AYARLAR__"]["son_secili_kullanici"] = ad
        
        self.dosyaya_kaydet()
        self.kullanim_kilavuzu_ekrani()
    
    def kullanim_kilavuzu_ekrani(self):
        for w in self.container.winfo_children(): w.destroy()
        
        # Ana frame
        main_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        main_frame.pack(fill="both", expand=True)
        
        # Scroll frame
        scroll = ctk.CTkScrollableFrame(main_frame, fg_color=RENK_KART_BG, corner_radius=20)
        scroll.pack(fill="both", expand=True, padx=100, pady=50)
        
        # Başlık
        ctk.CTkLabel(scroll, text="📖", font=("Arial", 60), text_color=RENK_TEXT_ANA).pack(pady=(30, 10))
        ctk.CTkLabel(scroll, text="KULLANIM KLAVUZU", font=("Arial", 28, "bold"), text_color=RENK_TEXT_ANA).pack(pady=10)
        ctk.CTkLabel(scroll, text="Finans Pro uygulamasını nasıl kullanacağınızı aşağıda bulabilirsiniz:", 
                    font=("Arial", 13), text_color=RENK_TEXT_SILIK, wraplength=700).pack(pady=(5, 30))
        
        # Kılavuz içeriği
        kilavuz_bilgileri = [
            {
                "ikon": "🏠",
                "baslik": "Ana Sayfa",
                "aciklama": "Tüm kullanıcılarınızın toplam net değerini ve özetini görebilirsiniz. Buradan hızlıca portföy durumunuzu kontrol edebilirsiniz."
            },
            {
                "ikon": "💼",
                "baslik": "Portföyüm",
                "aciklama": "Varlıklarınızı, borçlarınızı ve alacaklarınızı buradan ekleyebilir, düzenleyebilir ve silebilirsiniz. Üst kısımdaki hızlı ekleme formu ile anlık işlem yapabilirsiniz. Borç/Alacak seçtiğinizde kişi adı alanı otomatik açılır."
            },
            {
                "ikon": "📈",
                "baslik": "Canlı Piyasa",
                "aciklama": "TCMB ve Binance'den canlı döviz, altın ve kripto para fiyatlarını takip edebilirsiniz. Veriler otomatik olarak güncellenir."
            },
            {
                "ikon": "🧮",
                "baslik": "Hesap Makinesi",
                "aciklama": "Entegre hesap makinesi ile hızlı hesaplamalar yapabilirsiniz. Klavyenizden rakam ve işlem tuşlarını kullanabilirsiniz (0-9, +, -, *, /, Enter, C)."
            },
            {
                "ikon": "⚙️",
                "baslik": "Ayarlar",
                "aciklama": "PIN kodu belirleyebilir, kullanıcı adınızı değiştirebilir ve menü kısayolları (internet linkleri) ekleyebilirsiniz. İstediğiniz kadar link ekleyip silebilirsiniz."
            },
            {
                "ikon": "👥",
                "baslik": "Kullanıcı Yönetimi",
                "aciklama": "Portföy sayfasından '+ Yeni Kişi' butonu ile birden fazla kişinin portföyünü takip edebilirsiniz. Her kullanıcının varlıkları ayrı ayrı saklanır."
            },
            {
                "ikon": "🌙",
                "baslik": "Tema Değiştirme",
                "aciklama": "Sol menünün altındaki 'Aydınlık/Karanlık' butonuyla tema değiştirebilirsiniz. Tercihleriniz otomatik kaydedilir."
            }
        ]
        
        for bilgi in kilavuz_bilgileri:
            # Her kılavuz kutusu
            kutu = ctk.CTkFrame(scroll, fg_color=("#f8f9fa", "#34495e"), corner_radius=12)
            kutu.pack(fill="x", padx=40, pady=10)
            
            ust_frame = ctk.CTkFrame(kutu, fg_color="transparent")
            ust_frame.pack(fill="x", padx=20, pady=(15, 5))
            
            ctk.CTkLabel(ust_frame, text=bilgi["ikon"], font=("Arial", 30)).pack(side="left", padx=(0, 15))
            ctk.CTkLabel(ust_frame, text=bilgi["baslik"], font=("Arial", 16, "bold"), 
                        text_color=RENK_TEXT_ANA, anchor="w").pack(side="left", fill="x", expand=True)
            
            ctk.CTkLabel(kutu, text=bilgi["aciklama"], font=("Arial", 12), 
                        text_color=RENK_TEXT_SILIK, wraplength=650, justify="left").pack(
                        fill="x", padx=20, pady=(5, 15), anchor="w")
        
        # Alt kısım - checkbox ve buton
        alt_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        alt_frame.pack(fill="x", padx=40, pady=(20, 30))
        
        self.chk_kilavuz_gosterme = ctk.CTkCheckBox(
            alt_frame, 
            text="Bir daha gösterme",
            font=("Arial", 13),
            text_color=RENK_TEXT_ANA,
            fg_color=RENK_MAVI,
            hover_color=RENK_YESIL
        )
        self.chk_kilavuz_gosterme.pack(pady=15)
        
        ctk.CTkButton(
            alt_frame, 
            text="UYGULAMAYA BAŞLA", 
            command=self.kullanim_kilavuzu_kapat,
            width=300, 
            height=50, 
            fg_color=RENK_YESIL, 
            hover_color="#27ae60",
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 20))
    
    def kullanim_kilavuzu_kapat(self):
        # Checkbox işaretliyse bir daha gösterme
        if self.chk_kilavuz_gosterme.get():
            self.data["__AYARLAR__"]["kullanim_kilavuzu_gosterilsin"] = False
            self.dosyaya_kaydet()
        
        # PIN kontrolü varsa ona git, yoksa ana ekrana
        if self.data["__AYARLAR__"].get("pin_aktif", False):
            self.giris_ekranini_goster()
        else:
            self.ana_ekrani_yukle()
    
    def giris_ekranini_goster(self):
        for w in self.container.winfo_children(): w.destroy()
        frame = ctk.CTkFrame(self.container, corner_radius=20, fg_color=RENK_KART_BG)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        ctk.CTkLabel(frame, text="🔒", font=("Arial", 50), text_color=RENK_TEXT_ANA).pack(pady=(30, 10))
        ctk.CTkLabel(frame, text="GÜVENLİ GİRİŞ", font=("Arial", 20, "bold"), text_color=RENK_TEXT_ANA).pack(pady=10)
        self.ent_pin = ctk.CTkEntry(frame, show="*", width=200, justify="center", fg_color=("white", "#2d3436"), text_color=RENK_TEXT_ANA)
        self.ent_pin.pack(pady=20, padx=40)
        self.ent_pin.bind('<Return>', lambda e: self.pin_kontrol())
        ctk.CTkButton(frame, text="GİRİŞ YAP", command=self.pin_kontrol, width=200, fg_color=RENK_MAVI).pack(pady=(0, 30), padx=40)

    def pin_kontrol(self):
        if self.ent_pin.get() == self.data["__AYARLAR__"]["pin"]: self.ana_ekrani_yukle()
        else: self.ent_pin.delete(0, "end"); self.ent_pin.configure(placeholder_text="HATALI PIN")

    def ana_ekrani_yukle(self):
        for w in self.container.winfo_children(): w.destroy()
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self.container, width=260, corner_radius=0, fg_color=RENK_SIDEBAR)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)  # Genişliği sabitle
        ctk.CTkLabel(self.sidebar, text="FİNANS PRO", font=("Arial", 28, "bold"), text_color="white").pack(pady=(40, 30))
        
        self.btn_home = self.menu_butonu(METINLER[self.dil]["ana_sayfa"], "home")
        self.btn_portfoy = ctk.CTkButton(self.sidebar, text=METINLER[self.dil]["portfoyum"], command=self.portfoy_sayfasina_git, height=50, fg_color="transparent", anchor="w", font=("Arial", 16), hover_color="#2c2f33", corner_radius=8, text_color=RENK_TEXT_SIDEBAR, compound="left", width=230)
        self.btn_portfoy.pack(fill="x", padx=15, pady=5)
        self.btn_piyasa = self.menu_butonu(METINLER[self.dil]["canli_piyasa"], "piyasa")
        self.btn_hesapla = self.menu_butonu(METINLER[self.dil]["hesap_makinesi"], "hesapla")
        self.btn_ayarlar = self.menu_butonu(METINLER[self.dil]["ayarlar"], "ayarlar")
        self.btn_hakkinda = self.menu_butonu(METINLER[self.dil]["hakkimizda"], "hakkinda")

        ctk.CTkFrame(self.sidebar, height=1, fg_color="gray40").pack(fill="x", padx=30, pady=20)
        
        # Dinamik linkler
        linkler = self.data["__AYARLAR__"].get("linkler", [])
        for link in linkler:
            ad = link.get("ad", "")
            url = link.get("url", "")
            if ad and url:
                btn = ctk.CTkButton(
                    self.sidebar, 
                    text=f"🔗  {ad}",
                    command=lambda u=url: webbrowser.open(u),
                    fg_color=("#3498db", "#2c3e50"),
                    hover_color=("#2980b9", "#34495e"),
                    text_color=("white", "#ecf0f1"),
                    font=("Arial", 13),
                    corner_radius=8,
                    height=38,
                    anchor="w"
                )
                btn.pack(fill="x", padx=15, pady=3)

        ctk.CTkFrame(self.sidebar, height=1, fg_color="gray40").pack(fill="x", padx=30, pady=20)
        self.switch_tema = ctk.CTkSwitch(self.sidebar, text=METINLER[self.dil]["aydinlik"], command=self.tema_degistir, onvalue="Dark", offvalue="Light", text_color="gray85")
        self.switch_tema.pack(fill="x", padx=30)
        if ctk.get_appearance_mode() == "Dark": self.switch_tema.select(); self.switch_tema.configure(text=METINLER[self.dil]["karanlik"])

        self.frm_alt = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.frm_alt.pack(side="bottom", fill="x", padx=20, pady=5)
        
        # İlk yüklemede piyasa verilerini göster
        if self.kurlar.get('dolar', 0) > 0:
            style = {"font": ("Arial", 12), "text_color": "gray80", "anchor": "w"}
            ctk.CTkLabel(self.frm_alt, text=METINLER[self.dil]["canli_piyasa_title"], font=("Arial", 10, "bold"), text_color="gray60", anchor="w").pack(fill="x", pady=(0,5))
            vals = [(METINLER[self.dil]["dolar"], self.kurlar['dolar']), (METINLER[self.dil]["euro"], self.kurlar['euro']), (METINLER[self.dil]["gram_altin"], self.kurlar['gram-altin'])]
            for ad, val in vals:
                ctk.CTkLabel(self.frm_alt, text=f"{ad}: {val:,.2f} TL" if val>0 else f"{ad}: --", **style).pack(fill="x")
        else:
            ctk.CTkLabel(self.frm_alt, text=METINLER[self.dil]["yukleniyor"], text_color="gray").pack()

        # Sağ Panel
        self.right_panel = ctk.CTkFrame(self.container, fg_color=RENK_MAIN_BG)
        self.right_panel.grid(row=0, column=1, sticky="nsew")
        self.sayfa_degistir("home")

    def menu_butonu(self, text, cmd):
        btn = ctk.CTkButton(self.sidebar, text=text, command=lambda: self.sayfa_degistir(cmd), height=50, fg_color="transparent", anchor="w", font=("Arial", 16), hover_color="#2c2f33", corner_radius=8, text_color=RENK_TEXT_SIDEBAR, compound="left")
        btn.pack(fill="x", padx=15, pady=5)
        btn.configure(width=230)  # Sabit genişlik
        return btn

    def sayfa_degistir(self, sayfa):
        self.aktif_sayfa = sayfa
        for w in self.right_panel.winfo_children(): w.destroy()
        
        # Sidebar her zaman göster
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=0)
        
        for btn, val in [(self.btn_home, "home"), (self.btn_portfoy, "portfoy"), (self.btn_piyasa, "piyasa"), (self.btn_hesapla, "hesapla"), (self.btn_ayarlar, "ayarlar"), (self.btn_hakkinda, "hakkinda")]:
            if val == sayfa: btn.configure(fg_color=RENK_AKTIF_BTN, text_color="white")
            else: btn.configure(fg_color="transparent", text_color=RENK_TEXT_SIDEBAR)
        
        if sayfa == "home": self.home_ekranini_ciz()
        elif sayfa == "portfoy": self.portfoy_ekranini_ciz()
        elif sayfa == "piyasa": self.piyasa_ekranini_ciz()
        elif sayfa == "hesapla": self.hesapla_ekranini_ciz()
        elif sayfa == "ayarlar": self.ayarlar_ekranini_ciz()
        elif sayfa == "hakkinda": self.hakkinda_ekranini_ciz()

    # --- SAYFALAR ---
    def home_ekranini_ciz(self):
        self.varlik_gizli = False  # Başlangıçta görünür
        
        kullanici_adi = self.data["__AYARLAR__"].get("kullanici_adi", "")
        karsilama = f"{METINLER[self.dil]['hos_geldiniz']} {kullanici_adi}" if kullanici_adi else METINLER[self.dil]["hos_geldiniz"]
        ctk.CTkLabel(self.right_panel, text=karsilama, font=("Arial", 24), text_color=RENK_TEXT_ANA).pack(pady=(40, 5))
        ctk.CTkLabel(self.right_panel, text=METINLER[self.dil]["finansal_durum"], font=("Arial", 32, "bold"), text_color=RENK_TEXT_ANA).pack(pady=(0, 30))
        
        toplam = 0
        kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
        
        # Son seçili kullanıcıyı al
        son_secili = self.data["__AYARLAR__"].get("son_secili_kullanici", "")
        secili_kullanici = ""
        
        if kullanicilar:
            if son_secili and son_secili in kullanicilar:
                secili_kullanici = son_secili
            else:
                secili_kullanici = kullanicilar[0]
            
            h = self.data[secili_kullanici]
            for t in ["varlik", "alacak"]:
                for k, v in h.get(t, {}).items():
                    if isinstance(v, dict) and "toplam" in v:
                        toplam += v["toplam"] * self.kurlar.get(k, 0)
                    else:
                        toplam += v * self.kurlar.get(k, 0)
            for k, v in h.get("borc", {}).items():
                if isinstance(v, dict) and "toplam" in v:
                    toplam -= v["toplam"] * self.kurlar.get(k, 0)
                else:
                    toplam -= v * self.kurlar.get(k, 0)

        self.home_card = ctk.CTkFrame(self.right_panel, fg_color=RENK_MAVI, width=450, height=200, corner_radius=20)
        self.home_card.pack(pady=10)
        ctk.CTkLabel(self.home_card, text=METINLER[self.dil]["toplam_net_varlik"], text_color="#dff9fb", font=("Arial", 14)).place(relx=0.5, rely=0.25, anchor="center")
        self.home_toplam_label = ctk.CTkLabel(self.home_card, text=f"{toplam:,.2f} TL", text_color="white", font=("Arial", 40, "bold"))
        self.home_toplam_label.place(relx=0.5, rely=0.55, anchor="center")
        
        # Kullanıcı adını göster
        self.home_kullanici_label = ctk.CTkLabel(self.home_card, text=f"{secili_kullanici} kişisine ait" if secili_kullanici else "", text_color="#dff9fb", font=("Arial", 11))
        self.home_kullanici_label.place(relx=0.5, rely=0.85, anchor="center")
        
        # Göster/Gizle butonu
        self.btn_goster_gizle = ctk.CTkButton(
            self.right_panel,
            text=METINLER[self.dil]["gizle"],
            command=self.varlik_goster_gizle,
            width=120,
            height=35,
            fg_color=("gray60", "gray40"),
            hover_color=("gray50", "gray30"),
            font=("Arial", 13)
        )
        self.btn_goster_gizle.pack(pady=(10, 20))

        grid = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        grid.pack(pady=50)
        def kb(p, t, i, c): ctk.CTkButton(p, text=f"{i}\n{t}", command=c, width=180, height=140, font=("Arial", 18, "bold"), fg_color=RENK_KART_BG, text_color=RENK_TEXT_ANA, hover_color=RENK_KART_HOVER).pack(side="left", padx=15)
        kb(grid, METINLER[self.dil]["portfoyum_kisa"], "💼", lambda: self.portfoy_sayfasina_git())
        kb(grid, METINLER[self.dil]["canli_piyasa_kisa"], "📈", lambda: self.sayfa_degistir("piyasa"))
        kb(grid, METINLER[self.dil]["hesap_makinesi_kisa"], "🧮", lambda: self.sayfa_degistir("hesapla"))
        kb(grid, METINLER[self.dil]["ayarlar_kisa"], "⚙️", lambda: self.sayfa_degistir("ayarlar"))
    
    def varlik_goster_gizle(self):
        self.varlik_gizli = not self.varlik_gizli
        
        if self.varlik_gizli:
            self.home_toplam_label.configure(text="**********")
            self.btn_goster_gizle.configure(text="👁️ Göster")
        else:
            # Toplamı yeniden hesapla ve göster
            self.home_verilerini_guncelle()
            self.btn_goster_gizle.configure(text="👁️ Gizle")
    
    def portfoy_sayfasina_git(self):
        # PIN kontrolü varsa PIN sor
        if self.data["__AYARLAR__"].get("pin_aktif", False):
            self.pin_portfoy_kontrol()
        else:
            self.sayfa_degistir("portfoy")
    
    def pin_portfoy_kontrol(self):
        pen = OzelGirisPenceresi(self, "PIN Kontrolü", "Portföy sayfasına erişmek için PIN giriniz:", sifreli=True, dil=self.dil)
        self.wait_window(pen)
        if pen.girilen_deger and pen.girilen_deger == self.data["__AYARLAR__"]["pin"]:
            self.sayfa_degistir("portfoy")
        else:
            if pen.girilen_deger:
                OzelUyariPenceresi(self, "Hata", "Yanlış PIN!", dil=self.dil)
    
    def home_verilerini_guncelle(self):
        if not hasattr(self, 'home_toplam_label') or not self.home_toplam_label.winfo_exists():
            return
        
        toplam = 0
        kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
        
        # Son seçili kullanıcıyı al
        son_secili = self.data["__AYARLAR__"].get("son_secili_kullanici", "")
        secili_kullanici = ""
        
        if kullanicilar:
            if son_secili and son_secili in kullanicilar:
                secili_kullanici = son_secili
            else:
                secili_kullanici = kullanicilar[0]
            
            h = self.data[secili_kullanici]
            for t in ["varlik", "alacak"]:
                for k, v in h.get(t, {}).items():
                    if isinstance(v, dict) and "toplam" in v:
                        toplam += v["toplam"] * self.kurlar.get(k, 0)
                    else:
                        toplam += v * self.kurlar.get(k, 0)
            for k, v in h.get("borc", {}).items():
                if isinstance(v, dict) and "toplam" in v:
                    toplam -= v["toplam"] * self.kurlar.get(k, 0)
                else:
                    toplam -= v * self.kurlar.get(k, 0)
        
        self.home_toplam_label.configure(text=f"{toplam:,.2f} TL")
        if hasattr(self, 'home_kullanici_label') and self.home_kullanici_label.winfo_exists():
            self.home_kullanici_label.configure(text=f"{secili_kullanici} kişisine ait" if secili_kullanici else "")

    def portfoy_ekranini_ciz(self):
        frm = ctk.CTkFrame(self.right_panel, fg_color=RENK_MAIN_BG)
        frm.pack(fill="x", padx=30, pady=(30,10))
        ctk.CTkLabel(frm, text=METINLER[self.dil]["portfoy_detaylari"], font=("Arial", 28, "bold"), text_color=RENK_TEXT_ANA).pack(side="left")
        
        ra = ctk.CTkFrame(frm, fg_color="transparent")
        ra.pack(side="right")
        kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
        
        # Sadece birden fazla kullanıcı varsa menüyü göster
        if len(kullanicilar) > 1:
            self.opt_kullanici = ctk.CTkOptionMenu(ra, values=kullanicilar, command=self.kullanici_degisti, fg_color=RENK_KART_BG, text_color=RENK_TEXT_ANA, button_color="gray")
            self.opt_kullanici.pack(side="left", padx=10)
            
            # Son seçili kullanıcıyı ayarla
            son_secili = self.data["__AYARLAR__"].get("son_secili_kullanici", "")
            if son_secili and son_secili in kullanicilar:
                self.opt_kullanici.set(son_secili)
            else:
                self.opt_kullanici.set(kullanicilar[0])
        else:
            # Tek kullanıcı varsa sadece ismini göster
            if kullanicilar:
                ctk.CTkLabel(ra, text=kullanicilar[0], font=("Arial", 16, "bold"), text_color=RENK_TEXT_ANA).pack(side="left", padx=10)
                self.opt_kullanici = None
        
        ctk.CTkButton(ra, text=METINLER[self.dil]["yeni_kisi"], command=self.kisi_ekle, width=100, fg_color=RENK_SIDEBAR).pack(side="left", padx=5)
        ctk.CTkButton(ra, text=METINLER[self.dil]["kisi_sil"], command=self.kisi_sil, width=100, fg_color=RENK_KIRMIZI).pack(side="left", padx=5)

        islem = ctk.CTkFrame(self.right_panel, fg_color=RENK_KART_BG, corner_radius=15)
        islem.pack(fill="x", padx=30, pady=10)
        ctk.CTkLabel(islem, text=METINLER[self.dil]["hizli_ekle"], font=("Arial", 14, "bold"), text_color=RENK_TEXT_ANA).pack(side="left", padx=20, pady=15)
        self.cmb_para = ctk.CTkComboBox(islem, values=list(ParaBirimleri.keys()), width=160, state="readonly")
        self.cmb_para.pack(side="left", padx=10, pady=15)
        self.tur_var = ctk.StringVar(value="varlik")
        ctk.CTkRadioButton(islem, text=METINLER[self.dil]["cuzdan"], variable=self.tur_var, value="varlik", text_color=RENK_TEXT_ANA, command=self.tur_degisti).pack(side="left", padx=10)
        ctk.CTkRadioButton(islem, text=METINLER[self.dil]["borc"], variable=self.tur_var, value="borc", text_color=RENK_TEXT_ANA, command=self.tur_degisti).pack(side="left", padx=10)
        ctk.CTkRadioButton(islem, text=METINLER[self.dil]["alacak"], variable=self.tur_var, value="alacak", text_color=RENK_TEXT_ANA, command=self.tur_degisti).pack(side="left", padx=10)
        
        self.ent_isim = ctk.CTkEntry(islem, placeholder_text="Kime/Kimden", width=120, fg_color=("white", "#2d3436"), text_color=RENK_TEXT_ANA)
        self.ent_isim.pack(side="left", padx=5)
        self.ent_isim.pack_forget()  # Başlangıçta gizli
        
        self.ent_miktar = ctk.CTkEntry(islem, placeholder_text="Miktar", width=100, fg_color=("white", "#2d3436"), text_color=RENK_TEXT_ANA)
        self.ent_miktar.pack(side="left", padx=10)
        ctk.CTkButton(islem, text=METINLER[self.dil]["islem_kaydet"], command=self.islem_kaydet, width=140, fg_color=RENK_YESIL).pack(side="left", padx=20)

        self.scroll_portfoy = ctk.CTkScrollableFrame(self.right_panel, fg_color="transparent")
        self.scroll_portfoy.pack(fill="both", expand=True, padx=30, pady=20)
        self.dashboard_guncelle()

    def piyasa_ekranini_ciz(self):
        ctk.CTkLabel(self.right_panel, text="Canlı Piyasa", font=("Arial", 28, "bold"), text_color=RENK_TEXT_ANA).pack(padx=30, pady=(30, 20), anchor="w")
        h = ctk.CTkFrame(self.right_panel, height=40, fg_color=RENK_KART_BG)
        h.pack(fill="x", padx=30)
        ctk.CTkLabel(h, text="VARLIK", width=250, anchor="w", text_color=RENK_TEXT_ANA, font=("Arial", 12, "bold")).pack(side="left", padx=20)
        ctk.CTkLabel(h, text="DEĞİŞİM", width=100, anchor="center", text_color=RENK_TEXT_ANA, font=("Arial", 12, "bold")).pack(side="right", padx=10)
        ctk.CTkLabel(h, text="SATIŞ", width=120, anchor="e", text_color=RENK_TEXT_ANA, font=("Arial", 12, "bold")).pack(side="right", padx=10)
        ctk.CTkLabel(h, text="ALIŞ", width=120, anchor="e", text_color=RENK_TEXT_ANA, font=("Arial", 12, "bold")).pack(side="right", padx=10)

        self.scroll_piyasa = ctk.CTkScrollableFrame(self.right_panel, fg_color="transparent")
        self.scroll_piyasa.pack(fill="both", expand=True, padx=30, pady=10)
        self.piyasa_verilerini_goster()
        
        ctk.CTkButton(self.right_panel, text="⟳ Yenile", command=self.verileri_arkada_guncelle, fg_color="gray", width=150).pack(pady=20)
    
    def piyasa_verilerini_goster(self):
        if not hasattr(self, 'scroll_piyasa') or not self.scroll_piyasa.winfo_exists():
            return
        
        # Önce mevcut içeriği temizle
        for widget in self.scroll_piyasa.winfo_children():
            widget.destroy()
        
        if not self.piyasa_tablosu:
            ctk.CTkLabel(self.scroll_piyasa, text="Veriler Yükleniyor...", text_color="gray").pack(pady=20)
        else:
            for i, item in enumerate(self.piyasa_tablosu):
                row = ctk.CTkFrame(self.scroll_piyasa, fg_color=RENK_KART_BG)
                row.pack(fill="x", pady=3)
                ctk.CTkLabel(row, text=item["isim"], width=250, anchor="w", text_color=RENK_TEXT_ANA, font=("Arial", 13, "bold")).pack(side="left", padx=20, pady=12)
                degisim = str(item["degisim"])
                renk = RENK_YESIL if "%" in degisim and "-" not in degisim else RENK_KIRMIZI
                if degisim == "-": renk = "gray"
                ctk.CTkLabel(row, text=degisim, width=100, anchor="center", text_color=renk, font=("Arial", 12, "bold")).pack(side="right", padx=10)
                ctk.CTkLabel(row, text=f"{item['satis']:,.2f}", width=120, anchor="e", text_color=RENK_TEXT_ANA).pack(side="right", padx=10)
                ctk.CTkLabel(row, text=f"{item['alis']:,.2f}", width=120, anchor="e", text_color=RENK_TEXT_SILIK).pack(side="right", padx=10)

    def hesapla_ekranini_ciz(self):
        ctk.CTkLabel(self.right_panel, text="Hesap Makinesi", font=("Arial", 28, "bold"), text_color=RENK_TEXT_ANA).pack(padx=30, pady=(30, 20), anchor="w")
        
        calc_frame = ctk.CTkFrame(self.right_panel, fg_color=RENK_KART_BG, corner_radius=20)
        calc_frame.pack(padx=100, pady=30)
        
        self.calc_display = ctk.CTkEntry(calc_frame, width=350, height=70, font=("Arial", 32, "bold"), justify="right", fg_color=("#34495e", "#1a1a1a"), text_color="white", border_width=0)
        self.calc_display.pack(padx=20, pady=(20, 10))
        self.calc_display.insert(0, "0")
        self.calc_display.focus()
        self.calc_display.bind('<Key>', self.calc_keyboard_input)
        self.calc_expression = ""
        self.calc_first_input = True  # İlk girdi için bayrak
        
        buttons_frame = ctk.CTkFrame(calc_frame, fg_color="transparent")
        buttons_frame.pack(padx=20, pady=(10, 20))
        
        buttons = [
            ['', '', '', '⌫'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for i, row in enumerate(buttons):
            row_frame = ctk.CTkFrame(buttons_frame, fg_color="transparent")
            row_frame.pack(pady=5)
            for btn_text in row:
                if btn_text == '':  # Boş buton
                    ctk.CTkFrame(row_frame, width=80, height=60, fg_color="transparent").pack(side="left", padx=5)
                    continue
                color = RENK_KIRMIZI if btn_text == 'C' else (RENK_YESIL if btn_text == '=' else (RENK_SARI if btn_text == '⌫' else (RENK_MAVI if btn_text in ['+', '-', '*', '/'] else "#34495e")))
                hover = "#c0392b" if btn_text == 'C' else ("#27ae60" if btn_text == '=' else ("#f39c12" if btn_text == '⌫' else ("#2980b9" if btn_text in ['+', '-', '*', '/'] else "#2c3e50")))
                btn = ctk.CTkButton(row_frame, text=btn_text, width=80, height=60, font=("Arial", 24, "bold"), 
                                  fg_color=color, hover_color=hover, corner_radius=10,
                                  command=lambda t=btn_text: self.calc_button_click(t))
                btn.pack(side="left", padx=5)
    
    def calc_button_click(self, char):
        current = self.calc_display.get()
        
        if char == 'C':
            self.calc_display.delete(0, "end")
            self.calc_display.insert(0, "0")
            self.calc_expression = ""
            self.calc_first_input = True
        elif char == '⌫':  # Backspace
            if len(self.calc_expression) > 0:
                self.calc_expression = self.calc_expression[:-1]
                self.calc_display.delete(0, "end")
                if self.calc_expression:
                    self.calc_display.insert(0, self.calc_expression)
                else:
                    self.calc_display.insert(0, "0")
                    self.calc_first_input = True
        elif char == '=':
            try:
                result = eval(self.calc_expression)
                self.calc_display.delete(0, "end")
                self.calc_display.insert(0, str(result))
                self.calc_expression = str(result)
                self.calc_first_input = False
            except:
                self.calc_display.delete(0, "end")
                self.calc_display.insert(0, "HATA")
                self.calc_expression = ""
                self.calc_first_input = True
        else:
            # İlk girdi veya sonuç sonrası ise expression'ı sıfırla
            if self.calc_first_input or current == "0" or current == "HATA":
                self.calc_expression = char
                self.calc_first_input = False
            else:
                self.calc_expression += char
            
            self.calc_display.delete(0, "end")
            self.calc_display.insert(0, self.calc_expression)
    
    def calc_keyboard_input(self, event):
        char = event.char
        # Backspace tuşu
        if event.keysym == 'BackSpace':
            self.calc_button_click('⌫')
            return "break"
        # Sadece geçerli karakterleri kabul et
        if char in '0123456789+-*/':
            self.calc_button_click(char)
            return "break"  # Varsayılan davranışı engelle
        elif char == '\r' or char == '=':  # Enter veya =
            self.calc_button_click('=')
            return "break"
        elif char.lower() == 'c':
            self.calc_button_click('C')
            return "break"
        return "break"  # Diğer tuşları engelle

    def ayarlar_ekranini_ciz(self):
        ctk.CTkLabel(self.right_panel, text=METINLER[self.dil]["ayarlar_title"], font=("Arial", 28, "bold"), text_color=RENK_TEXT_ANA).pack(padx=30, pady=(30, 20), anchor="w")
        
        # Scrollable frame ekle
        frm = ctk.CTkScrollableFrame(self.right_panel, fg_color=RENK_KART_BG, corner_radius=15)
        frm.pack(fill="both", expand=True, padx=30, pady=(0, 10))

        ctk.CTkLabel(frm, text=METINLER[self.dil]["guvenlik"], font=("Arial", 16, "bold"), text_color=RENK_SIDEBAR).pack(anchor="w", padx=30, pady=(30,10))
        
        # Kullanıcı Adı
        kullanici_frame = ctk.CTkFrame(frm, fg_color=("white", "#34495e"), corner_radius=10)
        kullanici_frame.pack(fill="x", padx=30, pady=(0,15))
        kullanici_inner = ctk.CTkFrame(kullanici_frame, fg_color="transparent")
        kullanici_inner.pack(pady=15, padx=20, fill="x")
        ctk.CTkLabel(kullanici_inner, text=METINLER[self.dil]["kullanici_bilgileri"], font=("Arial", 14, "bold"), text_color=RENK_TEXT_ANA).pack(anchor="w", pady=(0,10))
        ad_frame = ctk.CTkFrame(kullanici_inner, fg_color="transparent")
        ad_frame.pack(fill="x")
        ctk.CTkLabel(ad_frame, text=METINLER[self.dil]["ad_soyad"], text_color=RENK_TEXT_SILIK, font=("Arial", 12), width=80, anchor="w").pack(side="left")
        self.ent_kullanici_adi_ayar = ctk.CTkEntry(ad_frame, fg_color=("#f1f2f6", "#2d3436"), text_color=RENK_TEXT_ANA, border_width=0, height=35)
        self.ent_kullanici_adi_ayar.pack(side="left", fill="x", expand=True)
        self.ent_kullanici_adi_ayar.insert(0, self.data["__AYARLAR__"].get("kullanici_adi", ""))
        
        self.switch_pin = ctk.CTkSwitch(frm, text=METINLER[self.dil]["sifre_sor"], progress_color=RENK_YESIL, text_color=RENK_TEXT_ANA)
        self.switch_pin.pack(anchor="w", padx=30, pady=5)
        if self.data["__AYARLAR__"].get("pin_aktif", False): self.switch_pin.select()
        
        pin_frame = ctk.CTkFrame(frm, fg_color=("white", "#34495e"), corner_radius=10)
        pin_frame.pack(fill="x", padx=30, pady=15)
        
        pin_inner = ctk.CTkFrame(pin_frame, fg_color="transparent")
        pin_inner.pack(pady=15, padx=20)
        
        ctk.CTkLabel(pin_inner, text=METINLER[self.dil]["pin_kodu"], font=("Arial", 14, "bold"), text_color=RENK_TEXT_ANA).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,10))
        ctk.CTkLabel(pin_inner, text=METINLER[self.dil]["mevcut"], text_color=RENK_TEXT_SILIK, font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0,10))
        self.lbl_pin_goruntule = ctk.CTkLabel(pin_inner, text="••••••", text_color=RENK_TEXT_ANA, font=("Arial", 14, "bold"))
        self.lbl_pin_goruntule.grid(row=1, column=1, sticky="w")
        
        btn_frame = ctk.CTkFrame(pin_inner, fg_color="transparent")
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(10,0))
        ctk.CTkButton(btn_frame, text=METINLER[self.dil]["goster"], width=100, command=self.pin_goster, fg_color="#3498db", hover_color="#2980b9").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text=METINLER[self.dil]["degistir"], width=100, command=self.pin_degistir, fg_color=RENK_YESIL, hover_color="#27ae60").pack(side="left", padx=5)

        ctk.CTkLabel(frm, text=METINLER[self.dil]["menu_kisayollari"], font=("Arial", 16, "bold"), text_color=RENK_SIDEBAR).pack(anchor="w", padx=30, pady=(30,10))
        
        # Link listesi scroll
        self.link_scroll = ctk.CTkScrollableFrame(frm, fg_color="transparent", height=200)
        self.link_scroll.pack(fill="x", padx=30, pady=10)
        
        self.link_entries = []
        linkler = self.data["__AYARLAR__"].get("linkler", [])
        
        for i, link in enumerate(linkler):
            self.link_satiri_ekle(i, link.get("ad", ""), link.get("url", ""))
        
        # Yeni link ekleme butonu
        ctk.CTkButton(
            frm, 
            text=METINLER[self.dil]["yeni_link_ekle"], 
            command=self.yeni_link_satiri,
            height=35,
            fg_color=("#3498db", "#2c3e50"),
            hover_color=("#2980b9", "#34495e")
        ).pack(padx=30, pady=(10,20), anchor="w")
        
        # DİL SEÇİMİ
        ctk.CTkLabel(frm, text=METINLER[self.dil]["dil_secimi"], font=("Arial", 16, "bold"), text_color=RENK_SIDEBAR).pack(anchor="w", padx=30, pady=(30,10))
        
        dil_frame = ctk.CTkFrame(frm, fg_color=("white", "#34495e"), corner_radius=10)
        dil_frame.pack(fill="x", padx=30, pady=(0,15))
        dil_inner = ctk.CTkFrame(dil_frame, fg_color="transparent")
        dil_inner.pack(pady=15, padx=20, fill="x")
        
        self.dil_var = ctk.StringVar(value=self.dil)
        dil_radio_frame = ctk.CTkFrame(dil_inner, fg_color="transparent")
        dil_radio_frame.pack(anchor="w")
        
        ctk.CTkRadioButton(
            dil_radio_frame, 
            text="🇹🇷 Türkçe", 
            variable=self.dil_var, 
            value="tr", 
            text_color=RENK_TEXT_ANA,
            font=("Arial", 14)
        ).pack(side="left", padx=(0,20))
        
        ctk.CTkRadioButton(
            dil_radio_frame, 
            text="🇬🇧 English", 
            variable=self.dil_var, 
            value="en", 
            text_color=RENK_TEXT_ANA,
            font=("Arial", 14)
        ).pack(side="left")
        
        ctk.CTkButton(frm, text=METINLER[self.dil]["ayarlari_kaydet"], command=self.ayarlari_kaydet, height=45, fg_color=RENK_YESIL, hover_color="#27ae60", font=("Arial", 14, "bold")).pack(pady=(40,30), padx=30, fill="x")
        
        # Sıfırlama butonu
        ctk.CTkButton(
            frm, 
            text=METINLER[self.dil]["tum_verileri_sifirla"], 
            command=self.verileri_sifirla_onayla,
            height=45, 
            fg_color=RENK_KIRMIZI, 
            hover_color="#c0392b", 
            font=("Arial", 14, "bold"),
            text_color="white"
        ).pack(pady=(0,30), padx=30, fill="x")

    def hakkinda_ekranini_ciz(self):
        ctk.CTkLabel(self.right_panel, text="Hakkımızda", font=("Arial", 32, "bold"), text_color=RENK_TEXT_ANA).pack(pady=(40, 30))
        
        scroll = ctk.CTkScrollableFrame(self.right_panel, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=40, pady=(0,40))
        
        # Uygulama Bilgisi
        app_frame = ctk.CTkFrame(scroll, fg_color=("#f8f9fa", "#34495e"), corner_radius=15)
        app_frame.pack(fill="x", pady=(0,20))
        
        app_inner = ctk.CTkFrame(app_frame, fg_color="transparent")
        app_inner.pack(pady=30, padx=30, fill="x")
        
        ctk.CTkLabel(
            app_inner, 
            text="💼 Finans Pro 1.0", 
            font=("Arial", 28, "bold"), 
            text_color=RENK_TEXT_ANA
        ).pack(anchor="w", pady=(0,15))
        
        ctk.CTkLabel(
            app_inner, 
            text="Kişisel finans yönetimi için geliştirilmiş modern bir uygulama. TL, döviz, altın, kripto para takibi, " +
                 "borç/alacak yönetimi, canlı piyasa verileri ve daha fazlası...",
            font=("Arial", 13), 
            text_color=RENK_TEXT_SILIK,
            wraplength=700,
            justify="left"
        ).pack(anchor="w")
        
        # Geliştiriciler
        dev_header = ctk.CTkFrame(scroll, fg_color="transparent")
        dev_header.pack(fill="x", pady=(10,15))
        
        ctk.CTkLabel(
            dev_header, 
            text="👨‍💻 Geliştiriciler", 
            font=("Arial", 22, "bold"), 
            text_color=RENK_TEXT_ANA
        ).pack(anchor="w")
        
        # Samet Can Ceylan
        dev1_frame = ctk.CTkFrame(scroll, fg_color=("white", "#2d3436"), corner_radius=12)
        dev1_frame.pack(fill="x", pady=(0,15))
        dev1_inner = ctk.CTkFrame(dev1_frame, fg_color="transparent")
        dev1_inner.pack(pady=20, padx=25, fill="x")
        
        ctk.CTkLabel(dev1_inner, text="Samet Can Ceylan", font=("Arial", 20, "bold"), text_color=RENK_TEXT_ANA).pack(anchor="w")
        email1 = ctk.CTkLabel(dev1_inner, text="📧 sametcanceylan@icloud.com", font=("Arial", 15), text_color=RENK_MAVI, cursor="hand2")
        email1.pack(anchor="w", pady=(8,0))
        email1.bind("<Button-1>", lambda e: webbrowser.open("mailto:sametcanceylan@icloud.com"))
        
        # Sosyal medya butonları - Samet
        social1_frame = ctk.CTkFrame(dev1_inner, fg_color="transparent")
        social1_frame.pack(anchor="w", pady=(12,0))
        
        linkedin1_btn = ctk.CTkButton(
            social1_frame,
            text="🔗 LinkedIn",
            command=lambda: webbrowser.open("https://www.linkedin.com/in/sametcanceylan"),
            fg_color=("#0077b5", "#0077b5"),
            hover_color=("#005885", "#005885"),
            width=120,
            height=32,
            font=("Arial", 12)
        )
        linkedin1_btn.pack(side="left", padx=(0,10))
        
        instagram1_btn = ctk.CTkButton(
            social1_frame,
            text="📸 Instagram",
            command=lambda: webbrowser.open("https://www.instagram.com/mrdancheva/"),
            fg_color=("#E1306C", "#E1306C"),
            hover_color=("#C13584", "#C13584"),
            width=120,
            height=32,
            font=("Arial", 12)
        )
        instagram1_btn.pack(side="left")
        
        # Buse Nur Çalı
        dev2_frame = ctk.CTkFrame(scroll, fg_color=("white", "#2d3436"), corner_radius=12)
        dev2_frame.pack(fill="x", pady=(0,15))
        dev2_inner = ctk.CTkFrame(dev2_frame, fg_color="transparent")
        dev2_inner.pack(pady=20, padx=25, fill="x")
        
        ctk.CTkLabel(dev2_inner, text="Buse Nur Çalı", font=("Arial", 20, "bold"), text_color=RENK_TEXT_ANA).pack(anchor="w")
        email2 = ctk.CTkLabel(dev2_inner, text="📧 busenurcali16@gmail.com", font=("Arial", 15), text_color=RENK_MAVI, cursor="hand2")
        email2.pack(anchor="w", pady=(8,0))
        email2.bind("<Button-1>", lambda e: webbrowser.open("mailto:busenurcali16@gmail.com"))
        
        # Sosyal medya butonları - Buse
        social2_frame = ctk.CTkFrame(dev2_inner, fg_color="transparent")
        social2_frame.pack(anchor="w", pady=(12,0))
        
        linkedin2_btn = ctk.CTkButton(
            social2_frame,
            text="🔗 LinkedIn",
            command=lambda: webbrowser.open("https://www.linkedin.com/in/buse-nur-çalı-0b1b60224"),
            fg_color=("#0077b5", "#0077b5"),
            hover_color=("#005885", "#005885"),
            width=120,
            height=32,
            font=("Arial", 12)
        )
        linkedin2_btn.pack(side="left", padx=(0,10))
        
        instagram2_btn = ctk.CTkButton(
            social2_frame,
            text="📸 Instagram",
            command=lambda: webbrowser.open("https://www.instagram.com/busenrcl/"),
            fg_color=("#E1306C", "#E1306C"),
            hover_color=("#C13584", "#C13584"),
            width=120,
            height=32,
            font=("Arial", 12)
        )
        instagram2_btn.pack(side="left")
        
        # Alt bilgi
        footer = ctk.CTkFrame(scroll, fg_color="transparent")
        footer.pack(fill="x", pady=(30,20))
        
        ctk.CTkLabel(
            footer, 
            text="© 2025 Finans Pro. Tüm hakları saklıdır.", 
            font=("Arial", 12), 
            text_color=RENK_TEXT_SILIK
        ).pack(anchor="center")

    def link_satiri_ekle(self, index, ad="", url=""):
        satir = ctk.CTkFrame(self.link_scroll, fg_color=("#ecf0f1", "#2d3436"), corner_radius=8)
        satir.pack(fill="x", pady=5)
        
        ent_ad = ctk.CTkEntry(satir, width=150, placeholder_text="Link Adı", fg_color=("white", "#34495e"), text_color=RENK_TEXT_ANA, border_width=0)
        ent_ad.pack(side="left", padx=10, pady=10)
        if ad: ent_ad.insert(0, ad)
        
        ent_url = ctk.CTkEntry(satir, placeholder_text="https://ornek.com", fg_color=("white", "#34495e"), text_color=RENK_TEXT_ANA, border_width=0)
        ent_url.pack(side="left", padx=5, pady=10, fill="x", expand=True)
        if url: ent_url.insert(0, url)
        
        btn_sil = ctk.CTkButton(
            satir, 
            text="🗑", 
            width=45,
            height=35,
            fg_color=RENK_KIRMIZI,
            hover_color="#c0392b",
            font=("Arial", 18),
            command=lambda: self.link_satiri_sil(satir, ent_ad, ent_url)
        )
        btn_sil.pack(side="right", padx=10, pady=10)
        
        self.link_entries.append({"frame": satir, "ad": ent_ad, "url": ent_url})
    
    def yeni_link_satiri(self):
        index = len(self.link_entries)
        self.link_satiri_ekle(index)
    
    def link_satiri_sil(self, frame, ent_ad, ent_url):
        frame.destroy()
        self.link_entries = [e for e in self.link_entries if e["frame"] != frame]
    
    def ayarlari_kaydet(self):
        # PIN kontrolü - PIN aktifse önce şifre sor
        if self.data["__AYARLAR__"].get("pin_aktif", False):
            pen = OzelGirisPenceresi(self, "🔒 PIN Kontrolü", "Ayarları kaydetmek için PIN giriniz:", sifreli=True, dil=self.dil)
            self.wait_window(pen)
            # PIN yanlış veya iptal edildi mi?
            if not pen.girilen_deger:
                # İptal edildi
                return
            if pen.girilen_deger != self.data["__AYARLAR__"]["pin"]:
                # Yanlış PIN
                OzelUyariPenceresi(self, "Hata", "Yanlış PIN! Ayarlar kaydedilmedi.", dil=self.dil)
                return
        
        # Ayarları al
        pin_aktif = bool(self.switch_pin.get())
        kullanici_adi = self.ent_kullanici_adi_ayar.get().strip()
        
        if not kullanici_adi:
            OzelUyariPenceresi(self, "Hata", "Kullanıcı adı boş bırakılamaz!", dil=self.dil)
            return
        
        # Linkleri topla
        linkler = []
        for entry in self.link_entries:
            ad = entry["ad"].get().strip()
            url = entry["url"].get().strip()
            if ad and url:
                linkler.append({"ad": ad, "url": url})
        
        # Dil değişikliği kontrol
        yeni_dil = self.dil_var.get()
        dil_degisti = (yeni_dil != self.dil)
        
        # PIN aktif durumunu kaydet
        self.data["__AYARLAR__"]["pin_aktif"] = pin_aktif
        self.data["__AYARLAR__"]["kullanici_adi"] = kullanici_adi
        self.data["__AYARLAR__"]["linkler"] = linkler
        self.data["__AYARLAR__"]["dil"] = yeni_dil
        
        self.dosyaya_kaydet()
        
        # Dil değiştiyse uygulamayı yeniden yükle
        if dil_degisti:
            self.dil = yeni_dil
            OzelUyariPenceresi(self, "Başarılı", "Dil değiştirildi. Lütfen uygulamayı yeniden başlatın.", "bilgi", dil=self.dil)
            self.quit()  # Uygulamayı kapat, kullanıcı tekrar açacak
        else:
            OzelUyariPenceresi(self, "Başarılı", "Ayarlar kaydedildi.", "bilgi", dil=self.dil)
            self.ana_ekrani_yukle()
    
    def verileri_sifirla_onayla(self):
        # Onay penceresi
        onay_penceresi = ctk.CTkToplevel(self)
        onay_penceresi.title("⚠️ Tehlikeli İşlem")
        onay_penceresi.geometry("450x280")
        onay_penceresi.configure(fg_color=RENK_MAIN_BG)
        onay_penceresi.attributes("-topmost", True)
        onay_penceresi.resizable(False, False)
        
        # Pencereyi ortala
        onay_penceresi.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() // 2) - 225
        y = self.winfo_y() + (self.winfo_height() // 2) - 140
        onay_penceresi.geometry(f"+{x}+{y}")
        
        # İçerik
        ctk.CTkLabel(
            onay_penceresi, 
            text="⚠️", 
            font=("Arial", 60), 
            text_color=RENK_KIRMIZI
        ).pack(pady=(30, 10))
        
        ctk.CTkLabel(
            onay_penceresi, 
            text="ONAYLIYOR MUSUNUZ?", 
            font=("Arial", 18, "bold"), 
            text_color=RENK_TEXT_ANA
        ).pack(pady=5)
        
        ctk.CTkLabel(
            onay_penceresi, 
            text="Bu işlem geri alınamaz.\nTüm kullanıcılar, varlıklar, borçlar ve\nalacaklar silinecektir.", 
            font=("Arial", 12), 
            text_color=RENK_TEXT_SILIK,
            justify="center"
        ).pack(pady=10)
        
        # Butonlar
        btn_frame = ctk.CTkFrame(onay_penceresi, fg_color="transparent")
        btn_frame.pack(pady=20)
        
        ctk.CTkButton(
            btn_frame, 
            text="❌ İptal", 
            command=onay_penceresi.destroy,
            width=120,
            height=40,
            fg_color=("gray60", "gray40"),
            hover_color=("gray50", "gray30"),
            font=("Arial", 13, "bold")
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame, 
            text="✅ Evet, Sil", 
            command=lambda: [onay_penceresi.destroy(), self.verileri_tamamen_sifirla()],
            width=120,
            height=40,
            fg_color=RENK_KIRMIZI,
            hover_color="#c0392b",
            font=("Arial", 13, "bold")
        ).pack(side="left", padx=10)
    
    def verileri_tamamen_sifirla(self):
        # JSON dosyasını varsayılan ayarlarla sıfırla
        self.data = {
            "__AYARLAR__": {
                "pin_aktif": False, 
                "pin": "123456",
                "kullanici_adi": "",
                "kullanim_kilavuzu_gosterilsin": True,
                "linkler": [
                    {"ad": "Altınkaynak", "url": "https://www.altinkaynak.com"},
                    {"ad": "Döviz.com", "url": "https://www.doviz.com"}
                ]
            }
        }
        self.dosyaya_kaydet()
        
        # Başarı mesajı
        OzelUyariPenceresi(self, "Başarılı", "Tüm veriler sıfırlandı.\nUygulama yeniden başlatılacak.", "bilgi", dil=self.dil)
        
        # Uygulamayı yeniden başlat
        self.after(1500, self.yeniden_baslat)
    
    def yeniden_baslat(self):
        self.destroy()
        yeni_uygulama = FinansProApp()
        yeni_uygulama.mainloop()

    def pin_goster(self):
        if self.lbl_pin_goruntule.cget("text") == "••••••":
            self.lbl_pin_goruntule.configure(text=self.data["__AYARLAR__"]["pin"])
        else:
            self.lbl_pin_goruntule.configure(text="••••••")
    
    def pin_degistir(self):
        pen = OzelGirisPenceresi(self, "PIN Değiştir", "Yeni PIN giriniz (min 4 hane):", sifreli=True, dil=self.dil)
        self.wait_window(pen)
        yeni_pin = pen.girilen_deger
        if yeni_pin and len(yeni_pin) >= 4:
            self.data["__AYARLAR__"]["pin"] = yeni_pin
            self.dosyaya_kaydet()
            self.lbl_pin_goruntule.configure(text="••••••")
            OzelUyariPenceresi(self, "Başarılı", "PIN başarıyla değiştirildi!", "bilgi", dil=self.dil)
        elif yeni_pin:
            OzelUyariPenceresi(self, "Hata", "PIN en az 4 haneli olmalı!", dil=self.dil)

    def kisi_listesini_yukle(self):
        isimler = [k for k in self.data.keys() if k != "__AYARLAR__"]
        self.opt_kullanici.configure(values=isimler)
        if isimler:
            self.opt_kullanici.set(isimler[0])
            self.dashboard_guncelle()

    def kisi_ekle(self):
        pen = OzelGirisPenceresi(self, "Yeni Kişi", "İsim giriniz:", dil=self.dil)
        self.wait_window(pen)
        ad = pen.girilen_deger
        if not ad:
            return
        
        # Küçük harfe çevirip kontrol et
        ad_lower = ad.lower()
        mevcut_isimler = [k.lower() for k in self.data.keys() if k != "__AYARLAR__"]
        
        if ad_lower in mevcut_isimler:
            OzelUyariPenceresi(self, "Hata", f"Bu isimde bir kullanıcı zaten mevcut!\n(Büyük/küçük harf farkı gözetilmez)", dil=self.dil)
            return
        
        # Orijinal haliyle kaydet
        self.data[ad] = {"varlik": {}, "borc": {}, "alacak": {}}
        self.dosyaya_kaydet()
        self.sayfa_degistir("portfoy")
        self.opt_kullanici.set(ad)
        self.dashboard_guncelle()

    def kisi_sil(self):
        if self.opt_kullanici:
            kisi = self.opt_kullanici.get()
        else:
            kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
            kisi = kullanicilar[0] if kullanicilar else None
        if not kisi or kisi not in self.data:
            OzelUyariPenceresi(self, "Hata", "Silinecek kişi seçiniz!", dil=self.dil)
            return
        pen = OzelGirisPenceresi(self, "Onay", f"{kisi} kişisini silmek için adını yazın:", dil=self.dil)
        self.wait_window(pen)
        if pen.girilen_deger == kisi:
            del self.data[kisi]
            self.dosyaya_kaydet()
            self.sayfa_degistir("portfoy")
        else:
            OzelUyariPenceresi(self, "Hata", "İsim eşleşmedi, silme iptal edildi.", dil=self.dil)

    def bakiye_duzenle(self, tur, kod):
        if self.opt_kullanici:
            kisi = self.opt_kullanici.get()
        else:
            kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
            kisi = kullanicilar[0] if kullanicilar else None
        if not kisi or kisi not in self.data: return
        mevcut = self.data[kisi].get(tur, {}).get(kod, 0)
        pen = OzelGirisPenceresi(self, "Bakiye Düzenle", f"{kod.upper()} için yeni miktar giriniz:\n(Mevcut: {mevcut:.2f})", dil=self.dil)
        self.wait_window(pen)
        try:
            yeni = float(pen.girilen_deger.replace(",", "."))
            if yeni < 0: yeni = 0
            if tur not in self.data[kisi]: self.data[kisi][tur] = {}
            self.data[kisi][tur][kod] = yeni
            self.dosyaya_kaydet()
            self.dashboard_guncelle()
        except:
            if pen.girilen_deger: OzelUyariPenceresi(self, "Hata", "Geçerli bir sayı giriniz!", dil=self.dil)

    def bakiye_sil(self, tur, kod):
        if self.opt_kullanici:
            kisi = self.opt_kullanici.get()
        else:
            kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
            kisi = kullanicilar[0] if kullanicilar else None
        if not kisi or kisi not in self.data: return
        
        # Basit onay penceresi
        onay_penceresi = ctk.CTkToplevel(self)
        onay_penceresi.title("Onay")
        onay_penceresi.geometry("400x200")
        onay_penceresi.configure(fg_color=RENK_MAIN_BG)
        onay_penceresi.attributes("-topmost", True)
        onay_penceresi.resizable(False, False)
        
        # Pencereyi ortala
        onay_penceresi.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() // 2) - 200
        y = self.winfo_y() + (self.winfo_height() // 2) - 100
        onay_penceresi.geometry(f"+{x}+{y}")
        
        # İçerik
        ctk.CTkLabel(
            onay_penceresi, 
            text=f"{kod.upper()} bakiyesini silmek istediğinize emin misiniz?", 
            font=("Arial", 14), 
            text_color=RENK_TEXT_ANA,
            wraplength=350
        ).pack(pady=30, padx=20)
        
        # Butonlar
        btn_frame = ctk.CTkFrame(onay_penceresi, fg_color="transparent")
        btn_frame.pack(pady=20)
        
        def iptal():
            onay_penceresi.destroy()
        
        def onayla():
            if tur in self.data[kisi] and kod in self.data[kisi][tur]:
                del self.data[kisi][tur][kod]
                self.dosyaya_kaydet()
                self.dashboard_guncelle()
            onay_penceresi.destroy()
        
        ctk.CTkButton(
            btn_frame, 
            text="❌ İptal", 
            command=iptal,
            width=120,
            height=40,
            fg_color=("gray60", "gray40"),
            hover_color=("gray50", "gray30"),
            font=("Arial", 13, "bold")
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame, 
            text="✅ Evet, Sil", 
            command=onayla,
            width=120,
            height=40,
            fg_color=RENK_KIRMIZI,
            hover_color="#c0392b",
            font=("Arial", 13, "bold")
        ).pack(side="left", padx=10)

    def kullanici_degisti(self, secilen):
        # Seçilen kullanıcıyı kaydet
        self.data["__AYARLAR__"]["son_secili_kullanici"] = secilen
        self.dosyaya_kaydet()
        self.dashboard_guncelle()
    
    def tur_degisti(self):
        tur = self.tur_var.get()
        if tur in ["borc", "alacak"]:
            self.ent_isim.pack(side="left", padx=5, before=self.ent_miktar)
            if tur == "borc":
                self.ent_isim.configure(placeholder_text=METINLER[self.dil]["kime"])
            else:
                self.ent_isim.configure(placeholder_text=METINLER[self.dil]["kimden"])
        else:
            self.ent_isim.pack_forget()
    
    def pin_degistir_popup(self):
        self.sayfa_degistir("ayarlar")

    def tema_degistir(self):
        mod = self.switch_tema.get()
        time.sleep(0.05)
        ctk.set_appearance_mode(mod)
        self.switch_tema.configure(text=METINLER[self.dil]["karanlik"] if mod == "Dark" else METINLER[self.dil]["aydinlik"])

    def islem_kaydet(self):
        if self.opt_kullanici:
            kisi = self.opt_kullanici.get()
        else:
            kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
            kisi = kullanicilar[0] if kullanicilar else None
        if not kisi or kisi not in self.data:
            OzelUyariPenceresi(self, "Hata", "Lütfen önce (+ Yeni Kişi) ekleyiniz!", dil=self.dil)
            return
        try:
            girilen = self.ent_miktar.get().strip().replace(",", ".")
            if not girilen: return
            mik = float(girilen)
            kod = ParaBirimleri[self.cmb_para.get()]
            tur = self.tur_var.get()
            
            # Borç veya alacak için isim kontrolü
            ilgili_kisi = ""
            if tur in ["borc", "alacak"]:
                ilgili_kisi = self.ent_isim.get().strip()
                if not ilgili_kisi:
                    OzelUyariPenceresi(self, "Hata", "Lütfen kişi adı giriniz!", dil=self.dil)
                    return
            
            if tur not in self.data[kisi]: self.data[kisi][tur] = {}
            
            # Veri yapısı: {para_birimi: {"toplam": miktar, "detaylar": {isim: miktar}}}
            if tur in ["borc", "alacak"]:
                if kod not in self.data[kisi][tur]:
                    self.data[kisi][tur][kod] = {"toplam": 0, "detaylar": {}}
                elif isinstance(self.data[kisi][tur][kod], (int, float)):
                    # Eski format varsa dönüştür
                    eski_deger = self.data[kisi][tur][kod]
                    self.data[kisi][tur][kod] = {"toplam": eski_deger, "detaylar": {}}
                
                self.data[kisi][tur][kod]["detaylar"][ilgili_kisi] = self.data[kisi][tur][kod]["detaylar"].get(ilgili_kisi, 0) + mik
                self.data[kisi][tur][kod]["toplam"] = sum(self.data[kisi][tur][kod]["detaylar"].values())
            else:
                # Cüzdan için eski format
                eski = self.data[kisi][tur].get(kod, 0)
                yeni = eski + mik
                if yeni < 0: yeni = 0
                self.data[kisi][tur][kod] = yeni
            
            self.dosyaya_kaydet()
            self.ent_miktar.delete(0, "end")
            self.ent_isim.delete(0, "end")
            self.dashboard_guncelle()
        except: OzelUyariPenceresi(self, "Hata", "Geçerli bir sayı giriniz!", dil=self.dil)

    def dashboard_guncelle(self, event=None):
        if not hasattr(self, 'scroll_portfoy') or not self.scroll_portfoy.winfo_exists(): return
        for w in self.scroll_portfoy.winfo_children(): w.destroy()
        if self.opt_kullanici:
            kisi = self.opt_kullanici.get()
        else:
            kullanicilar = [k for k in self.data.keys() if k != "__AYARLAR__"]
            kisi = kullanicilar[0] if kullanicilar else None
        if not kisi or kisi not in self.data: return
        hesap = self.data[kisi]
        net = 0
        
        # Net hesaplama - hem eski hem yeni format için
        for t in ["varlik", "alacak"]:
            for k, v in hesap.get(t, {}).items():
                if isinstance(v, dict) and "toplam" in v:
                    net += v["toplam"] * self.kurlar.get(k, 0)
                else:
                    net += v * self.kurlar.get(k, 0)
        for k, v in hesap.get("borc", {}).items():
            if isinstance(v, dict) and "toplam" in v:
                net -= v["toplam"] * self.kurlar.get(k, 0)
            else:
                net -= v * self.kurlar.get(k, 0)
        
        cols = [("varlik", METINLER[self.dil]["varliklarim"], RENK_YESIL, "+"), ("alacak", METINLER[self.dil]["alacaklarim"], RENK_MAVI, "+"), ("borc", METINLER[self.dil]["borclarim"], RENK_KIRMIZI, "-")]
        for i in range(len(cols)): self.scroll_portfoy.grid_columnconfigure(i, weight=1)
        for i, (key, title, color, sign) in enumerate(cols):
            frm = ctk.CTkFrame(self.scroll_portfoy, fg_color="transparent")
            frm.grid(row=0, column=i, sticky="nsew", padx=10, pady=10)
            ctk.CTkLabel(frm, text=title, font=("Arial", 16, "bold"), text_color=color).pack(pady=(0, 10))
            if key in hesap:
                for kod, miktar in hesap[key].items():
                    # Hem eski hem yeni format için kontrol
                    if isinstance(miktar, dict) and "toplam" in miktar:
                        toplam_miktar = miktar["toplam"]
                        detaylar = miktar.get("detaylar", {})
                    else:
                        toplam_miktar = miktar
                        detaylar = {}
                    
                    if toplam_miktar <= 0: continue
                    val = toplam_miktar * self.kurlar.get(kod, 0)
                    card = ctk.CTkFrame(frm, fg_color=RENK_KART_BG, corner_radius=10)
                    card.pack(fill="x", pady=5)
                    r1 = ctk.CTkFrame(card, fg_color="transparent")
                    r1.pack(fill="x", padx=10, pady=10)
                    ikon = "💰"
                    if kod=="tl": ikon="₺"
                    elif kod=="dolar": ikon="$"
                    elif kod=="euro": ikon="€"
                    elif kod=="sterlin": ikon="£"
                    elif kod=="gram-altin": ikon="🥇"
                    elif kod=="ceyrek": ikon="🪙"
                    elif kod=="gumus": ikon="⚪"
                    elif kod=="btc": ikon="₿"
                    ctk.CTkLabel(r1, text=f"{ikon} {kod.upper()}", font=("Arial", 12, "bold"), text_color=RENK_TEXT_ANA).pack(side="left")
                    btn_frame = ctk.CTkFrame(r1, fg_color="transparent")
                    btn_frame.pack(side="right")
                    ctk.CTkButton(btn_frame, text="✏", width=40, height=32, command=lambda k=key, c=kod: self.bakiye_duzenle(k, c), fg_color="#3498db", hover_color="#2980b9", corner_radius=8, font=("Arial", 18, "bold")).pack(side="left", padx=3)
                    ctk.CTkButton(btn_frame, text="🗑", width=40, height=32, command=lambda k=key, c=kod: self.bakiye_sil(k, c), fg_color="#e74c3c", hover_color="#c0392b", corner_radius=8, font=("Arial", 18)).pack(side="left", padx=3)
                    
                    # Detayları göster (borç/alacak için)
                    if detaylar:
                        detay_frame = ctk.CTkFrame(card, fg_color="transparent")
                        detay_frame.pack(fill="x", padx=20, pady=(0,5))
                        for isim, det_mik in detaylar.items():
                            det_row = ctk.CTkFrame(detay_frame, fg_color=("#f8f9fa", "#34495e"), corner_radius=5)
                            det_row.pack(fill="x", pady=2)
                            ctk.CTkLabel(det_row, text=f"• {isim}", font=("Arial", 10), text_color=RENK_TEXT_SILIK).pack(side="left", padx=10, pady=3)
                            ctk.CTkLabel(det_row, text=f"{det_mik:.2f}", font=("Arial", 10, "bold"), text_color=RENK_TEXT_ANA).pack(side="right", padx=10, pady=3)
                    
                    r2 = ctk.CTkFrame(card, fg_color="transparent")
                    r2.pack(fill="x", padx=10, pady=(0,10))
                    if kod!="tl": ctk.CTkLabel(r2, text=f"{toplam_miktar:.2f}", text_color="gray", font=("Arial", 11)).pack(side="left")
                    ctk.CTkLabel(r2, text=f"{sign} {val:,.2f} TL", text_color=color, font=("Arial", 14, "bold")).pack(side="right")
        c = RENK_KIRMIZI if net < 0 else RENK_YESIL
        if hasattr(self, 'lbl_net_tl') and self.lbl_net_tl.winfo_exists():
            self.lbl_net_tl.configure(text=f"{net:,.2f} TL", text_color=c)

if __name__ == "__main__":
    app = FinansProApp()
    app.mainloop()