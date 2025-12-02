# Finans Pro - Kurulum Kılavuzu

## EXE Dosyası Oluşturma

### 1. Gerekli Paketleri Yükleyin
```powershell
pip install cx_Freeze
```

### 2. EXE Dosyasını Oluşturun
```powershell
python setup.py build
```

Bu komut `build` klasörü içinde `exe.win-amd64-3.x` adında bir klasör oluşturacak.
İçinde `FinansPro.exe` dosyası bulunur.

### 3. Dağıtım
- `build/exe.win-amd64-3.x` klasörünün tamamını paylaşın
- Kullanıcılar `FinansPro.exe` dosyasına çift tıklayarak programı çalıştırabilir
- Klasördeki tüm DLL ve dosyalar gereklidir, sadece .exe dosyası yeterli değildir

## PyInstaller ile Tek Dosya EXE (Alternatif)

Eğer tek bir .exe dosyası istiyorsanız:

### 1. PyInstaller Yükleyin
```powershell
pip install pyinstaller
```

### 2. Tek Dosya EXE Oluşturun
```powershell
pyinstaller --onefile --windowed --name FinansPro main.py
```

Parametreler:
- `--onefile`: Tek bir .exe dosyası oluşturur
- `--windowed`: Konsol penceresi olmadan çalışır
- `--name`: Çıktı dosyasının adı

### 3. Çıktı
- `dist` klasöründe `FinansPro.exe` dosyası oluşur
- Bu dosya tek başına çalışır, ek dosya gerekmez

## Not
İlk çalıştırmada Windows Defender uyarı verebilir. Bu normaldir.
"Daha fazla bilgi" > "Yine de çalıştır" seçeneğini kullanabilirsiniz.

## Önerilen Yöntem
**PyInstaller** kullanmanızı öneririm çünkü:
- Tek dosya oluşturur (daha kolay dağıtım)
- Kullanıcı için daha basit
- Windows Defender ile daha az sorun
