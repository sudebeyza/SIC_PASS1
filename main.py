import os  # Dosya işlemleri için os modülü import ediliyor

# OPTAB (operation table) tanımlanıyor: her komut için opcode eşleştirmesi yapılıyor
OPERATIONTABEL = {
    "ADD": "18", "AND": "40","COMP": "28",  "DIV": "24", "J": "3C",
    "JEQ": "30", "JGT": "34", "JLT": "38", "JSUB": "48", "LDA": "00", 
    "LDCH": "50","LDL": "08", "LDX": "04",  "MUL": "20","STL": "14", 
    "STSW": "E8", "STX": "10", "SUB": "1C","TD": "E0", "TIX": "2C", 
    "WD": "DC","OR": "44","RD": "D8","RSUB": "4C","STA": "0C", "STCH": "54"
}

# DIRECTIVES (directives) listesi tanımlanıyor
DIRECTIVES = ['START', 'END', 'BYTE', 'WORD', 'RESB', 'RESW', 'BASE']

# Hata kontrolü için bayrak tanımlanıyor
ErrFlag = False

try:
    inputFile = open("sic.txt", "r")  # sic.txt dosyası açılıyor
except:
    print("Belirtilen dosya bulunamadı, lütfen adını doğru kontrol edin.")
    ErrFlag = True

# Hata bayrağı kontrol ediliyor, dosya bulunamadıysa döngüden çıkılıyor
while ErrFlag:
    break

# Dosya satır satır okunuyor
Lines = inputFile.readlines()

# Her sütunu liste olarak tanımlıyoruz
LOCCOUNTER = list()
LABEL = list()
OPCODE = list()
OPERAND = list()
SYMBOL = {} #Programdaki sembollerin (etiketlerin) ve bu sembollerin adreslerinin eşleştirildiği bir sözlüktür.
ERRORS = []
index = 0
LOCATION = int("0000", base=16) #Programın çalıştırılacağı bellek adresini saklar. Programın çalışmaya başlayacağı adresi ifade eder.
progName = Lines[0][0:9].strip()
first_line = Lines[0]
byteLen = 0 #BYTE direktifinde belirtilen verinin uzunluğunu saklar. Özellikle karakter ve onaltılık veri türlerinde kullanılır.
LocctrArray = []

# Başlangıç konumu belirleniyor
if first_line[11:19].strip() == 'START':  # Eğer ilk satırın 11-19 aralığındaki kısmı 'START' ise:
    LOCATION = int(first_line[21:38].strip(), base=16)  # İlk satırdaki başlangıç adresini onaltılık tabanda al ve LOCATION'a ata
    baseLoc = LOCATION  # Başlangıç konumunu temel konum olarak belirle
    LOCCOUNTER.append(hex(baseLoc))  # Başlangıç konumunu LOCCOUNTER listesine ekleyerek bellekteki yerini kaydet 
    #hex() fonksiyonu, bir sayıyı onaltılık formata dönüştürmek için kullanılır
    LABEL.append(first_line[0:9])  # Etiketi LABEL listesine ekle
    OPCODE.append(first_line[11:19])  # İşlem kodunu OPCODE listesine ekle
    OPERAND.append(first_line[21:38].strip())  # Operanı OPERAND listesine ekle
else:  # Eğer başlangıç işareti yoksa:
    LOCATION = int("0000", base=16)  # LOCATION'ı 0000 olarak ayarla
    baseLoc = LOCATION  # Başlangıç konumunu temel konum olarak belirle

start_location = baseLoc  # Başlangıç konumunu başlangıç konumu olarak ayarla


# Dosyanın her satırı üzerinde döngü başlıyor
for lineIndex, line in enumerate(Lines):
    tempLocCtr = baseLoc
    if lineIndex == 0: continue

    # Yorum satırlarını atla
    if line.strip()[0] != '.':
        _LABEL = line[0:9].strip()
        _OPCODE = line[11:19].strip()
        _OPERAND = line[21:38].strip()

        # Etiket varsa, simgesel tabloya ekle
        if _LABEL != '':
            if _LABEL in SYMBOL: # Eğer etiket sembol tablosunda zaten varsa:
                ERRORS.append('HATA-Satır:' + str(lineIndex) + 'zaten tabloda var') 
                ErrFlag = True
            elif (_LABEL != ''):
                SYMBOL[_LABEL] = baseLoc

        # OPTAB'da komut ara
        if (_OPCODE in OPERATIONTABEL): # Eğer işlem kodu OPTAB'de tanımlı ise:
            baseLoc = baseLoc + 3
        elif (_OPCODE == 'WORD'):
            baseLoc += 3
        elif (_OPCODE == 'RESW') and (_OPERAND != ''):
            baseLoc += 3 * int(_OPERAND) # Bellek konumunu, operanda belirtilen kelimenin boyutunu (3 * operant) arttır
        elif (_OPCODE == 'RESB') and (_OPERAND != ''):
            baseLoc += int(_OPERAND)
        elif (_OPCODE == 'BYTE'):
            if (_OPERAND[0] == 'C'):
                byteLen = len(_OPERAND) - 3 # Karakter dizisinin uzunluğunu hesapla (3 karakterlik C'' işareti hariç)
                baseLoc += byteLen
            elif _OPERAND[0] == 'X':
                byteLen = (int((len(_OPERAND) - 3) / 2)) # İkilik sayı sistemine göre bayt sayısını hesapla
                baseLoc += byteLen
        elif (_OPCODE == 'END'):
            LABEL.append(_LABEL)  # Etiketi LABEL listesine ekle
            OPCODE.append(_OPCODE)  # İşlem kodunu OPCODE listesine ekle
            OPERAND.append(_OPERAND)  # Operanı OPERAND listesine ekle
            LOCCOUNTER.append("      ")  # Geçerli bellek konumunu LOCCOUNTER listesine boşluk olarak ekle
            
        else:# Eğer işlem kodu OPTAB'de tanımlı degil ise:
            ERRORS.append('HATA satır ' + str(lineIndex) + ': Geçersiz işlem kodu: ' + _OPCODE) 
            errorFlag = True
       
        if (_OPCODE != 'END'):  # END,LTORG lines have been written above
            LOCCOUNTER.append(hex(tempLocCtr))
            LABEL.append(_LABEL)
            OPCODE.append(_OPCODE)
            OPERAND.append(_OPERAND)

# Symtab dosya formatinda
with open("symtab.txt", "w") as output_file:
    # Simge tablosunu dosyaya yaz
    for Label in SYMBOL:
        output_file.write( Label.ljust(7) + "    " + str(hex(SYMBOL[Label])).upper()[2:] +'\n')
    
       
# Simge tablosu ekrana yazdırılıyor
print('\n\n         SYMTAB')
print('_________________________\n|  LABEL   |  LOCATION  |\n|-----------------------|')
for lineNumber, Label in enumerate(SYMBOL):
    print("|  " + Label.ljust(7) + " |   " + str(hex(SYMBOL[Label])).upper()[2:] + ' H   |')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n')

# Program uzunluğu hesaplanıyor ve ekrana yazdırılıyor
ProgramLength = baseLoc - start_location - 1 + 1
print("\nProgram Name: " + str(progName) + "\n" + "Program Length: " + str(hex(ProgramLength)[2:]).upper() + " H\n")



