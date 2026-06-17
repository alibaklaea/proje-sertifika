import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Sayfa Yapılandırması
st.set_page_config(page_title="Certificate Robot", page_icon="🎓")

# Görsel Tasarım Öğeleri
st.title("🕊️ Project Certificate Robot")
st.subheader("From Sumud's Children to Hope's Children")
st.write("Please enter your name below to download your official certificate.")

# Kullanıcıdan isim girişi
name = st.text_input("Enter Name & Surname (Ad Soyad Yazınız):")

if name:
    try:
        # Şablonu aç
        img = Image.open("template.png")
        draw = ImageDraw.Draw(img)
        
        # YAZI TİPİ AYARI: Yazı boyutu (80) ihtiyaca göre değiştirilebilir
        # font dosyasının adının klasördekiyle aynı olduğundan emin olun
        font = ImageFont.truetype("arial.ttf", 80)
        
        # KOORDİNAT AYARI: 
        # İsmin tam olarak noktaların üzerine gelmesi için X ve Y değerlerini ayarlamalıyız.
        # Genişlik (W) ve Yükseklik (H) bilgisini alalım
        W, H = img.size
        
        # İsmi ortalamak için (X, Y) koordinatları
        # ÖNEMLİ: 350 değerini ismin sertifikadaki dikey konumuna göre artırıp azaltın
        # (Noktalarınız görselin neresindeyse oraya denk getireceğiz)
        text_y_position = H / 2  # Görselin tam ortası. 
        
        # Yazıyı görselin ortasına hizalı şekilde yazdır
        draw.text((W/2, text_y_position), name, fill="gold", font=font, anchor="mm")
        
        # Sonucu göster
        st.image(img, caption="Preview (Önizleme)", use_column_width=True)
        
        # İndirme Butonu Oluştur
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="📥 Download Certificate (Sertifikayı İndir)",
            data=byte_im,
            file_name=f"Certificate_{name}.png",
            mime="image/png"
        )
        st.success("Your certificate is ready! Click the button above to download.")
        
    except Exception as e:
        st.error(f"An error occurred: {e}. Please make sure 'template.png' and 'arial.ttf' files are in the same folder.")
