# IMPORT
import os
import json
import string
import random
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

#COLORS
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

#DAYS
days = {
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jumat',
    'Saturday': 'Sabtu',
    'Sunday': 'Minggu'
}

#LINES
WIDTH = 50
line = '═' * WIDTH
subLine = '─' * WIDTH
vertLine = f'{CYAN}║{RESET}'

#INDENTITY
appName = 'NIK INFORMATION DECODER'
version = '1.0.0'
author = 'Eljaaa Rezeah'

#FUNCTIONS
def main():
    try:
        while True:
            menu()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Program terminated.{RESET}")

def clrScr():
    os.system('cls' if os.name == 'nt' else 'clear')

def lines():
    print(f'{CYAN}{line}{RESET}')

def subLines():
    print(f'{CYAN}{subLine}{RESET}')

def menuHeader():
    print(f'{CYAN}╔{line}╗{RESET}')
    print(f'{vertLine}{YELLOW}{appName:^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{version:^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{author:^{WIDTH}}{RESET}{vertLine}')
    print(f'{CYAN}╚{line}╝{RESET}')

def about():
    clrScr()
    print()
    print(f'{CYAN}╔{line}╗{RESET}')
    print(f'{vertLine}{YELLOW}{"TENTANG PROGRAM":^{WIDTH}}{RESET}{vertLine}')
    print(f'{CYAN}╠{line}╣{RESET}')
    print(f'{vertLine}{YELLOW}{"NIK Information Decoder adalah program CLI":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"berbasis Python untuk memvalidasi dan":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"menguraikan informasi dari Nomor Induk":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"Kependudukan (NIK). Project ini dikembangkan":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"sebagai sarana pembelajaran pemrograman untuk":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"menerapkan konsep validasi input, pengolahan":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"data, dan pengembangan aplikasi CLI.":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"":^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"Developed by : " + author:^{WIDTH}}{RESET}{vertLine}')
    print(f'{vertLine}{YELLOW}{"Version : " + version:^{WIDTH}}{RESET}{vertLine}')
    print(f'{CYAN}╚{line}╝{RESET}')
    print()
    
    while True:
      choice = input('Kembali ke menu?(y/N)   : ').strip().upper()
      
      if choice == 'Y':
        return
      elif choice == 'N':
        continue
      else:
        print(f'{RED}Masukkan tidak valid!{RESET}')

def menu():
    clrScr()
    print()
    menuHeader()
    print()
    print(f'{YELLOW}[1] Decode NIK{RESET}')
    print(f'{YELLOW}[2] Tentang Program{RESET}')
    print(f'{YELLOW}[3] Keluar{RESET}')
    
    while True:
      choice = input('\nPilih menu   : ')
      
      if choice == '1':
        decodeNik()
        break
      elif choice == '2':
        about()
        break
      elif choice == '3':
        confirm = input('Yakin ingin keluar?(y/N)   : ').strip().upper()
        if confirm == 'Y':
          clrScr()
          exit()
        elif confirm == 'N':
          continue
        else:
          print()
          print(f'{RED}Masukkan tidak valid!{RESET}')
      else:
        print(f'{RED}Menu tidak tersedia!{RESET}')

def decodeNik():
    errorMessage = None
    
    while True:
      #INTRO
      clrScr()
      menuHeader()
      print()
      header('NIK Information Decoder')
      print()
      
      if errorMessage:
        print(f'{RED}{errorMessage}{RESET}')
     
      #INPUT DATA
      print()
      section('Input Data')
      print()
      
      success, result = inputData()
      
      if not success:
        errorMessage = result
        continue
      
      errorMessage = None
      
      (name,
      nik,
      isLenVal,
      validLen,
      isNumVal,
      validNum
      ) = result
      
      #CAPTCHA
      print()
      section('Captcha')
      print()
      success, result = captcha()
      
      if not success:
        errorMessage = result
        continue
      
      errorMessage = None
      print()
      
      #DECODE REGION
      success, result = decodeRegion(nik)
      
      if not success:
        errorMessage = result
        continue
      
      errorMessage = None
      print()
      
      (provCode,
      regeCode,
      distCode,
      serialNumber,
      isRegVal,
      validReg,
      province,
      regency,
      district
      ) = result
      
      #STATUS VALIDATOR
      validNik = statValidator(isLenVal, isNumVal, isRegVal)
      
      #BIRTH AND GENDER
      success, result = decodeBirth(nik)
      
      if not success:
        errorMessage = result
        continue
      
      errorMessage = None
      print()
      
      (day,
      month,
      year,
      sex,
      birth,
      birthDay,
      birthDate
      ) = result
      
      #CALCULATE AGE
      success, result = calculateAge(day, month, year, birth)
      
      if not success:
        errorMessage = result
        continue
      
      errorMessage = None
      print()
      
      (today,
      birthdayCountdown,
      age,
      totalDaysLived,
      generation,
      ageCategory
      ) = result
      
      #DECODE TIME
      (decodeDate,
      decodeTime
      ) = getDecodeTime(today)
      
      #GET ZODIAC
      zodiac = getZodiac(day, month)
      
      clrScr()
      
      #PRINT OUTPUT
      printResult(
          #Input
          nik,
          name,
          #Status
          validNik,
          validLen,
          validNum,
          validReg,
          #Wilayah
          provCode,
          province,
          regeCode,
          regency,
          distCode,
          district,
          #Kelahiran
          birthDate,
          birthDay,
          sex,
          #Informasi
          age,
          ageCategory,
          totalDaysLived,
          birthdayCountdown,
          generation,
          zodiac,
          #Lainnya
          serialNumber,
          decodeDate,
          decodeTime)
          
      if footer():
        continue
      return

