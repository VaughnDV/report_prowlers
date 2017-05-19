from app import *
from random import randint
import string
import random


first_names = [
    'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie', 'Sophie', 'Mia',
    'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
    'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
]
last_names = [
    'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
    'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
    'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
]
colours = [
    'red', 'blue', 'yellow', 'black', 'green', 'brown', 'purple', 'white', 
    'light blue', 'beige' , 'cream'
]
#areas = [
#    'Port Edward', 'Meadow Brook', 'North Sand Bluff', 'Ivy Beach', ' Three Hills',
#    'Leisure Bay', 'Nzimakwe', 'Glenmore', 'Palm Beach', 'Sanlameer', 'South Broom',
#    'Trafalgar', 'Munster'
#]

ages = [
    'Teens', '20-40', '40+'
]
builds = [
    'slim', 'medium', 'large'
]
heights = [
    'tall', 'meduim', 'short'
]
tones = [
    'light', 'medium', 'dark'
]
makes = [
    'toyota', 'nissan', 'bmw', 'mercedes', 'audi', 'chevrolet', 'citroen',
    'fiat', 'ford', 'honda', 'gmc', 'jeep', 'hyundai', 'kia', 'jaguar', 'land rover',
    'mazada', 'lexus', 'peugeot', 'renault', 'suzuki', 'volkswagen', 'volvo'
]

models = [
    'bakkie', 'hatchback', 'doublecab', 'combi', 'truck', 'sedan', 'taxi', 'rust bucket' 
]

filenames = []


nc = [
        'Aalwynsfontein','Aggeneys','Alexander Bay','Andriesvale','Askham','Augrabies','Barkly West','Bekker','Belmont','Bermolli','Biesiespoort','Britstown','Calvinia','Campbell',
        'Carlton','Carnarvon','Carolusberg','Concordia','Colesberg','Colston','Copperton','Danielskuil','De Aar','Delportshoop','Dibeng','Dingleton','Douglas','Fraserburg','Griekwastad',
        'Groblershoop','Hopetown','Kimberley','Modder River','Orania','Prieska','Richmond','Springbok','Strydenburg','Upington','Victoria West','Warrenton','Williston',
        ]

ec = [
        'Aberdeen','Adelaide','Adendorp','Addo','Alderley','Alexandria','Alice','Alicedale','Aliwal North','Bailey','Balfour','Barakke','Barkly East','Baroda','Baroe','Bathurst','Bedford','Behulpsaam','Bell','Bellevue','Berlin','Bethelsdorp','Bhisho',
        'Bityi','Bonza Bay','Braunschweig','Burgersdorp','Butterworth','Cala','Cambria','Cannon Rocks','Cape St. Francis','Cathcart','Chalumna','Chintsa',
        'Clarkebury','Clifford','Coega','Coffee Bay','Cofimvaba','Coghlan','Colchester','Coleford','Cookhouse','Cradock','Despatch','Dohne','Dordrecht','Dutywa','East London','Elliot','Flagstaff','Fort Beaufort',
        'Gcuwa','Gonubie','Graaff-Reinet','Grahamstown','Hankey','Hofmeyr','Humansdorp','Jansenville','Jeffreys Bay','Kenton-on-Sea',
        'King Williams Town','Kirkwood','Lady Frere','Lady Grey','Maclear','Madadeni','Mandini','Matatiele','Middelburg','Molteno','Mount Fletcher','Mthatha','Engcobo','Nieu-Bethesda','Oyster Bay','Patensie',
        'Paterson','Port Alfred','Port Elizabeth','Queenstown','Somerset East','Steynsburg','St Francis Bay','Stutterheim','Tarkastad','Uitenhage','uMthatha','Whittlesea','Zwelitsha',
        ]

l = [
        'Afguns','Alldays','Baltimore','Bandelierkop','Bandur','Beauty','Beitbridge','Bela-Bela','Burgersfort','Carlow','Chuniespoort','Duiwelskloof','Giyani','Gravelotte ','Groblersdal','Haenertsburg','Hoedspruit','Lephalale',
        'Louis Trichardt','Marble Hall','Modimolle','Mokopane','Musina','Naboomspruit','Phalaborwa','Polokwane','Shawela','Thabazimbi','Thohoyandou','Vaalwater','Vivo',
        ]

