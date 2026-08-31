# OmniQR Studio Professional 🚀

**OmniQR Studio Professional**, modern, kullanıcı dostu ve modüler mimarisiyle geliştirilmiş profesyonel bir **masaüstü QR Kod üretim merkezidir**.

Kişisel, ticari ve kurumsal kullanım senaryolarına yönelik olarak; farklı içerik türlerinde QR kodlar oluşturabilir, tasarımlarını özelleştirebilir, logo ekleyebilir ve yüksek çözünürlüklü çıktılar elde edebilirsiniz.

---

## 🌟 Özellikler

### 📦 Çoklu İçerik Modülleri

Farklı ihtiyaçlara yönelik çeşitli QR içerik türlerini destekler:

* 🔗 **URL / Metin**
* 👤 **vCard – Dijital Kartvizit**
* 📧 **E-Posta**
* 📝 Özelleştirilebilir veri içerikleri

---

### 🎨 Gelişmiş QR Tasarım Motoru

QR kodların görünümünü kullanım amacınıza göre özelleştirebilirsiniz.

Desteklenen modül şekilleri:

* ◼️ Klasik kare
* ⚪ Yuvarlak
* 🔵 Noktalı

Tasarım değişiklikleri canlı önizleme üzerinden anlık olarak görüntülenebilir.

---

### 🏷️ Logo Entegrasyonu

QR kodun merkezine özel logo ekleme desteği bulunur.

Logo sistemi:

* Otomatik hizalama
* Boyutlandırma
* QR okunabilirliğini koruyacak şekilde merkezleme
* Yüksek kaliteli görsel işleme
* Logo katmanlaştırma

özelliklerini destekler.

---

### 🌈 Özelleştirilebilir Renkler

Kurumsal kimliğinize veya tasarımınıza uygun renk kombinasyonları oluşturabilirsiniz.

Özelleştirilebilir:

* QR ön plan rengi
* Arka plan rengi
* Logo
* QR modül görünümü

---

### 🛡️ Hata Düzeltme Seviyeleri

QR kodların farklı kullanım senaryolarına uygun şekilde hata düzeltme seviyeleri ayarlanabilir.

Desteklenen seviyeler:

| Seviye | Kullanım                |
| ------ | ----------------------- |
| **L**  | Düşük hata düzeltme     |
| **M**  | Orta seviye             |
| **Q**  | Yüksek hata düzeltme    |
| **H**  | En yüksek hata düzeltme |

Özellikle **logo kullanılan QR kodlarda** yüksek hata düzeltme seviyeleri tercih edilebilir.

---

### 👁️ Canlı Render Önizlemesi

Arayüzde yapılan değişiklikler gerçek zamanlı olarak QR kod önizlemesine yansıtılır.

Değiştirilebilen seçenekler:

* İçerik
* Renkler
* QR şekli
* Logo
* Hata düzeltme seviyesi
* Tasarım seçenekleri

Bu sayede QR kodu oluşturmadan önce sonucu anında görebilirsiniz.

---

## 🖥️ Teknolojiler

OmniQR Studio Professional aşağıdaki teknolojiler kullanılarak geliştirilmiştir:

| Teknoloji         | Kullanım Alanı          |
| ----------------- | ----------------------- |
| **Python 3.x**    | Uygulama altyapısı      |
| **CustomTkinter** | Modern masaüstü arayüzü |
| **Pillow (PIL)**  | Görsel işleme           |
| **qrcode**        | QR kod üretimi          |

### Kullanılan Kütüphaneler

* `customtkinter`
* `qrcode`
* `Pillow`

---

# 🚀 Kurulum

## 1. Repoyu Klonlayın

Projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/ardairmk55/omniqr-studio.git
```

Ardından proje klasörüne girin:

```bash
cd omniqr-studio
```

---

## 2. Gerekli Kütüphaneleri Yükleyin

Gerekli Python paketlerini aşağıdaki komutla yükleyebilirsiniz:

```bash
pip install qrcode[pil] customtkinter Pillow
```

---

## 3. Uygulamayı Başlatın

Kurulum tamamlandıktan sonra uygulamayı çalıştırın:

```bash
python app.py
```

Uygulama masaüstü arayüzüyle başlatılacaktır. 🎉

---

# 📁 Proje Yapısı

Örnek proje yapısı:

```text
omniqr-studio/
│
├── app.py
├── README.md
├── requirements.txt
│
├── assets/
│   └── ...
│
└── ...
```

---

# 📋 Gereksinimler

Projeyi çalıştırmak için:

* **Python 3.x**
* Windows / macOS / Linux
* İnternet bağlantısı yalnızca kurulum sırasında gerekli olabilir.

Python sürümünüzü kontrol etmek için:

```bash
python --version
```

---

# 🎯 Kullanım Alanları

OmniQR Studio Professional birçok farklı kullanım senaryosunda kullanılabilir:

* 🌐 Web sitesi bağlantıları
* 💼 Dijital kartvizitler
* 📧 E-posta bağlantıları
* 🏢 Kurumsal QR kodlar
* 🛍️ Ürün ve ambalaj QR kodları
* 📱 Sosyal medya yönlendirmeleri
* 📄 Dijital doküman bağlantıları
* 🎟️ Etkinlik ve davetiyeler
* 🏷️ Marka ve işletme kullanımları

---

# 🔐 QR Kod Kalitesi

QR kodun doğru şekilde okunabilmesi için tasarım sırasında kontrast ve hata düzeltme seviyesine dikkat edilmesi önerilir.

Özellikle logo kullanılan tasarımlarda:

```text
Error Correction → H
```

seviyesinin tercih edilmesi okunabilirliğin korunmasına yardımcı olabilir.

---

# 🛠️ Geliştirme

Projeyi kendi ihtiyaçlarınıza göre geliştirebilir ve yeni modüller ekleyebilirsiniz.

Örnek geliştirme alanları:

* Yeni QR içerik türleri
* Yeni QR şekilleri
* Gelişmiş logo seçenekleri
* PNG / JPG / SVG çıktı desteği
* PDF çıktısı
* QR geçmişi
* Toplu QR oluşturma
* Tema sistemi
* Gelişmiş şablon sistemi

---


---

# 👨‍💻 Geliştirici

**Arda İrmk**

GitHub:
https://github.com/ardairmk55

---

## ⭐ Destek Ol

Projeyi faydalı bulduysanız GitHub üzerinden ⭐ **Star** vermeyi unutmayın!

---

<p align="center">
  <strong>OmniQR Studio Professional</strong>
  <br>
  Modern QR kod üretimi. Profesyonel tasarım. 🚀
</p>
