﻿# Generated by Django 4.1.2 on 2023-05-10 14:19

from django.db import migrations

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from datetime import datetime, timedelta
import time

def beginning(apps, schema_editor):
    
    # Суперпользователь id-1
    user = User.objects.create_superuser(username='root',
    email='rest100523@mail.ru',
    password='SsNn5678+-@', 
    last_login=datetime.now())
    print("Суперпользователь создан")
    
    # Группа менеджеров
    managers = Group.objects.get_or_create(name = 'Managers')
    managers = Group.objects.get(name='Managers')
    print("Группа менеджеров создана")
    
    # Пользователь с ролью менеджера id2
    user = User.objects.create_user(username='manager', password='Ss0066+-', email='manager@mail.ru', first_name='Менеджер', last_name='', last_login=datetime.now())
    managers.user_set.add(user)
    print("Менеджер добавлен в группу менеджеров")

    # Простые пользователи (заявители) id3-27
    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Алижан', last_name='Нурмуханов', last_login=datetime.now())
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Алишер', last_name='Базарбаев', last_login=datetime.now())
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Бахтияр', last_name='Турарбеков', last_login=datetime.now())
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Мурат', last_name='Шакиров', last_login=datetime.now())
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Вадим ', last_name='Цаплин', last_login=datetime.now())
    user = User.objects.create_user(username='user6', password='Uu0066+-', email='user6@mail.ru', first_name='Альбина', last_name='Ақмалиева', last_login=datetime.now())
    user = User.objects.create_user(username='user7', password='Uu0066+-', email='user7@mail.ru', first_name='Назерке', last_name='Камзинова', last_login=datetime.now())
    user = User.objects.create_user(username='user8', password='Uu0066+-', email='user8@mail.ru', first_name='Аягоз', last_name='Аманжолова', last_login=datetime.now())
    user = User.objects.create_user(username='user9', password='Uu0066+-', email='user9@mail.ru', first_name='Назира ', last_name='Шамшиева', last_login=datetime.now())
    user = User.objects.create_user(username='user10', password='Uu0066+-', email='user10@mail.ru', first_name='Дина', last_name='Мусагалиева', last_login=datetime.now())
    print("Созданы простые пользователи")

    ###### Страны / регионы / отели / заявки / отзывы #####

    Kind = apps.get_model("center", "Kind")
    Room = apps.get_model("center", "Room")
    Claim = apps.get_model("center", "Claim") 
    Reviews = apps.get_model("center", "Reviews") 
    
    kind = Kind()
    kind.title = 'Standart (однокомнатный, двухместный) (twin)'   
    kind.save()

    room = Room()
    room.kind = kind;
    room.title = '11' 
    room.floor  = 1
    room.details = 'Две односпальные 90*200 кровати, прикроватные тумбы, гардеробный шкаф, холодильник, телевизор, кондиционер, санузел с душевой кабиной. Площадь номера 15кв.м.'
    room.photo  = 'images/room1.jpg'
    room.price = 26000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 3
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Отличная зона отдыха,зелёная все условия для детей и взрослых,пляж близко,питание супер,персонал супер все молодцы такие дружелюбныене .Хозяива зоны тоже классные !Не первый год тут отдыхаем и менять зону отдыха не собираемся! В этом году обязательно приедем)'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    room = Room()
    room.kind = kind;
    room.title = '21' 
    room.floor  = 2
    room.details = 'Две односпальные 90*200 кровати, прикроватные тумбы, гардеробный шкаф, холодильник, телевизор, кондиционер, санузел с душевой кабиной. Площадь номера 15кв.м.'
    room.photo  = 'images/room2.jpg'
    room.price = 26000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=31);
    claim.user_id = 4
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=31);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'СПАСИБО всему персоналу! КУХНЯ замечательная, сервис на высшем уровне! Обязательно приедем в следующем году! Удачи Вам!'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()
            
    kind = Kind()
    kind.title = 'Standart (однокомнатный, двухместный) (double)'   
    kind.save()

    room = Room()
    room.kind = kind;
    room.title = '12' 
    room.floor  = 1
    room.details = 'Номера на первом этаже имеют выход на свою террасу. Двуспальная 160*200 кровать, прикроватные тумбы, гардеробный шкаф,  холодильник, телевизор, кондиционер, санузел с душевой кабиной. Площадь номера 15кв.м.'
    room.photo  = 'images/room3.jpg'
    room.price = 26000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 5
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Отличная зона, кормят на отбой, все вкусно, зелёная зона вежливая администрация, отдельное спасибо официанту Дону, вежливый парень, очень учтивый, и вообще зона чистая ухоженная, чистые номера прекрасная кухня моя оценка1000+'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    room = Room()
    room.kind = kind;
    room.title = '22' 
    room.floor  = 2
    room.details = 'Номера на первом этаже имеют выход на свою террасу. Двуспальная 160*200 кровать, прикроватные тумбы, гардеробный шкаф,  холодильник, телевизор, кондиционер, санузел с душевой кабиной. Площадь номера 15кв.м.'
    room.photo  = 'images/room4.jpg'
    room.price = 26000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=31);
    claim.user_id = 6
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=31);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Всем рекомендуем, отдыхали с женой. Понравилось абсолютно все. Обслуживание на высоком уровне, все вежливы, и добры, кухня очень вкусная. Номера полу люкс вообще отличные. Спасибо владелецу пансионата за уровень, и качество.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    kind = Kind()
    kind.title = 'Lux (двухкомнатный, четырёхместный)'   
    kind.save()

    room = Room()
    room.kind = kind;
    room.title = '13' 
    room.floor  = 1
    room.details = 'Домик из сруба с террасой (двуспальная 160*200 кровать и прикроватные тумбы, гардеробный шкаф, стол со стульями, холодильник, телевизор, кондиционер в каждой комнате, санузел с душевой кабиной, фен) гостиная с мягкой мебелью, электрочайник, кухонная мебель, набор чайной посуды. В гостиной с мягкой мебелью можно организовать 1 доп.мест за 7000 тенге в сутки. Площадь номера 40 кв.м., площадь террасы 8 кв.м.'
    room.photo  = 'images/room5.jpg'
    room.price = 48000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 7
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Зона отдыха очень понравилась, чуткий персонал, в номерах чисто и опрятно, в номерах убирают и меняют постель и полотенца! По еде, очень вкусно и сытно! В общем, не пожалеете, до этого бывали в более дорогие местах, где совсем не понравилось. Спасибо администрации и персоналу за замечательный отдых!!!'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    room = Room()
    room.kind = kind;
    room.title = '14' 
    room.floor  = 1
    room.details = 'Домик из сруба с террасой (двуспальная 160*200 кровать и прикроватные тумбы, гардеробный шкаф, стол со стульями, холодильник, телевизор, кондиционер в каждой комнате, санузел с душевой кабиной, фен) гостиная с мягкой мебелью, электрочайник, кухонная мебель, набор чайной посуды. В гостиной с мягкой мебелью можно организовать 1 доп.мест за 7000 тенге в сутки. Площадь номера 40 кв.м., площадь террасы 8 кв.м.'
    room.photo  = 'images/room6.jpg'
    room.price = 48000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=31);
    claim.user_id = 8
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=31);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Все было круто!!!! Мне понравилось( этот отзыв абсолютно не проплачен)'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    kind = Kind()
    kind.title = 'Lux (трёхкомнатный, шестиместный)'   
    kind.save()

    room = Room()
    room.kind = kind;
    room.title = '15' 
    room.floor  = 1
    room.details = 'Домик из сруба с террасой ( две односпальные 90*200 и двуспальная 160*200 кровать, прикроватные тумбы, гардеробный шкаф, стол со стульями, набор столовой и чайной посуды, холодильник, телевизор, кондиционер в каждой комнате, санузел с душевой кабиной, фен). Гостиная с мягкой мебелью, СВЧ-печь, электрочайник, кухонная мебель. В гостиной с мягкой мебелью можно организовать 2 доп.мест за 7000 тенге в сутки за каждое доп.место. Площадь номера 57кв.м., площадь террассы 11 кв.м..'
    room.photo  = 'images/room7.jpg'
    room.price = 72000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 9
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Отличное питание, вежливый персонал, чистые и уютные номера. Спасибо'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    room = Room()
    room.kind = kind;
    room.title = '16' 
    room.floor  = 1
    room.details = 'Домик из сруба с террасой ( две односпальные 90*200 и двуспальная 160*200 кровать, прикроватные тумбы, гардеробный шкаф, стол со стульями, набор столовой и чайной посуды, холодильник, телевизор, кондиционер в каждой комнате, санузел с душевой кабиной, фен). Гостиная с мягкой мебелью, СВЧ-печь, электрочайник, кухонная мебель. В гостиной с мягкой мебелью можно организовать 2 доп.мест за 7000 тенге в сутки за каждое доп.место. Площадь номера 57кв.м., площадь террассы 11 кв.м..'
    room.photo  = 'images/room8.jpg'
    room.price = 72000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=31);
    claim.user_id = 10
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=31);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Хорошо отдохнули! Номера очень уютные и комфортабельные. Еда по домашнему очень вкусная! Спасибо Салтанат и всему персоналу. Надеемся отдохнуть у вас в следующем году.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    kind = Kind()
    kind.title = 'Lux (пятикомнатный, восьмиместный) '   
    kind.save()

    room = Room()
    room.kind = kind;
    room.title = '17' 
    room.floor  = 1
    room.details = 'Коттедж из сруба (четыре двуспальные 180*200 кровать, раскладной диван в двух спальнях,прикроватные тумбы, гардеробный шкаф, сплит система в каждой спальне). Большая гостиная оборудована кухонным уголком набором посуды с мягкой мебелью, стол со стульями, большим холодильником, плоским телевизором, электрочайником и микроволновой печью. Два санузела с душевыми кабинами, фен. В гостиной с мягкой мебелью можно организовать 2 доп.мест за 7000 тенге в сутки за каждое доп.место. Площадь коттеджа 160в.м.'
    room.photo  = 'images/room9.jpg'
    room.price = 140000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=30);
    claim.user_id = 11
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Отличная зона отдыха. Трехразовое питание, вкусно и порции хорошие, чисто и уютно, сразу видно за территорией ухаживают, бассейны чистят ежедневно, вода прям чистейшая. Персонал добрый и отзывчивый. Номера хорошие. Озеро находится очень близко, берег чистый. Отдохнули просто отлично. Дети получили массу положительных эмоций. Мы благодарны вам за такие хорошие выходные. Дальнейшего вам процветания. Мы теперь ваши постоянные клиенты.'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    room = Room()
    room.kind = kind;
    room.title = '18' 
    room.floor  = 1
    room.details = 'Коттедж из сруба (четыре двуспальные 180*200 кровать, раскладной диван в двух спальнях,прикроватные тумбы, гардеробный шкаф, сплит система в каждой спальне). Большая гостиная оборудована кухонным уголком набором посуды с мягкой мебелью, стол со стульями, большим холодильником, плоским телевизором, электрочайником и микроволновой печью. Два санузела с душевыми кабинами, фен. В гостиной с мягкой мебелью можно организовать 2 доп.мест за 7000 тенге в сутки за каждое доп.место. Площадь коттеджа 160в.м.'
    room.photo  = 'images/room10.jpg'
    room.price = 140000
    room.save()

    claim = Claim()
    #claim.datec = datetime.now() - timedelta(days=31);
    claim.user_id = 12
    claim.room = room
    claim.start  = datetime.now() - timedelta(days=27);
    claim.finish  = datetime.now() - timedelta(days=20);
    claim.details = ''
    claim.result =  'Ваша заявка одобрена'
    claim.save()
    claim.datec = datetime.now() - timedelta(days=30);
    claim.save()

    reviews = Reviews()
    #reviews.dater = claim.finish;
    reviews.room = room
    reviews.user = claim.user
    reviews.rating = 5
    reviews.details = 'Классный отдых! Спасибо за все, Айдос Ага! летом еще раз поедим'
    reviews.save()
    reviews.dater = claim.finish;
    reviews.save()

    print("Kind, Room, Claim, Reviews Ok")
    
    ##### Новости #####
    News = apps.get_model("center", "News")
    
    news = News()
    news.daten = datetime.now() - timedelta(days=35)
    news.title = 'КТЖ организует более 270 тысяч пассажирских мест в поездах до Алаколя'
    news.details = """Количество пассажирских мест в поездах, отправляющихся на озеро Алаколь, на летний туристический сезон в 2023 году вырастет на 6 процентов по сравнению с аналогичным периодом прошлого года. Пассажирам будет предложено более 276 тысяч мест. В направлении озера Алаколь продолжат курсировать пассажирские поезда по 11 маршрутам из Астаны, Алматы, Восточно-Казахстанской и Абайской областей. Впервые запустят поезд "Тальго" по маршруту "Астана-Достык".
    В данный момент АО "Пассажирские перевозки" рассматривает совместно с акиматами, авиа- и автоперевозчиками и туроператорами возможность формирования интермодальных перевозок (двумя или более видами транспорта) до озера Алаколь из городов Шымкент, Павлодар, Усть-Каменогорск, Кызылорда.
    """
    news.photo = 'images/news1.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=30)
    news.title = 'Поезд "Тальго" запустят до Алаколя из Астаны'
    news.details =  """Для удобства туристов до озера Алаколь запустят поезд "Тальго". Об этом сообщили в пресс-службе НК "Қазақстан темір жолы", передает Tengritravel.kz.
    Как проинформировали в нацкомпании, в 2023 году в направлении озера Алаколь продолжат курсировать 11 маршрутов из Астаны, Алматы, Восточно-Казахстанской и Абайской областей. Впервые запустят поезд "Тальго" по маршруту Астана - Достык.
    """
    news.photo = 'images/news2.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=25)
    news.title = 'Дороги к популярным курортным зонам отремонтируют в Казахстане'
    news.details = """Туристскую инфраструктуру существенно модернизируют в Казахстане, передает Tengritravel.kz со ссылкой на сайт премьер-министра.
    "Предполагается провести строительство и реконструкцию автодорог к курортным зонам Балхаш, Капшагай, Алаколь и Баянаул, на 100 процентов покрыть зоны отдыха мобильной связью, провести необходимые инженерные сети в Щучинско-Боровской курортной зоне, построить дополнительные водно-спасательные станции на водоемах", - говорится в сообщении
    """
    news.photo = 'images/news3.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=20)
    news.title = 'Увеличить поток иностранных туристов до 4 миллионов человек планируют в Казахстане'
    news.details = """Проект концепции развития туристической отрасли на 2023-2029 годы рассмотрели на совещании под председательством премьер-министра Алихана Смаилова, сообщает Tengritravel.kz со ссылкой на primeminister.kz.
    Как сообщил министр культуры и спорта Асхат Оралов, для развития туристической отрасли планируется реализовать меры по модернизации инфраструктуры в 10 основных турдестинациях республики, повышению качества сервиса, продвижению туристического потенциала страны на международной арене и так далее.
    Так, предполагается провести строительство и реконструкцию автодорог к курортным зонам Балхаш, Капшагай, Алаколь и Баянаул, на 100 процентов покрыть зоны отдыха мобильной связью, провести необходимые инженерные сети в Щучинско-Боровской курортной зоне, построить дополнительные водно-спасательные станции на водоемах.
    """
    news.photo = 'images/news4.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=15)
    news.title = 'Токаев назвал уникальные места для развития экологического туризма'
    news.details = """Президент Касым-Жомарт Токаев назвал уникальные места в Казахстане для развития экологического туризма, передает Tengritravel.kz.
    "В Казахстане очень много достопримечательностей. Мы должны использовать это рационально. Акимату Жетысуской области необходимо уделить особое внимание развитию туризма. Особенно Алаколь и Балхаш имеют огромный потенциал.
    Национальный парк "Алтын-Эмель" и Жонгар-Алатауский государственный национальный природный парк – это уникальные места для развития экологического туризма. Знаменитые ущелья Шаджа и Кора в Текели полны великолепных видов. Вот и все - богатство, которое оседает.
    Конечно, для посещения большого количества туристов необходимо построить соответствующую инфраструктуру и создать комфортные условия. Это непростая задача. За последние годы в этом направлении проделана значительная работа. Но этим нельзя ограничиваться", - отметил Глава государства.
    """
    news.photo = 'images/news5.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=10)
    news.title = 'Сколько человек добрались до Алаколя на поезде этим летом'
    news.details = """В "Қазақстан темір жолы" подвели итоги летних перевозок в направлении курортной зоны Алаколь. По подсчетам ведомства, свыше 240 тысяч пассажиров перевезли железнодорожным транспортом до озера Алаколь, передает Tengritravel.kz.
    В направлении Алаколь курсировало 11 пассажирских поездов, из них 9 - АО "Пассажирские перевозки", 2 - частных перевозчика. Три состава отправлялись из Астаны, пять - из Алматы, а также два - из Восточно-Казахстанской и Абайской областей и пригородный поезд из Актогай - Достык. Также впервые в этом году по двум маршрутам были задействованы пассажирские составы, сформированные вагонами "Тальго".
    "За три летних месяца в направлении озера Алаколь перевезли 243 тысячи пассажиров, что на 33,5 процента больше, чем прошлым летом. Чтобы удовлетворить спрос, было предложено свыше 260 тысяч мест, что на 8 процентов выше в сравнении с прошлым годом", - говорится в сообщении.
    """
    news.photo = 'images/news6.jpeg' 
    news.save()
    
    news = News()
    news.daten = datetime.now() - timedelta(days=5)
    news.title = 'Острова на Алаколе: какие из них доступны туристам'
    news.details = """Алаколь летом – одно из любимейших направлений для внутреннего туризма в Казахстане. Привлекает горько-соленое бессточное озеро и иностранцев. С каждым годом число гостей растет, но далеко не каждый из них знает о существовании Алакольского государственного природного заповедника, и потому встает вопрос: какие территории доступны для посещения, а какие – нет. Подробнее – в материале Tengritravel.kz.
    Не так давно мы писали о том, как один из туристов, отдыхающий в поселке Акши, решил совершить водную прогулку по озеру Алаколь, так как его заинтересовали острова вдалеке. Мужчина договорился с владельцем катера, и тот его отвез. Турист сделал серию фотоснимков и только после того, как выложил их в Сеть, узнал, что острова на Алаколе – заповедная зона. Примечательно было даже не то, что владелец катера легко согласился совершить водную прогулку в данном направлении, а то, что на самом острове не было ни охраны, ни постов, ни шлагбаумов, ни табличек, запрещающих нахождение на острове.
    """
    news.photo = 'images/news7.jpeg' 
    news.save()
    
    print("News Ok")

class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
         migrations.RunPython(beginning),       
         migrations.RunSQL("""CREATE VIEW view_room AS
                        SELECT room.id, room.kind_id, kind.title AS kind, room.title, room.floor, room.details, room.photo, room.price, (SELECT AVG(rating) FROM reviews WHERE reviews.room_id = room.id) AS avg_rating 
                        FROM room LEFT JOIN kind ON room.kind_id = kind.id;"""),

    ]
