import csv
import requests

waterfalls = [
        {
                'loc': (43.242972, 25.033299),
                'name': 'Крушунски водопади'
            },
        {
                'loc': (42.412941, 22.684916),
                'name': 'Водопад Полска Скакавица'
            },
        {
                'loc': (43.011086, 23.747761),
                'name': 'Водопад Скочи вода'
            },
        {
                'loc': (42.67277, 24.75262),
                'name': 'Сопотски водопад'
            },
        {
                'loc': (42.504427, 22.755390),
                'name': 'Пещерски Водопад'
            },
        {
                'loc': (43.013370, 23.252584),
                'name': 'Добравишка скакля'
            },
        {
                'loc': (43.003318, 22.958265),
                'name': 'Водопад Котлите'
            },
        {
                'loc': (42.208524, 23.177464),
                'name': 'Бистришки водопад'
            },
        {
                'loc': (42.862466, 22.701349),
                'name': 'Врабчански водопад'
            },
        {
                'loc': (42.607987, 23.311296),
                'name': 'Алековите Водопади'
            },
        {
                'loc': (42.838670, 22.716799),
                'name': 'Драговско врело'
            },
        {
                'loc': (43.151886, 23.504769),
                'name': 'Водопад Боров Камък'
            },
        {
                'loc': (42.220151, 23.306283),
                'name': 'Водопад Рилска Скакавица'
            },
        {
                'loc': (42.452824, 25.446514),
                'name': 'Водопад Казането'
            },
        {
                'loc': (42.644981, 25.549012),
                'name': 'Мъглижки Водопад'
            },
        {
                'loc': (41.438187, 25.213268),
                'name': 'Водопад Герме бунар'
            },
        {
                'loc': (41.437068, 25.246877),
                'name': 'Водопад Марф'
            },
        {
                'loc': (41.752562, 24.352439),
                'name': 'Водопад Самодивско пръскало'
            },
        {
                'loc': (41.586285, 24.631458),
                'name': 'Водопад Орфей'
            },
        {
                'loc': (41.440709, 25.223621),
                'name': 'Водопади Желъдово'
            },
        {
                'loc': (43.145777, 25.514629),
                'name': 'Хотнишки водопад'
            },
        {
                'loc': (41.940264, 24.859309),
                'name': 'Бачковски водопад'
            },
        {
                'loc': (42.736190, 24.953690),
                'name': 'Видимско пръскало'
            },
        {
                'loc': (42.758852, 24.608118),
                'name': 'Сувчарско пръскало'
            },
        {
                'loc': (42.824063, 24.038887),
                'name': 'Етрополски водопад Варовитец'
            },
        {
                'loc': (43.035506, 23.330590),
                'name': 'Водопад Бовска Скакля'
            },
        {
                'loc': (42.728018, 25.025427),
                'name': 'Кадемлийско пръскало'
            },
        {
                'loc': (41.892068, 24.385401),
                'name': 'Фотински водопади'
            },
        {
                'loc': (42.720123, 26.357074),
                'name': 'Водопад Футула'
            },
        {
                'loc': (42.731425, 25.910870),
                'name': 'Водопад Скоковете'
            },
        {
                'loc': (43.337442, 22.836708),
                'name': 'Копренски водопади'
            },
        {
                'loc': (43.356896, 22.816640),
                'name': 'Чипровски водопад'
            },
        {
                'loc': (42.691765, 25.043356),
                'name': 'Водопад Дяволска черква'
            },
        {
                'loc': (43.141542, 25.368950),
                'name': 'Момин скок'
            },
        {
                'loc': (43.150817, 25.328261),
                'name': 'Зараповски водопад'
            },
        {
                'loc': (42.889585, 24.250528),
                'name': 'Водопад Скока'
            },
        {
                'loc': (42.644546, 25.565679),
                'name': 'Водопад Стълбата'
            }
    ]