kzn = [
        'Ahrens','Aldinville','Alpha','Amanzimtoti','Anerley','Babanango','Balgowan',
        'Ballengeich','Ballito','Banana Beach','Bayala','Bazley','Bendigo','Bergville','Besters','Biggarsberg','Boston','Bulwer','Calvert','Camperdown','Candover','Cape Vidal','Catalina Bay','Cato Ridge','Cedarville','Charlestown','Clansthal','Clermont','Colenso','Dannhauser','Darnall','Doonside','Drummond','Dundee',
        'Durban','ekuPhakameni','Elandslaagte','Empangeni','Eshowe','Estcourt','Franklin','Glencoe','Greytown','Hattingspruit','Hibberdene','Hillcrest',
        'Hilton','Himeville','Hluhluwe','Howick','Ifafa Beach','Illovo Beach','Impendle','Inanda','Ingwavuma','Isipingo','Ixopo','Karridene','Kingsburgh','Kloof','Kokstad','KwaDukuza','KwaMashu','Ladysmith','La Lucia','La Mercy','Louwsburg','Magabeni','Mahlabatini','Margate','Melmoth','Merrivale','Mkuze','Mooirivier','Mount Edgecombe',
        'Mtubatuba','Mtunzini','Newcastle','New Germany','New Hanover','Nongoma','Nottingham Road','Palm Beach','Park Rynie','Paulpietersburg','Pennington','Pietermaritzburg','Pinetown','Pomeroy','Pongola','Port Edward','Port Shepstone','Queensburgh','Ramsgate',
        'Richards Bay','Salt Rock','Scottburgh','Sezela','Shelly Beach',
        'Southbroom','St Lucia','St Michaels-on-sea','Tongaat','Tugela Ferry','Ubombo','Ulundi','Umbogintwini','Umdloti','Umgababa','Umhlanga Rocks','Umkomaas','Umlazi','Umtentweni','Umzinto','Umzumbe','Underberg','Utrecht',
        'Uvongo','Van Reenen','Verulam','Virginia','Vryheid','Warner Beach','Wartburg','Wasbank','Weenen','Westville','Winkelspruit','Winterton','York',
        ]

gp = [
        'Akasia','Alberton','Alexandra','Atteridgeville','Ban ','Bapsfontein','Benoni','Boipatong',
        'Boksburg','Bophelong','Brakpan','Bronkhorstspruit','Carletonville','Centurion','Chantelle','Cullinan','Daveyton','Devon','Duduza','Edenvale','Evaton','Fochville','Germiston',
        'Hammanskraal','Heidelberg','Henley on Klip','Irene','Isando','Johannesburg','Katlehong','Kempton Park','Kromdraai',
        'Krugersdorp','KwaThema','Lenasia','Lyttelton','Magaliesburg','Mamelodi','Meyerton','Midrand','Muldersdrift','Nigel','Orchards','Pretoria','Randburg','Randfontein',
        'Ratanda','Roodepoort','Rooihuiskraal','Sandton','Sebokeng','Sharpeville','Soshanguve','Soweto','Springs','Tembisa','Thokoza','Tsakane','Vanderbijlpark','Vereeniging','Vosloorus','Wedela','Westonaria',
        ]

wc = [
        'Aan de Doorns','Abbotsdale','Agulhas','Albertinia','Amalienstein',
        'Arniston','Ashton','Atlantis','Aurora','Baardskeerdersbos','Barrington','Barrydale','Baviaan','Beaufort West','Bellville','Berea','Bergplaas','Bergrivier','Biesiesfontein',
        'Bitterfontein','Bonnievale','Bredasdorp','Buffelsjagbaai','Caledon','Calitzdorp','Camps Bay','Cape Town','Ceres','Churchaven','Citrusdal',
        'Clanwilliam','Claremont','Clarkson','Clifton','Constantia','Darling','De Doorns','De Kelders','De Rust','Doringbaai','Dysselsdorp','Eendekuil','Elandsbaai','Elim','Elgin',
        'Fisherhaven','Franskraal','Franschhoek','Gansbaai','Genadendal','George','Gouda','Graafwater','Grabouw','Greyton','Heidelberg',
        'Hermanus','Hopefield','Keurboomstrand','Khayelitsha','Knysna','Laingsburg','Lamberts Bay','Matjiesfontein','Mossel Bay','Oudtshoorn','Paarl','Piketberg',
        'Plettenberg Bay','Pniel','Prins Albert','Riebeek Kasteel','Somerset West','Stellenbosch','Strand','Swartberg','Swellendam','Tulbagh','Uniondale','Wellington','Wilderness','Worcester',
        ]

