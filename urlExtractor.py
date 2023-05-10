import sys
import re

# dosya yolu parametresini alın
dosya_yolu = sys.argv[1]

# dosyayı açın ve içeriği metin değişkenine atayın
with open(dosya_yolu, 'r') as dosya:
    metin = dosya.read()

# düzenli ifade deseni
desen = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]+(?:\?\S+)?'

# metindeki tüm URL'leri bulmak için düzenli ifadeyi kullanın
url_listesi = re.findall(desen, metin)

# URL'leri yazdırın
for url in url_listesi:
    print(url)