caves =  [
        {
                'loc': (43.011553, 23.750223),
                'name': 'Липнишка пещера Очите'
            },
        {
                'loc': (43.011204, 23.746216),
                'name': 'Пещера Водната пещ'
            },
        {
                'loc': (42.739636, 25.396500),
                'name': 'Бузлуджанската пещера'
            },
        {
                'loc': (42.508419, 25.635128),
                'name': 'Пещера Змееви дупки'
            },
        {
                'loc': (42.698857, 26.357549),
                'name': 'Змееви дупки Сливен'
            },
        {
                'loc': (43.204606, 23.493411),
                'name': 'Пещера Леденика'
            },
        {
                'loc': (43.630254, 22.736446),
                'name': 'Пещера Венеца'
            },
        {
                'loc': (41.628729, 24.329681),
                'name': 'Ягодинска пещера'
            },
        {
                'loc': (43.233655, 24.885262),
                'name': 'Деветашка пещера'
            },
        {
                'loc': (43.727638, 22.582709),
                'name': 'Пещера Магура'
            },
        {
                'loc': (43.176885, 24.072753),
                'name': 'Пещера Проходна'
            },
        {
                'loc': (41.614669, 24.379267),
                'name': 'Пещера Дяволското гърло'
            },
        {
                'loc': (42.947068, 25.430284),
                'name': 'Пещера Бачо Киро'
            },
        {
                'loc': (42.002711, 24.277352),
                'name': 'Пещера Снежанка'
            },
        {
                'loc': (43.217571, 24.973323),
                'name': 'Пещера Стълбицата'
            },
        {
                'loc': (43.244941, 25.029307),
                'name': 'Пещера Урушка Маара'
            },
        {
                'loc': (42.495909, 23.195845),
                'name': 'Пещерата Духлата'
            },
        {
                'loc': (42.525148, 23.202646),
                'name': 'Пещера Живата вода'
            },
        {
                'loc': (43.310400, 24.112938),
                'name': 'Капанът на времето'
            }
        ]

mountains = [
        {
                'loc': (42.462233, 25.600796),
                'name': 'Връх Купеларица'
            },
        {
                'loc': (42.435523, 25.573873),
                'name': 'Черен Острец'
            },
        {
                'loc': (42.511510, 25.629451),
                'name': 'Връх Бетер'
            },
        {
                'loc': (43.134154, 23.196295),
                'name': 'Връх Тодорини Кукли'
            },
        {
                'loc': (42.843425, 22.709840),
                'name': 'Връх Драговски Камък'
            },
        {
                'loc': (42.173891, 23.363075),
                'name': 'Връх Мальовица'
            },
        {
                'loc': (42.179282, 23.585325),
                'name': 'Връх Мусала'
            },
        {
                'loc': (42.588680, 23.246938),
                'name': 'Връх Конярника'
            },
        {
                'loc': (42.611971, 23.276648),
                'name': 'Връх Камен Дел'
            },
        {
                'loc': (42.833037, 23.668500),
                'name': 'Връх Мургаш'
            },
        {
                'loc': (42.756105, 22.753623),
                'name': 'Връх Любаш'
            },
        {
                'loc': (42.541190, 25.756864),
                'name': 'Връх Морулей'
            },
        {
                'loc': (43.173996, 23.052170),
                'name': 'Връх Ком'
            },
        {
                'loc': (42.344045, 22.839494),
                'name': 'Връх Виден'
            },
        {
                'loc': (42.862915, 22.575467),
                'name': 'Връх Руй'
            },
        {
                'loc': (42.474419, 25.636555),
                'name': 'Чичек баир'
            }
    ]

markers = [
        {
                'loc': (42.862697, 22.649117),
                'name': 'Ждрелото на река Ерма Църквището'
            },
        {
                'loc': (42.260796, 23.642923),
                'name': 'Черната скала'
            },
        {
                'loc': (41.818587, 24.581803),
                'name': 'Чудните мостове'
            },
        {
                'loc': (42.468406, 25.610114),
                'name': 'Средновековен Манастир'
            },
        {
                'loc': (42.440906, 25.622905),
                'name': 'Извънземната полянка'
            },
        {
                'loc': (42.420769, 25.599447),
                'name': 'Апаратна Камера тръбата'
            },
        {
                'loc': (42.754586, 27.719095),
                'name': 'Секретен Обект А'
            },
        {
                'loc': (42.860238, 22.680814),
                'name': 'Ябланишкото Ждрело'
            },
        {
                'loc': (42.356893, 23.922448),
                'name': 'Крепост Траянови Врата'
            },
        {
                'loc': (42.297095, 23.534556),
                'name': 'Крепост Шишманово Кале'
            },
        {
                'loc': (42.197954, 23.311285),
                'name': 'Седемте рилски езера'
            },
        {
                'loc': (41.470273, 25.225727),
                'name': 'Крепост Устра'
            },
        {
                'loc': (41.715798, 25.464589),
                'name': 'град Перперикон'
            },
        {
                'loc': (42.638270, 25.793906),
                'name': 'Крепост Асара Николаево'
            },
        {
                'loc': (42.480532, 25.598638),
                'name': 'Крепост Българското кале'
            },
        {
                'loc': (42.581873, 25.189959),
                'name': 'Гьоз тепе'
            },
        {
                'loc': (43.175009, 27.447651),
                'name': 'Крепост Овеч'
            },
        {
                'loc': (43.197504, 27.504069),
                'name': 'Кара пещера'
            },
        {
                'loc': (42.992024, 23.820320),
                'name': 'Боженишки Урвич'
            },
        {
                'loc': (42.945578, 23.878859),
                'name': 'Крепост Боровец'
            }
    ]

