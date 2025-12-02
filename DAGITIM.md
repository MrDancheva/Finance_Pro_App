# Finans Pro - Dağıtım Kılavuzu

## ✅ EXE Dosyası Hazır!

### 📦 Dosya Konumu
```
dist/FinansPro.exe
```

### 🚀 Kullanım
1. `dist` klasöründeki `FinansPro.exe` dosyası tek başına çalışır
2. Kullanıcılara sadece bu dosyayı gönderebilirsiniz
3. Herhangi bir Python kurulumu gerektirmez
4. Çift tıklayarak direkt çalışır

### ⚠️ Windows Defender Uyarısı
İlk çalıştırmada Windows SmartScreen uyarı verebilir:
1. "Daha fazla bilgi" seçeneğine tıklayın
2. "Yine de çalıştır" butonuna basın
3. Bu normal bir durumdur (imzasız uygulama uyarısı)

### 📊 Dosya Boyutu
Yaklaşık 25-35 MB olabilir (tüm kütüphaneler dahil)

### 🔄 Yeniden Oluşturma
Eğer kodda değişiklik yaparsanız:
```powershell
# Kolay yol - batch dosyası
olustur_exe.bat

# Veya direkt komut
C:/Users/samet/PycharmProjects/akilli_kumbara/.venv/Scripts/python.exe -m PyInstaller --onefile --windowed --name FinansPro --clean main.py
```

### 📁 Oluşturulan Dosyalar
- `dist/FinansPro.exe` → Dağıtılacak dosya
- `build/` → Geçici dosyalar (silinebilir)
- `FinansPro.spec` → PyInstaller yapılandırması (silinebilir)

### 🎯 Dağıtım Önerileri
1. **Basit Dağıtım**: `FinansPro.exe` dosyasını paylaşın
2. **Profesyonel Dağıtım**: Inno Setup ile installer oluşturun
3. **Bulut**: Google Drive, Dropbox veya OneDrive üzerinden paylaşın

### 🔒 Güvenlik
- Program tamamen offline çalışır
- Veriler yerel `birikimler_pro.json` dosyasında saklanır
- İnternet sadece döviz/altın kurları için kullanılır (isteğe bağlı)

### ✨ Özellikler
- Tek dosya (.exe)
- Kurulum gerektirmez
- Taşınabilir (USB'den çalışır)
- Windows 10/11 uyumlu

---
**Not**: Antivirüs programları yeni/imzasız uygulamaları şüpheli görebilir. 
Bu normaldir ve virüs değildir. Kod açık kaynak ve güvenlidir.