mp =[
        'Acornhoek','Amersfoort','Amsterdam','Badplaas','Balfour','Balmoral','Bankkop',
        'Barberton','Belfast','Berbice','Bethal','Bettiesdam','Bosbokrand','Breyten','Carolina','Charl Cilliers','Chrissiesmeer','Clewer',
        'Coalville','Commondale','Cork','Delmas','Dullstroom','Ermelo','Graskop','Greylingstad','Hazyview','Hectorspruit','Kaapmuiden','Kinross','Komatipoort','Kriel',
        'KwaMhlanga','Loopspruit','Lydenburg','Machadodorp','Malelane','Middelburg','Morgenzon','Muden','Nelspruit','Ogies','Ohrigstad','Perdekop','Piet Retief','Pilgrims Rest',
        'Sabie','Secunda','Standerton','Trichardt','Vaalbank','Volksrust','Wakkerstroom','Waterval Boven','Waterval Onder','White River','Witbank',
        ]

nw = [
        'Albertshoek','Alettasrus','Amalia','Babelegi','Bakerville','Barberspan','Beestekraal',
        'Bethanie','Bewley','Biesiesvlei','Bloemhof','Bray','Brits','Broederstroom','Carlsonia','Christiana','Coligny','Delareyville',
        'Derby','Ganyesa','Ga-Rankuwa','Groot Marico','Lichtenburg','Mafikeng','Orkney','Potchefstroom','Rustenburg','Vryburg','Wolmaransstad','Zeerust',
        ]

fs = [
        'Aberfeldy','Allandale','Allanridge','Allep','Arlington','Bethlehem','Bethulie','Bloemfontein','Boshof','Bothaville','Botshabelo','Brandfort','Bultfontein','Boompie Alleen','Clarens','Clocolan','Cornelia','Dealesville',
        'Deneysville','Dewetsdorp','Edenburg','Edenville','Excelsior','Fauresmith','Ficksburg','Fouriesburg','Frankfort','Harrismith','Heilbron','Hennenman','Hertzogville','Hobhouse','Hoopstad','Jacobsdal','Jagersfontein',
        'Kestell','Kgotsong','Koffiefontein','Koppies','Kroonstad','Ladybrand','Lindley','Luckhoff','Makeleketla','Marquard','Memel','Odendaalsrus','Oranjeville','Parys','Paul Roux',
        'Petrusburg','Petrus Steyn','Philippolis','Phuthaditjhaba','Reddersburg','Reitz','Rosendal','Rouxville','Sasolburg','Senekal','Smithfield','Springfontein','Steynsrus','Swinburne','Thaba Nchu','Theunissen','Trompsburg','Tweeling','Tweespruit',
        'Van Stadensrus','Ventersburg','Verkeerdevlei','Viljoenskroon','Villiers','Vrede','Vredefort','Warden','Welkom','Wepener','Wesselsbron','Winburg','Zastron',
        ]
        

provinces= ['Mpumalanga', 'KwaZulu-Natal', 'Free State', 'Western Cape', 'Eastern Cape', 'Northern Cape', 'Gauteng', 'North west', 'Limpopo']


def create_person():
    province = provinces[randint(0, len(provinces)-1)]
    print(province)
    if province == 'Northern Cape':
        area = nc[randint(0, len(nc)-1)]
    elif province == 'Eastern Cape':
        area = ec[randint(0, len(ec)-1)]
    elif province == 'Western Cape':
        area = wc[randint(0, len(wc)-1)]
    elif province == 'Limpopo':
        area = l[randint(0, len(l)-1)]
    elif province == 'Mpumalanga':
        area = mp[randint(0, len(mp)-1)]
    elif province == 'KwaZulu-Natal':
        area = kzn[randint(0, len(kzn)-1)]
    elif province == 'Gauteng':
        area = gp[randint(0, len(gp)-1)]
    elif province == 'North west':
        area = nw[randint(0, len(nw)-1)]
    elif province == 'Free State':
        area = fs[randint(0, len(fs)-1)]

    for i in range(len(first_names)):
            reporter_email = first_names[i].lower() + "." + last_names[i].lower() + "@example.com"

    report_person = Person(
                    time = datetime.now() - timedelta(days=randint(0,2), hours=randint(0, 23), minutes=randint(0, 60)),
                    reporter_email = reporter_email,
                    province = province,
                    area = area,
                    street = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(6)),
                    age = ages[randint(0, len(ages)-1)], 
                    build = builds[randint(0, len(builds)-1)],
                    height = heights[randint(0, len(ages)-1)],
                    tone = tones[randint(0, len(tones)-1)],
                    shirt = colours[randint(0, len(colours)-1)],
                    pants = colours[randint(0, len(colours)-1)], 
                    shoes = colours[randint(0, len(colours)-1)],
                    remarks = 'None'
                    )
    db.session.add(report_person)
    db.session.commit()
    return