def tokml(data):
    from simplekml import Kml
    kml = Kml(name='points')
    for d in data:
        folder = kml.newfolder(name=d.get('folder'))
        folder.iconstyle.icon.href=d.get('icon')
        for p in d.get('points'):
            pt = folder.newpoint(name=p.get('name'))
            loc = p.get('loc')
            pt.coords = [(loc[1], loc[0], p.get('altitude', 0))]
            pt.description =p.get('description', 'none')
            pt.style = folder.style

    kml.save('points.kml')
    kml.savekmz('points.kmz')

def tocsv(data):
    csvdata = []
    fields = ['name','description','latitude','longitude','altitude', 'type']
    for d in data:
        type = d.get('type')
        for p in d.get('points'):
            loc = p.get('loc')
            csvdata.append(
                    {
                            'name': p.get('name'),
                            'description': p.get('description', 'none'),
                            'latitude': loc[0],
                            'longitude': loc[1],
                            'altitude': p.get   ('altitude', 0),
                            'type': type,
                        }
                )

    with open('points.csv', 'w', newline='\n') as f:
        writer = csv.DictWriter(
            f,
            delimiter='|',
            quoting=csv.QUOTE_ALL,
            fieldnames=fields)
        writer.writeheader()
        writer.writerows(csvdata)

if __name__ == '__main__':
    repeaters = []
    kml_data = []
    resp = requests.get('https://varna.radio/reps.json')
    data = resp.json()
    cm200 = 10
    cm70 = 50

    def analog_filter(x):
        k, v = x
        return 'analog' in v.get('mode')

    def analog_rx(x):
        k, v = x
        return v.get('rx')

    for name, data in sorted([x for x in filter(analog_filter, sorted(data.get('repeaters').items(), key=lambda x: x[0]))], key=analog_rx):
        if data.get('disabled'):
            continue

        if 400 > data.get('rx'):
            desc = 'm %d' % cm200
            cm200 += 1
        else:
            desc = 'm %d' % cm70
            cm70 += 1

        desc += ' %s %s %s %s' % ('rx', data.get('rx'), 'tx', data.get('tx'))
        if 'tone' in data:
            desc += ' %s %s' % ('tone', data.get('tone'))

        loc = data.get('locExtra')
        if loc:
            desc += ' %s' % (loc)
        desc += ' %s' % (data.get('loc'))
        desc += ' %s' % (data.get('recordUpdated'))

        repeaters.append(
                {
                        'name': name,
                        'description': desc,
                        'loc': (data.get('lat'), data.get('lon')),
                        'altitude': data.get('altitude', 0)
                    }
            )

    kml_data.append(
                            {
                                    'folder': 'repeaters',
                                    'points': repeaters,
                                    'icon': 'https://img.icons8.com/hatch/100/radio-tower.png',
                                    'type': 51
                                }
                        )

    kml_data.append(
                            {
                                    'folder': 'caves',
                                    'points': caves,
                                    'icon': 'https://img.icons8.com/glyph-neue/100/cave.png',
                                    'type': 91,
                                }
                        )

    kml_data.append(
                            {
                                    'folder': 'mountains',
                                    'points': mountains,
                                    'icon': 'https://img.icons8.com/fluency-systems-filled/100/mountain.png',
                                    'type': 91,
                                }
                        )

    kml_data.append(
                            {
                                    'folder': 'waterfalls',
                                    'points': waterfalls,
                                    'icon': 'https://img.icons8.com/fluency-systems-filled/100/mountain.png',
                                    'type': 91,
                                }
                        )

    kml_data.append(
                            {
                                    'folder': 'markers',
                                    'points': markers,
                                    'icon': 'https://img.icons8.com/windows/100/map-marker--v1.png',
                                    'type': 91,
                                }
                        )

    tocsv(kml_data)
    tokml(kml_data)
