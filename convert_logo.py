from PIL import Image

# Yeni logoyu aç (new_logo.png olarak kaydetmeniz gerekiyor)
try:
    img = Image.open("new_logo.png")
    
    # ICO formatına çevir (birden fazla boyut ekle)
    img.save("icon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    
    print("✅ Logo başarıyla icon.ico olarak kaydedildi!")
    print("📁 Dosya: icon.ico")
except FileNotFoundError:
    print("❌ HATA: new_logo.png bulunamadı!")
    print("Lütfen önce yeni logo görselini 'new_logo.png' olarak bu klasöre kaydedin.")
except Exception as e:
    print(f"❌ HATA: {e}")
