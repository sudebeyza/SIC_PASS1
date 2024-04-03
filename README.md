# SIC_PASS1
 SIC standart sürüm için Python programlama dili kullanarak sembol tablosu oluşturma

# SIC PASS1 NE İŞE YARAR?
Bu program, bir SIC (Simplified Instructional Computer) programının ilk aşamasıdır. Bu aşama, kaynak kodun semantik analizini yapar ve sembol tablosunu(symtab.txt) oluşturur. Ayrıca, her komutun bellek adresini belirler ve bu adresleri işaretler(intermediate.txt). Bu bilgiler, daha sonra SIC Pass 2 veya başka bir derleyici aşaması tarafından kullanılarak nihai makine kodu oluşturulur. 

# PROJE :
![image](https://github.com/sudebeyza/SIC_PASS1/assets/115953068/8eecd881-ee3a-4445-a4b1-c808e5fdf779)

**sic.txt:** SIC programınızı içeren giriş dosyası.<br/>
**intermediate.txt:** Assembler tarafından üretilen ara çıktı dosyası. Her satır, bellek adresi ve montaj kodunu içerir.<br/>
**symtab.txt:** Programdaki sembollerin (etiketlerin) ve bu sembollerin bellek adreslerinin eşleştirildiği bir dosyadır.<br/>

Program, öncelikle `sic.txt` dosyasındaki kodları okur. Bu kodları okurken etiketlerin varlığını, adını ve adresini bulur. Bulunan bilgileri `symtab.txt` dosyasına ve konsola yazar. Bu süreçte ayrıca SIC Pass 2'de kullanılmak üzere geçici bir dosya olan `intermediate.txt` hazırlar. Bu ara dosyada, tespit edilen tüm işlemlerin gerçekleştiği adresler bulunmaktadır. Programın sonunda, programın adı ve uzunluğu çıktı olarak belirtilir.

# Kodun Çalışması
**OPTAB (operation table) Tanımlama:** Her bir komut için opcode (işlem kodu) eşleştirmelerini içeren bir sözlük oluşturulur. Bu sözlük, makine dilindeki işlem kodlarını ve bunlara karşılık gelen hexadecimal değerleri içerir.

**DIRECTIVES (directives) Tanımlama:** Programda kullanılan direktifleri içeren bir liste oluşturulur. Bu direktifler, programın akışını kontrol etmek ve bellek ayırmak için kullanılır.

**Dosya İşlemleri ve Hata Kontrolü:** sic.txt dosyası açılır ve hata kontrolü yapılır. Dosya bulunamazsa, kullanıcıya bir hata mesajı gösterilir.

**Bellek Adresleme ve İntermediate Dosya Oluşturma:** Program, bellek adresleme için gerekli olan işlemleri gerçekleştirir ve intermediate.txt dosyasını oluşturur. Bu dosya, her bir makine kodu satırını ve ilgili bellek adresini içerir.

**Sembol Tablosu Oluşturma ve Yazdırma:** Program, sembol tablosunu oluşturur ve symtab.txt dosyasına yazar. Sembol tablosu, programdaki sembollerin (etiketlerin) ve bunların bellek adreslerinin eşleştirildiği bir sözlüktür.

**Program Uzunluğunu Hesaplama ve Yazdırma:** Programın uzunluğu hesaplanır ve ekrana yazdırılır. Bu, programın kaç hexadecimal hanelik bir uzunluğa sahip olduğunu gösterir.

# Nasıl Kullanılır?
**1.** sic.txt dosyasına SIC programınızı girin. Programın ilk satırı başlatma (START) direktifini içermelidir.<br/>
**2.** Kodu çalıştırın.<br/>
**3.** Çıktılarınızı intermediate.txt ve symtab.txt dosyalarında bulabilirsiniz.Ayrica symtab'a konsoldan da ulasabilirsiniz.<br/>
**4.** Hata mesajları gerekirse konsolda görüntülenecektir.

# Sonuçlar : 
Asagida programın calışması sonucu elde edilenler verilmiştir.


<img src="https://github.com/sudebeyza/SIC_PASS1/assets/115953068/373d873d-13cd-44f4-afe2-078bd33c4848" width=200 height=300>
<img src="https://github.com/sudebeyza/SIC_PASS1/assets/115953068/15a94763-d5b2-4501-afba-92147e1c8441" width=200 height=300>
<img src="https://github.com/sudebeyza/SIC_PASS1/assets/115953068/669ce1b7-d555-4bd4-9d87-ddba4f78ec86" width=200 height=300>