def header(title):
    text = f' {title.upper()} '
    lines()
    print(f'{YELLOW}{text.center(WIDTH)}{RESET}')
    lines()

def footer():
    print()
    print(f'{YELLOW}[1] Decode lagi{RESET}')
    print(f'{YELLOW}[2] Kembali ke menu{RESET}')
    
    while True:
      choice = input('\nPilih opsi   : ')
      
      if choice == '1':
        return True
      elif choice == '2':
        return False
      else:
        print(f'{RED}Opsi tidak tersedia!{RESET}')

def section(title):
    text = f' {title.upper()} '
    print(f'{CYAN}{text.center(WIDTH, "─")}{RESET}')

def inputData():
    name = input(f'{YELLOW}Nama Lengkap   : {RESET}')
    nik = input(f'{YELLOW}NIK            : {RESET}')
    isLenVal = len(nik) == 16
    isNumVal = nik.isdigit()
    
    if isLenVal:
      validLen = '16 Digit'
    else:
      return False, 'NIK harus memiliki 16 digit!'
    
    if isNumVal:
      validNum = 'Numeric'
    else:
      return False, 'NIK hanya boleh berisi angka!!'
    
    return True, (
      name,
      nik,
      isLenVal,
      validLen,
      isNumVal,
      validNum)

def captcha():
    captchaChar = ''.join(
    char for char in string.ascii_letters + string.digits
    if char not in 'O0Il1'
    )
    captcha = ''.join(random.choices(captchaChar, k=5))
    
    print(f'{YELLOW}CAPTCHA        : {RESET}{GREEN}{captcha}{RESET}')
    print()
    captchaInput = input(f'{YELLOW}Kode CAPTCHA   : {RESET}')
    
    if captchaInput != captcha:
      return False, 'Kode CAPTCHA tidak valid!'
    
    return True, None

def decodeRegion(nik):
    with open('wilayah.json', 'r', encoding='utf-8') as file:
      wilayah = json.load(file)
    
    regionCode = nik[:6]
    provCode = nik[:2]
    regeCode = nik[:4]
    distCode = nik[:6]
    serialNumber = nik[12:16]
    isRegVal = regionCode in wilayah
    
    if isRegVal:
      data = wilayah[regionCode]
      province = data['provinsi']
      regency = data['kabupaten']
      district = data['kecamatan']
      validReg = 'Ditemukan'
    else:
      return False, 'Wilayah NIK tidak ditemukan!'
   
    return True, (
      provCode,
      regeCode,
      distCode,
      serialNumber,
      isRegVal,
      validReg,
      province,
      regency,
      district)

def statValidator(isLenVal, isNumVal, isRegVal):
    isNikVal = isLenVal and isNumVal and isRegVal
    
    if isNikVal:
      validNik = 'Valid'
    else:
      validNik = 'Tidak Valid'
    
    return validNik

def decodeBirth(nik):
    day = int(nik[6:8])
    month = int(nik[8:10])
    year = int(nik[10:12])
    currentYear = datetime.now().year % 100
    
    if day > 40:
      sex = 'Perempuan'
      day -= 40
    else:
      sex = 'Laki-laki'
   
    if year <= currentYear:
      year += 2000
    else:
      year += 1900
    
    try:
      birth = datetime(year, month, day)
    except ValueError:
      return False, 'Tanggal NIK tidak valid!'
   
    birthWeekDay = birth.strftime('%A')
    birthDay = days[birthWeekDay]
    birthDate = f'{day:02d}-{month:02d}-{year}'
    
    return True, (
      day,
      month,
      year,
      sex,
      birth,
      birthDay,
      birthDate)

