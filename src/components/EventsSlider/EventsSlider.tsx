import React, { useEffect, useState } from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, EffectFade } from 'swiper/modules';
import type { Swiper as SwiperType } from 'swiper';
import { type TimelineEvent } from '../../types/timeline';
import 'swiper/css';
import 'swiper/css/navigation';
import './EventsSlider.scss';

interface EventsSliderProps {
  events: TimelineEvent[];
}

const EventsSlider: React.FC<EventsSliderProps> = ({ events }) => {
  const [swiperInstance, setSwiperInstance] = useState<SwiperType | null>(null);

  useEffect(() => {
    if (swiperInstance) {
      swiperInstance.slideTo(0, 0); // 0 - индекс слайда, 0 - скорость (мгновенно)
    }
  }, [events, swiperInstance]);

  return (
    <div className="events-slider">
      <div className="events-slider__container">
        <Swiper
          onSwiper={setSwiperInstance}
          modules={[Navigation, EffectFade]}
          spaceBetween={80}
          slidesPerView={3}
          allowTouchMove={true}
          grabCursor={true}
          fadeEffect={{ crossFade: true }}
          navigation={{
            nextEl: '.events-slider .swiper-button-next',
            prevEl: '.events-slider .swiper-button-prev',
          }}
          breakpoints={{
            320: {
              slidesPerView: 1.2,
              spaceBetween: 25,
            },
            768: {
              slidesPerView: 2,
              spaceBetween: 40,
            },
            1024: {
              slidesPerView: 3,
              spaceBetween: 40,
            },
          }}
        >
          {events.map((event, index) => (
            <SwiperSlide key={`${event.year}-${index}`} className="events-slider__slide">
              <div className="events-slider__event">
                <div className="events-slider__event__year">{event.year}</div>
                <div className="events-slider__event__title">{event.title}</div>
              </div>
            </SwiperSlide>
          ))}
          <div className="swiper-button-next"></div>
          <div className="swiper-button-prev"></div>
        </Swiper>
      </div>
    </div>
  );
};

export default EventsSlider;
