import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image
import customtkinter as ctk
from tkinter import filedialog, messagebox, colorchooser
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class OmniQRStudio(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OmniQR Studio Professional")
        self.geometry("1100x750")
        self.minsize(1000, 700)

        # Durum Değişkenleri
        self.secilen_on_renk = "#000000"
        self.secilen_arka_renk = "#FFFFFF"
        self.secilen_logo_yolu = ""
        self.guncel_qr_pil = None

        # Ortak Fontlar
        self.font_baslik = ctk.CTkFont(family="Segoe UI", size=26, weight="bold")
        self.font_alt_baslik = ctk.CTkFont(family="Segoe UI", size=14, weight="bold")
        self.font_metin = ctk.CTkFont(family="Segoe UI", size=13)

        self.arayuz_olustur()
        self.onizlemeyi_guncelle()

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def arayuz_olustur(self):
        # Sol Panel - Kontrol Merkezi
        self.sol_frame = ctk.CTkScrollableFrame(self, width=450, corner_radius=15, fg_color="#1E1E1E")
        self.sol_frame.pack(side="left", fill="y", padx=25, pady=25)

        # Sağ Panel - Önizleme ve Durum
        self.sag_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="#121212")
        self.sag_frame.pack(side="right", fill="both", expand=True, padx=(0, 25), pady=25)

        # Üst Başlık Alanı
        baslik_frame = ctk.CTkFrame(self.sol_frame, fg_color="transparent")
        baslik_frame.pack(anchor="w", fill="x", pady=(10, 20))
        ctk.CTkLabel(baslik_frame, text="OmniQR Studio", font=self.font_baslik, text_color="#3498DB").pack(anchor="w")
        ctk.CTkLabel(baslik_frame, text="Profesyonel Karekod Üretim Merkezi", font=self.font_metin, text_color="#7F8C8D").pack(anchor="w")

        # 1. BÖLÜM: VERİ GİRİŞİ
        ctk.CTkLabel(self.sol_frame, text="1. İçerik Verisi", font=self.font_alt_baslik).pack(anchor="w", pady=(10, 5))
        self.tabview = ctk.CTkTabview(self.sol_frame, width=420, height=220, command=self.onizlemeyi_guncelle, segmented_button_selected_color="#2980B9")
        self.tabview.pack(anchor="w", pady=(0, 20))
        
        self.tabview.add("🔗 URL / Metin")
        self.tabview.add("👤 vCard (Kişi)")
        self.tabview.add("✉️ E-Posta")

        # Sekme İçerikleri: URL
        self.entry_link = ctk.CTkEntry(self.tabview.tab("🔗 URL / Metin"), placeholder_text="https:// veya herhangi bir metin...", width=380, height=45, font=self.font_metin)
        self.entry_link.pack(pady=40)
        self.entry_link.bind("<KeyRelease>", self.onizlemeyi_guncelle)

        # Sekme İçerikleri: vCard
        vcard_grid = ctk.CTkFrame(self.tabview.tab("👤 vCard (Kişi)"), fg_color="transparent")
        vcard_grid.pack(expand=True)
        self.entry_vcard_isim = ctk.CTkEntry(vcard_grid, placeholder_text="Ad Soyad", width=180, height=35)
        self.entry_vcard_isim.grid(row=0, column=0, padx=8, pady=10)
        self.entry_vcard_isim.bind("<KeyRelease>", self.onizlemeyi_guncelle)

        self.entry_vcard_tel = ctk.CTkEntry(vcard_grid, placeholder_text="Telefon Numarası", width=180, height=35)
        self.entry_vcard_tel.grid(row=0, column=1, padx=8, pady=10)
        self.entry_vcard_tel.bind("<KeyRelease>", self.onizlemeyi_guncelle)

        self.entry_vcard_mail = ctk.CTkEntry(vcard_grid, placeholder_text="E-Posta Adresi", width=180, height=35)
        self.entry_vcard_mail.grid(row=1, column=0, padx=8, pady=10)
        self.entry_vcard_mail.bind("<KeyRelease>", self.onizlemeyi_guncelle)

        self.entry_vcard_sirket = ctk.CTkEntry(vcard_grid, placeholder_text="Şirket / Kurum", width=180, height=35)
        self.entry_vcard_sirket.grid(row=1, column=1, padx=8, pady=10)
        self.entry_vcard_sirket.bind("<KeyRelease>", self.onizlemeyi_guncelle)

        # Sekme İçerikleri: E-Posta
        self.entry_email_alici = ctk.CTkEntry(self.tabview.tab("✉️ E-Posta"), placeholder_text="Alıcı E-Posta Adresi", width=380, height=35)
        self.entry_email_alici.pack(pady=(20, 10))
        self.entry_email_alici.bind("<KeyRelease>", self.onizlemeyi_guncelle)
        
        self.entry_email_konu = ctk.CTkEntry(self.tabview.tab("✉️ E-Posta"), placeholder_text="Konu Başlığı", width=380, height=35)
        self.entry_email_konu.pack(pady=5)
        self.entry_email_konu.bind("<KeyRelease>", self.onizlemeyi_guncelle)

        # 2. BÖLÜM: TASARIM MOTORU
        ctk.CTkLabel(self.sol_frame, text="2. Görsel Yapılandırma", font=self.font_alt_baslik).pack(anchor="w", pady=(15, 10))
        tasarim_frame = ctk.CTkFrame(self.sol_frame, fg_color="#2A2D31", corner_radius=10)
        tasarim_frame.pack(anchor="w", fill="x", pady=(0, 20), ipadx=10, ipady=10)
        
        # Stil ve Kalite
        stil_ayar_frame = ctk.CTkFrame(tasarim_frame, fg_color="transparent")
        stil_ayar_frame.pack(fill="x", pady=(10, 5), padx=10)
        
        ctk.CTkLabel(stil_ayar_frame, text="Form:", font=self.font_metin).pack(side="left", padx=(0, 10))
        self.combo_stil = ctk.CTkComboBox(stil_ayar_frame, values=["Klasik Kare", "Yuvarlak", "Noktalı"], width=130, command=self.onizlemeyi_guncelle)
        self.combo_stil.pack(side="left")

        ctk.CTkLabel(stil_ayar_frame, text="Hata Payı:", font=self.font_metin).pack(side="left", padx=(20, 10))
        self.combo_hata = ctk.CTkComboBox(stil_ayar_frame, values=["H (%30)", "Q (%25)", "M (%15)"], width=100, command=self.onizlemeyi_guncelle)
        self.combo_hata.pack(side="left")

        # Renk Paleti
        renk_frame = ctk.CTkFrame(tasarim_frame, fg_color="transparent")
        renk_frame.pack(fill="x", pady=15, padx=10)

        self.btn_on_renk = ctk.CTkButton(renk_frame, text="Ön Renk (#000000)", command=self.on_renk_sec, width=170, height=35, fg_color="#000000", hover_color="#333333", border_width=1, border_color="#555555")
        self.btn_on_renk.pack(side="left", expand=True, padx=(0, 5))

        self.btn_arka_renk = ctk.CTkButton(renk_frame, text="Arka Plan (#FFFFFF)", command=self.arka_renk_sec, width=170, height=35, fg_color="#FFFFFF", text_color="black", hover_color="#E0E0E0")
        self.btn_arka_renk.pack(side="left", expand=True, padx=(5, 0))

        # 3. BÖLÜM: MARKALAMA
        ctk.CTkLabel(self.sol_frame, text="3. Markalama & Logo", font=self.font_alt_baslik).pack(anchor="w", pady=(10, 10))
        logo_frame = ctk.CTkFrame(self.sol_frame, fg_color="transparent")
        logo_frame.pack(anchor="w", fill="x", pady=(0, 25))
        
        self.btn_logo = ctk.CTkButton(logo_frame, text="🖼️ Merkez Logo Seç", command=self.logo_sec, width=280, height=40, fg_color="#2C3E50", hover_color="#34495E")
        self.btn_logo.pack(side="left", padx=(0, 10))
        
        self.btn_logo_sil = ctk.CTkButton(logo_frame, text="🗑️ Temizle", command=self.logo_sil, width=120, height=40, fg_color="#C0392B", hover_color="#A93226", state="disabled")
        self.btn_logo_sil.pack(side="left")

        # DIŞA AKTAR
        self.btn_kaydet = ctk.CTkButton(self.sol_frame, text="🚀 YÜKSEK ÇÖZÜNÜRLÜKTE İNDİR", command=self.qr_kaydet, font=self.font_alt_baslik, height=55, fg_color="#27AE60", hover_color="#219150")
        self.btn_kaydet.pack(anchor="w", fill="x", pady=(10, 10))

        # --- SAĞ PANEL (ÖNİZLEME) ---
        ctk.CTkLabel(self.sag_frame, text="Canlı Render Önizlemesi", font=self.font_alt_baslik, text_color="#BDC3C7").pack(pady=(30, 15))
        
        self.onizleme_kapsayici = ctk.CTkFrame(self.sag_frame, fg_color="#FFFFFF", corner_radius=15, width=450, height=450)
        self.onizleme_kapsayici.pack(expand=True)
        self.onizleme_kapsayici.pack_propagate(False) 
        
        self.lbl_onizleme = ctk.CTkLabel(self.onizleme_kapsayici, text="")
        self.lbl_onizleme.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_durum = ctk.CTkLabel(self.sag_frame, text="🟢 Sistem Hazır", text_color="#2ECC71", font=self.font_metin)
        self.lbl_durum.pack(side="bottom", pady=20, padx=20, anchor="w")

    def icerik_verisi_al(self):
        aktif_sekme = self.tabview.get()
        
        if aktif_sekme == "🔗 URL / Metin":
            return self.entry_link.get() or "https://omniqr.studio"
            
        elif aktif_sekme == "👤 vCard (Kişi)":
            isim = self.entry_vcard_isim.get() or "Ad Soyad"
            tel = self.entry_vcard_tel.get() or ""
            mail = self.entry_vcard_mail.get() or ""
            sirket = self.entry_vcard_sirket.get() or ""
            return f"BEGIN:VCARD\nVERSION:3.0\nFN:{isim}\nORG:{sirket}\nTEL:{tel}\nEMAIL:{mail}\nEND:VCARD"
            
        elif aktif_sekme == "✉️ E-Posta":
            alici = self.entry_email_alici.get() or "ornek@mail.com"
            konu = self.entry_email_konu.get() or ""
            return f"mailto:{alici}?subject={konu}"

    def qr_resmi_uret(self):
        veri = self.icerik_verisi_al()
        
        hata_seviyeleri = {
            "H (%30)": qrcode.constants.ERROR_CORRECT_H, 
            "Q (%25)": qrcode.constants.ERROR_CORRECT_Q, 
            "M (%15)": qrcode.constants.ERROR_CORRECT_M
        }
        
        qr = qrcode.QRCode(
            version=4,
            error_correction=hata_seviyeleri[self.combo_hata.get()],
            box_size=15,
            border=2,
        )
        qr.add_data(veri)
        qr.make(fit=True)

        stil = self.combo_stil.get()
        if stil == "Noktalı": drawer = CircleModuleDrawer()
        elif stil == "Yuvarlak": drawer = RoundedModuleDrawer()
        else: drawer = SquareModuleDrawer()

        rgb_on = self.hex_to_rgb(self.secilen_on_renk)
        rgb_arka = self.hex_to_rgb(self.secilen_arka_renk)

        qr_resim = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=drawer,
            color_mask=SolidFillColorMask(front_color=rgb_on, back_color=rgb_arka)
        ).convert('RGB')

        if self.secilen_logo_yolu and os.path.exists(self.secilen_logo_yolu):
            try:
                logo = Image.open(self.secilen_logo_yolu).convert("RGBA")
                baslangic_boyutu = qr_resim.size[0]
                logo_boyutu = int(baslangic_boyutu * 0.22)
                logo = logo.resize((logo_boyutu, logo_boyutu), Image.Resampling.LANCZOS)
                
                pozisyon = ((baslangic_boyutu - logo_boyutu) // 2, (baslangic_boyutu - logo_boyutu) // 2)
                qr_resim.paste(logo, pozisyon, logo)
            except Exception:
                self.lbl_durum.configure(text="🔴 Hata: Logo işlenemedi", text_color="#E74C3C")

        return qr_resim

    def onizlemeyi_guncelle(self, *args):
        self.guncel_qr_pil = self.qr_resmi_uret()
        
        ctk_img = ctk.CTkImage(light_image=self.guncel_qr_pil, dark_image=self.guncel_qr_pil, size=(410, 410))
        self.lbl_onizleme.configure(image=ctk_img)
        self.lbl_durum.configure(text="🟢 Önizleme Güncel", text_color="#2ECC71")

    def on_renk_sec(self):
        renk = colorchooser.askcolor(initialcolor=self.secilen_on_renk, title="Karekod Rengini Seçin")[1]
        if renk:
            self.secilen_on_renk = renk
            self.btn_on_renk.configure(fg_color=renk, text=f"Ön Renk ({renk.upper()})", text_color="white" if renk != "#ffffff" else "black")
            self.onizlemeyi_guncelle()

    def arka_renk_sec(self):
        renk = colorchooser.askcolor(initialcolor=self.secilen_arka_renk, title="Arka Plan Rengini Seçin")[1]
        if renk:
            self.secilen_arka_renk = renk
            self.btn_arka_renk.configure(fg_color=renk, text=f"Arka Plan ({renk.upper()})", text_color="white" if renk != "#ffffff" else "black")
            self.onizlemeyi_guncelle()

    def logo_sec(self):
        dosya = filedialog.askopenfilename(filetypes=[("Görsel Dosyaları", "*.png;*.jpg;*.jpeg")])
        if dosya:
            self.secilen_logo_yolu = dosya
            dosya_adi = os.path.basename(dosya)
            self.btn_logo.configure(text=f"✅ {dosya_adi[:15]}...", fg_color="#27AE60")
            self.btn_logo_sil.configure(state="normal")
            self.onizlemeyi_guncelle()

    def logo_sil(self):
        self.secilen_logo_yolu = ""
        self.btn_logo.configure(text="🖼️ Merkez Logo Seç", fg_color="#2C3E50")
        self.btn_logo_sil.configure(state="disabled")
        self.onizlemeyi_guncelle()

    def qr_kaydet(self):
        if not self.guncel_qr_pil: return
        kayit_yolu = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Formatı", "*.png"), ("JPEG Formatı", "*.jpg")],
            title="Karekod Çıktısını Kaydet"
        )
        if kayit_yolu:
            self.guncel_qr_pil.save(kayit_yolu)
            self.lbl_durum.configure(text=f"✨ {os.path.basename(kayit_yolu)} başarıyla kaydedildi!", text_color="#F1C40F")
            messagebox.showinfo("Başarılı İşlem", "Karekod belirtilen konuma yüksek kalitede kaydedildi.")

if __name__ == "__main__":
    app = OmniQRStudio()
    app.mainloop()