def calculateAge(day, month, year, birth):
    today = datetime.now()
    todayDate = today.date()
    targetYear = today.year
    
    if birth.date() > todayDate:
      return False, 'Tanggal NIK tidak valid!'
    
    if (month, day) < (today.month, today.day):
      targetYear += 1
   
    if month == 2 and day == 29 and not calendar.isleap(targetYear):
      nextBirthday = datetime(targetYear, 2, 28)
    else:
      nextBirthday = datetime(targetYear, month, day)
   
    nextBirthdayDate = nextBirthday.date()
    birthdayCountdownDays = (nextBirthdayDate - todayDate).days
    
    if birthdayCountdownDays == 0:
      birthdayCountdown = 'Hari Ini'
    elif birthdayCountdownDays == 1:
      birthdayCountdown = 'Besok'
    else:
      birthdayCountdown = f'{birthdayCountdownDays} Hari Lagi'
    
    lifeTime = relativedelta(today, birth)
    lifeYears = lifeTime.years
    lifeMonths = lifeTime.months
    lifeDays = lifeTime.days
    age = f'{lifeYears} Tahun {lifeMonths} Bulan {lifeDays} Hari'
    
    lifeDuration = (today - birth).days
    totalDaysLived = f'{lifeDuration} Hari'
    
    if 1946 <= year <= 1964:
      generation = 'Baby Boomer'
    elif 1965 <= year <= 1980:
      generation = 'Gen X'
    elif 1981 <= year <= 1997:
      generation = 'Milenial'
    elif 1998 <= year <= 2012:
      generation = 'Gen Z'
    elif 2013 <= year <= 2020:
      generation = 'Gen Alpha'
    elif year >= 2021:
      generation = 'Gen Beta'
    else:
      generation = 'Silent Generation'
    
    if lifeYears <= 5:
      ageCategory = 'Balita'
    elif lifeYears <= 11:
      ageCategory = 'Anak'
    elif lifeYears <= 16:
      ageCategory = 'Remaja Awal'
    elif lifeYears <= 25:
      ageCategory = 'Remaja Akhir'
    elif lifeYears <= 35:
      ageCategory = 'Dewasa Awal'
    elif lifeYears <= 45:
      ageCategory = 'Dewasa Akhir'
    elif lifeYears <= 55:
      ageCategory = 'Lansia Awal'
    elif lifeYears <= 65:
      ageCategory = 'Lansia Akhir'
    else:
      ageCategory = 'Manula'
    
    return True, (
      today,
      birthdayCountdown,
      age,
      totalDaysLived,
      generation,
      ageCategory)

def getDecodeTime(today):
    todayWeekDay = today.strftime('%A')
    todayDateDisp = today.strftime('%d-%m-%Y')
    todayTimeDisp = today.strftime('%H:%M:%S')
    todayDay = days[todayWeekDay]
    decodeDate = f'{todayDay}, {todayDateDisp}'
    decodeTime = todayTimeDisp
    
    return(
      decodeDate,
      decodeTime)

def getZodiac(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
      zodiac = 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
      zodiac = 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
      zodiac = 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
      zodiac = 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
      zodiac = 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
      zodiac = 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
      zodiac = 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
      zodiac = 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
      zodiac = 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
      zodiac = 'Scorpio'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
      zodiac = 'Sagitarius'
    else:
      zodiac = 'Capricorn'
    
    return zodiac

def printResult(nik, name, validNik, validLen, validNum, validReg, provCode, province, regeCode, regency, distCode, district, birthDate, birthDay, sex, age, ageCategory, totalDaysLived, birthdayCountdown, generation, zodiac, serialNumber, decodeDate, decodeTime):
    menuHeader()
    print()
    header('NIK Information Decoder')
    print()
    print(f'{YELLOW}NIK                   :{RESET} {nik}')
    print(f'{YELLOW}Nama Lengkap          :{RESET} {name}')
    print()
    section('Status')
    print()
    print(f'{YELLOW}Status                :{RESET} {validNik}')
    print(f'{YELLOW}Panjang               :{RESET} {validLen}')
    print(f'{YELLOW}Karakter              :{RESET} {validNum}')
    print(f'{YELLOW}Database              :{RESET} {validReg}')
    print()
    section('Wilayah')
    print()
    print(f'{YELLOW}Kode Provinsi         :{RESET} {provCode}')
    print(f'{YELLOW}Provinsi              :{RESET} {province}')
    print()
    print(f'{YELLOW}Kode Kabupaten/Kota   :{RESET} {regeCode}')
    print(f'{YELLOW}Kabupaten/Kota        :{RESET} {regency}')
    print()
    print(f'{YELLOW}Kode Kecamatan        :{RESET} {distCode}')
    print(f'{YELLOW}Kecamatan             :{RESET} {district}')
    print()
    section('Kelahiran')
    print()
    print(f'{YELLOW}Tanggal Lahir         :{RESET} {birthDate}')
    print(f'{YELLOW}Hari Lahir            :{RESET} {birthDay}')
    print(f'{YELLOW}Jenis Kelamin         :{RESET} {sex}')
    print()
    section('Informasi')
    print()
    print(f'{YELLOW}Usia                  :{RESET} {age}')
    print(f'{YELLOW}Kategori Usia         :{RESET} {ageCategory}')
    print(f'{YELLOW}Hari Hidup            :{RESET} {totalDaysLived}')
    print(f'{YELLOW}Menuju Ulang Tahun    :{RESET} {birthdayCountdown}')
    print(f'{YELLOW}Generasi              :{RESET} {generation}')
    print(f'{YELLOW}Zodiak                :{RESET} {zodiac}')
    print()
    section('Lainnya')
    print()
    print(f'{YELLOW}Kode Unik             :{RESET} {serialNumber}')
    print(f'{YELLOW}Tanggal Decode        :{RESET} {decodeDate}')
    print(f'{YELLOW}Waktu Decode          :{RESET} {decodeTime}')
    print()
    lines()

if __name__ == "__main__":
    main()