def create_vehicle():

    province = provinces[randint(0, len(provinces)-1)]

    if province == 'Northern Cape':
        area = nc[randint(0, len(nc)-1)]
    elif province == 'Eastern Cape':
        area = ec[randint(0, len(ec)-1)]
    elif province == 'Western Cape':
        area = wc[randint(0, len(wc)-1)]
    elif province == 'Limpopo':
        area = l[randint(0, len(l)-1)]
    elif province == 'Mpumalanga':
        area = mp[randint(0, len(mp)-1)]
    elif province == 'KwaZulu-Natal':
        area = kzn[randint(0, len(kzn)-1)]
    elif province == 'Gauteng':
        area = gp[randint(0, len(gp)-1)]
    elif province == 'North west':
        area = nw[randint(0, len(nw)-1)]
    elif province == 'Free State':
        area = fs[randint(0, len(fs)-1)]

    for i in range(len(first_names)):
            reporter_email = first_names[i].lower() + "." + last_names[i].lower() + "@example.com"

    report_vehicle = Vehicle(    
                time = datetime.now() - timedelta(days=randint(0,2), hours=randint(0, 23), minutes=randint(0, 60)),
                reporter_email = reporter_email,
                province = province,
                area = area,
                street = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(6)),
                colour = colours[randint(0, len(colours)-1)],
                registration = 'NPS'.join(random.choice(string.ascii_lowercase + string.digits) for i in range(3)),
                occupants = randint(0, 6),
                make = makes[randint(0, len(makes)-1)], 
                model = models[randint(0, len(models)-1)],
                remarks = 'None'
                )
    db.session.add(report_vehicle)
    db.session.commit()
    return


def create_group():

    province = provinces[randint(0, len(provinces)-1)]

    if province == 'Northern Cape':
        area = nc[randint(0, len(nc)-1)]
    elif province == 'Eastern Cape':
        area = ec[randint(0, len(ec)-1)]
    elif province == 'Western Cape':
        area = wc[randint(0, len(wc)-1)]
    elif province == 'Limpopo':
        area = l[randint(0, len(l)-1)]
    elif province == 'Mpumalanga':
        area = mp[randint(0, len(mp)-1)]
    elif province == 'KwaZulu-Natal':
        area = kzn[randint(0, len(kzn)-1)]
    elif province == 'Gauteng':
        area = gp[randint(0, len(gp)-1)]
    elif province == 'North west':
        area = nw[randint(0, len(nw)-1)]
    elif province == 'Free State':
        area = fs[randint(0, len(fs)-1)]

    for i in range(len(first_names)):
            reporter_email = first_names[i].lower() + "." + last_names[i].lower() + "@example.com"

    report_group = Group(
                time = datetime.now() - timedelta(days=randint(0,2), hours=randint(0, 23), minutes=randint(0, 60)), 
                reporter_email = reporter_email,
                province = province,
                area = area,
                street = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(6)),
                number_of_people = randint(0, 20),
                remarks = 'None'
                )
    db.session.add(report_group)
    db.session.commit()
    return


def create_image(image_name):

    province = provinces[randint(0, len(provinces)-1)]

    if province == 'Northern Cape':
        area = nc[randint(0, len(nc)-1)]
    elif province == 'Eastern Cape':
        area = ec[randint(0, len(ec)-1)]
    elif province == 'Western Cape':
        area = wc[randint(0, len(wc)-1)]
    elif province == 'Limpopo':
        area = l[randint(0, len(l)-1)]
    elif province == 'Mpumalanga':
        area = mp[randint(0, len(mp)-1)]
    elif province == 'KwaZulu-Natal':
        area = kzn[randint(0, len(kzn)-1)]
    elif province == 'Gauteng':
        area = gp[randint(0, len(gp)-1)]
    elif province == 'North west':
        area = nw[randint(0, len(nw)-1)]
    elif province == 'Free State':
        area = fs[randint(0, len(fs)-1)]

    for i in range(len(first_names)):
            reporter_email = first_names[i].lower() + "." + last_names[i].lower() + "@example.com"

    report_image = Image(
                time = datetime.now() - timedelta(days=randint(0,2), hours=randint(0, 23), minutes=randint(0, 60)), 
                reporter_email = reporter_email,
                province = province,
                area = area,
                street = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(6)),
                filename = image_name,
                remarks = 'None'
                )
    db.session.add(report_image)
    db.session.commit()
    return


for i in range(25):
    create_person()
    create_vehicle()
    create_group()

for fn in os.listdir('static/uploads'):
    fn = fn.lower()
    if fn.endswith(".jpg") or fn.endswith(".png"):
        filenames.append(fn)
        create_image(fn)
    else:
        pass




#def printer(string):
 #   string=string.lower()
 #   for letter in string:
 #       for key in alphabet:
  #          if letter == key:
 #               print (alphabet[letter][0], end='#')