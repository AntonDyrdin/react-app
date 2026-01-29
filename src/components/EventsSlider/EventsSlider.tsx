import React, { useEffect, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation, EffectFade } from "swiper/modules";
import type { Swiper as SwiperType } from "swiper";
import { type TimelineEvent } from "../../types/timeline";
import "swiper/css";
import "swiper/css/navigation";
import "./EventsSlider.scss";

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
    <div className="row">
      <Swiper
        className="events-slider"
        onSwiper={setSwiperInstance}
        spaceBetween={80}
        slidesPerView={"auto"}
        allowTouchMove={true}
        grabCursor={true}
        modules={[Navigation]}
        navigation={{
          nextEl: "#swiper-button-next",
          prevEl: "#swiper-button-prev",
        }}
      >
        {events.map((event, index) => (
          <SwiperSlide
            key={`${event.year}-${index}`}
            className="events-slider__slide"
          >
            <div className="events-slider__event">
              <div className="events-slider__event__year">{event.year}</div>
              <div className="events-slider__event__title">{event.title}</div>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
      <button id="swiper-button-next">
        <svg viewBox="0 0 8 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M0.707093 0.707092L5.70709 5.70709L0.707093 10.7071"
            stroke="#3877EE"
            strokeWidth="2"
          />
        </svg>
      </button>
      <button id="swiper-button-prev">
        <svg viewBox="0 0 8 12" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M0.707093 0.707092L5.70709 5.70709L0.707093 10.7071"
            stroke="#3877EE"
            strokeWidth="2"
          />
        </svg>
      </button>
    </div>
  );
};

export default EventsSlider;
