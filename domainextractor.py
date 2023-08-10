def unique_domains(input_file, output_file):
    try:
        # Kullanıcıdan giriş dosyasını okuyarak domain listesini al
        with open(input_file, 'r') as f:
            lines = f.readlines()

        domains = set()
        
        # Her satırdaki domaini set'e ekle (tekrarları otomatik olarak filtreler)
        for line in lines:
            domain = line.strip()  # Satır sonundaki boşlukları temizle
            domains.add(domain)

        # Tekrar tekrar yazılmadan unique domainleri çıktı dosyasına yaz
        with open(output_file, 'w') as f:
            for domain in domains:
                f.write(domain + '\n')

        print("Unique domain listesi başarıyla oluşturuldu.")

    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Kullanım: python3 domainextractor.py <giriş_dosyası> <çıkış_dosyası>")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        unique_domains(input_filename, output_filename)
