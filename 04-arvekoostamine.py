fmt = "{:50}";
print fmt.format("ARVE")
print

fmt = "{:20}{:20}{:20}"

print fmt.format("Arve valjastaja", "Arve Saaja", "Arvenumber: 1234")
print fmt.format("Eesnimi Perenimi", "Eesnimi Perenimi", "Arve kuupaev: 06.11.2013")
print fmt.format("Aadress", "Adress", "Makse tahtaeg: 07.11.2013")
print

fmt = "{:20}{:20}{:20}{:20}"

print fmt.format("Kaup", "Hind", "Kogus", "Kokku")
print fmt.format("Maasikad", "10.10", "1", "10.10")
print fmt.format("Mustikad", "15.00", "2", "30.00")
print fmt.format("Pohlad", "13.30", "3", "39.90")
print

fmt = "{:60}{:5}"


print fmt.format("Vahesumma", "123.123")
print fmt.format("Kaibemaks 20%", "2131.12")
print fmt.format("Kokku", "12132.213")
print


fmt = "{:20}{:20}"

print fmt.format("Kontaktid", "Arveldus")
print fmt.format("Kaibemaks 20%", "Pank: SEB Pank")
print fmt.format("Telefon: 6600600", "Konto: IBAN000012341234")



