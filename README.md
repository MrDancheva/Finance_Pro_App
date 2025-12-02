# Finans Pro - Electron + React

Modern finansal varlık yönetim uygulaması

## 🚀 Kurulum

### Gereksinimler
- Node.js 18+ 
- npm veya yarn

### Başlangıç

```bash
# Bağımlılıkları yükle
npm install

# Geliştirme modunda çalıştır
npm start

# Production build
npm run build

# Electron uygulaması olarak paketleWindows için)
npm run package:win
```

## 📦 Teknolojiler

- **Electron** - Masaüstü uygulama framework
- **React 18** - UI library
- **Material-UI (MUI)** - Modern component library
- **Vite** - Hızlı build tool

## 🎯 Özellikler

- ✅ Çoklu dil desteği (TR/EN)
- ✅ Varlık/Borç/Alacak yönetimi
- ✅ Canlı piyasa takibi
- ✅ PIN koruması
- ✅ Modern ve kullanıcı dostu arayüz
- ✅ Yerel veri saklama (Documents/FinansPro)

## 📁 Proje Yapısı

```
finans-pro/
├── electron/          # Electron ana işlem dosyaları
│   ├── main.js       # Ana Electron dosyası
│   └── preload.js    # Preload script
├── src/              # React kaynak kodları
│   ├── components/   # React bileşenleri
│   ├── pages/        # Sayfa bileşenleri
│   ├── App.jsx       # Ana uygulama
│   ├── main.jsx      # React giriş noktası
│   ├── constants.js  # Sabitler ve dil dosyaları
│   └── DataManager.js # Veri yönetimi
├── assets/           # Statik dosyalar
├── package.json      # Proje yapılandırması
└── vite.config.js    # Vite yapılandırması
```

## 🔧 Geliştirme

1. `npm start` - React dev server ve Electron'u birlikte çalıştırır
2. Değişiklikler otomatik yenilenir (hot reload)
3. DevTools otomatik açılır

## 📦 Paketleme

```bash
# Windows için EXE oluştur
npm run package:win
```

Oluşturulan dosyalar `dist/` klasöründe olacaktır.

## 📝 Lisans

MIT

---

