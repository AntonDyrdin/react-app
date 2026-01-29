import { type TimelineData } from '../types/timeline';

export const timelineData: TimelineData = {
  periods: [
    {
      id: 1,
      title: 'Технологии',
      startYear: 1980,
      endYear: 1986,
      events: [
        {
          year: 1980,
          title: 'Создание первого персонального компьютера',
          description: 'IBM выпустила свой первый персональный компьютер IBM PC'
        },
        {
          year: 1981,
          title: 'Появление MS-DOS',
          description: 'Microsoft выпустила операционную систему MS-DOS'
        },
        {
          year: 1983,
          title: 'Интернет протокол TCP/IP',
          description: 'Стандартизация протокола TCP/IP для сети ARPANET'
        }
      ]
    },
    {
      id: 2,
      title: 'Кино',
      startYear: 1987,
      endYear: 1991,
      events: [
        {
          year: 1987,
          title: 'Выход фильма "Хищник"',
          description: 'Арнольд Шварценеггер в роли майора Датча Шеффера'
        },
        {
          year: 1989,
          title: 'Бэтмен Тима Бертона',
          description: 'Майкл Китон в роли Бэтмена, Джек Николсон в роли Джокера'
        },
        {
          year: 1991,
          title: 'Терминатор 2',
          description: 'Продолжение культовой франшизы с революционными спецэффектами'
        }
      ]
    },
    {
      id: 3,
      title: 'Литература',
      startYear: 1992,
      endYear: 1997,
      events: [
        {
          year: 1992,
          title: 'Публикация романа "Игра престолов"',
          description: 'Джордж Мартин начал серию "Песнь льда и пламени"'
        },
        {
          year: 1995,
          title: 'Выход "Гарри Поттера"',
          description: 'Дж. К. Роулинг опубликовала первую книгу о юном волшебнике'
        },
        {
          year: 1997,
          title: 'Нобелевская премия Дарио Фо',
          description: 'Итальянский драматург получил Нобелевскую премию по литературе'
        }
      ]
    },
    {
      id: 4,
      title: 'Театр',
      startYear: 1999,
      endYear: 2004,
      events: [
        {
          year: 1999,
          title: 'Премьера мюзикла "Мамма Миа!"',
          description: 'Мюзикл на песни группы ABBA дебютировал в Лондоне'
        },
        {
          year: 2001,
          title: 'Открытие нового театра',
          description: 'В Москве открылся Театр Наций'
        },
        {
          year: 2003,
          title: 'Премьера "Продюсеров"',
          description: 'Мюзикл Мела Брукса стал хитом Бродвея'
        }
      ]
    },
    {
      id: 5,
      title: 'Спорт',
      startYear: 2006,
      endYear: 2014,
      events: [
        {
          year: 2008,
          title: 'Олимпиада в Пекине',
          description: 'XXIX летние Олимпийские игры в Китае'
        },
        {
          year: 2010,
          title: 'Чемпионат мира по футболу',
          description: 'Первый чемпионат мира по футболу в Африке (ЮАР)'
        },
        {
          year: 2014,
          title: 'Зимняя Олимпиада в Сочи',
          description: 'XXII зимние Олимпийские игры в России'
        }
      ]
    },
    {
      id: 6,
      title: 'Наука',
      startYear: 2015,
      endYear: 2022,
      events: [
        {
          year: 2015,
          title: '13 сентября — частное солнечное затмение',
          description: 'видимое в Южной Африке и части Антарктиды'
        },
        {
          year: 2016,
          title: 'Телескоп «Хаббл» обнаружил самую удалённую галактику',
          description: 'получившую обозначение GN-z11'
        },
        {
          year: 2017,
          title: 'Компания Tesla официально представила',
          description: 'первый в мире электрический грузовик Tesla Semi'
        }
      ]
    }
  ]
};
