import React, { useState, useEffect, useRef, useCallback } from "react";
import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";
import EventsSlider from "../EventsSlider/EventsSlider";
import { timelineData } from "../../data/timelineData";
import { TimelinePeriod } from "../../types/timeline";
import "./Timeline.scss";

const RADIUS = 265;

export const degToRad = (deg: number) => (deg * Math.PI) / 180;

const Timeline: React.FC = () => {
  const [activePeriodIndex, setActivePeriod] = useState<number>(5);
  const [animatedStartYear, setAnimatedStartYear] = useState<number>(
    timelineData.periods[5].startYear,
  );
  const [animatedEndYear, setAnimatedEndYear] = useState<number>(
    timelineData.periods[5].endYear,
  );
  const [currentPeriod, setCurrentPeriod] = useState<TimelinePeriod>(
    timelineData.periods[activePeriodIndex],
  );

  const startYearRef = useRef<HTMLHeadingElement>(null);
  const endYearRef = useRef<HTMLHeadingElement>(null);
  const eventsRef = useRef<HTMLDivElement>(null);

  const totalPeriods = timelineData.periods.length;
  const pointsRef = useRef<HTMLDivElement[]>([]);

  useGSAP(
    () => {
      const period = timelineData.periods[activePeriodIndex];

      const startObj = { value: animatedStartYear };
      const endObj = { value: animatedEndYear };

      const setStart = gsap.quickSetter(startObj, "value");
      const setEnd = gsap.quickSetter(endObj, "value");

      gsap.to(startObj, {
        value: period.startYear,
        duration: 1,
        ease: "power2.out",
        onUpdate: () => setAnimatedStartYear(Math.round(startObj.value)),
      });

      gsap.to(endObj, {
        value: period.endYear,
        duration: 1,
        ease: "power2.out",
        onUpdate: () => setAnimatedEndYear(Math.round(endObj.value)),
      });
    },
    { dependencies: [activePeriodIndex] },
  );

  const anglesRef = useRef<number[]>([]);
  // Появление точек после инициализации компонента
  useGSAP(() => {
    const step = 360 / timelineData.periods.length;

    anglesRef.current = timelineData.periods.map(
      (_, index) => index * step - 60,
    );

    pointsRef.current.forEach((point, index) => {
      if (!point) return;

      const angle = anglesRef.current[index];

      gsap.set(point, {
        x: RADIUS + Math.cos(degToRad(angle)) * RADIUS,
        y: RADIUS + Math.sin(degToRad(angle)) * RADIUS,
      });
    });
  }, []);

  // Поворот точек
  useGSAP(
    () => {
      const step = 360 / timelineData.periods.length;

      pointsRef.current.forEach((point, index) => {
        if (!point) return;

        const fromAngle = anglesRef.current[index];
        const toAngle = (index - activePeriodIndex) * step - 60;

        const angleObj = { value: fromAngle };

        gsap.to(angleObj, {
          value: toAngle,
          duration: 1,
          ease: "power2.inOut",
          onUpdate: () => {
            anglesRef.current[index] = angleObj.value;

            gsap.set(point, {
              x: RADIUS + Math.cos(degToRad(angleObj.value)) * RADIUS,
              y: RADIUS + Math.sin(degToRad(angleObj.value)) * RADIUS,
            });
          },
          onComplete: () => {
            if (index === activePeriodIndex) {
              // В прямом направлении активируем лейбл только после завершения поворота
              gsap.set(pointsRef.current[index], {
                className:
                  "timeline__point timeline__point--active timeline__point--label",
              });
            } else {
              gsap.set(pointsRef.current[index], {
                className: "timeline__point",
              });
            }
          },
        });
      });
    },
    { dependencies: [activePeriodIndex] },
  );

  // fade-эффект слайдера
  useGSAP(
    () => {
      if (!eventsRef.current) return;

      gsap
        .timeline()
        .fromTo(
          eventsRef.current,
          {
            autoAlpha: 1,
            y: 0,
          },
          {
            autoAlpha: 0,
            duration: 1,
            y: 0,
            ease: "cubic-bezier(0,.8,0,1)",
          },
        )
        .add(() => {
          setCurrentPeriod(timelineData.periods[activePeriodIndex]);
        })
        .fromTo(
          eventsRef.current,
          {
            autoAlpha: 0,
            y: 10,
          },
          {
            autoAlpha: 1,
            y: 0,
            duration: 0.3,
            ease: "cubic-bezier(0,.8,0,1)",
          },
        );
    },
    { dependencies: [activePeriodIndex] },
  );

  const handlePeriodChange = (index: number) => {
    if (index !== activePeriodIndex) {
      setActivePeriod(index);
    }
  };

  const handleNavigation = (direction: "prev" | "next") => {
    let newIndex = activePeriodIndex;

    if (direction === "prev" && activePeriodIndex > 0) {
      newIndex = activePeriodIndex - 1;
    } else if (direction === "next" && activePeriodIndex < totalPeriods - 1) {
      newIndex = activePeriodIndex + 1;
    }

    if (newIndex !== activePeriodIndex) {
      handlePeriodChange(newIndex);
    }
  };

  return (
    <section className="timeline">
      <div className="timeline__margin_left">
        <svg className="lines" viewBox="0 0 100 100" preserveAspectRatio="none">
          <line
            x1="0"
            y1="0"
            x2="0"
            y2="100"
            stroke="rgba(66, 86, 122, 0.1)"
            strokeWidth="1"
            vectorEffect="non-scaling-stroke"
          />
          <line
            x1="100"
            y1="0"
            x2="100"
            y2="100"
            stroke="rgba(66, 86, 122, 0.1)"
            strokeWidth="1px"
            vectorEffect="non-scaling-stroke"
          />
          <line
            x1="50"
            y1="0"
            x2="50"
            y2="100"
            stroke="rgba(66, 86, 122, 0.1)"
            strokeWidth="1px"
            vectorEffect="non-scaling-stroke"
          />
          <line
            x1="0"
            y1="50"
            x2="100"
            y2="50"
            stroke="rgba(66, 86, 122, 0.1)"
            strokeWidth="1px"
            vectorEffect="non-scaling-stroke"
          />
        </svg>
        <div className="timeline__container">
          <header className="timeline__header">
            <h1 className="timeline__title">
              Исторические
              <br />
              даты
            </h1>
          </header>

          <div className="timeline__content">
            <div className="timeline__years">
              <h2
                ref={startYearRef}
                className="timeline__year timeline__year--start"
              >
                {animatedStartYear}
              </h2>
              <h2
                ref={endYearRef}
                className="timeline__year timeline__year--end"
              >
                {animatedEndYear}
              </h2>
            </div>

            <div className="timeline__circle">
              <svg
                className="timeline__circle-svg"
                width="530"
                height="530"
                viewBox="0 0 530 530"
              >
                <circle
                  cx="265"
                  cy="265"
                  r="265"
                  fill="none"
                  stroke="rgba(66, 86, 122, 0.1)"
                  strokeWidth="1"
                  vectorEffect="non-scaling-stroke"
                />
              </svg>
              {timelineData.periods.map((period, index) => (
                <div
                  key={period.id}
                  ref={(el) => {
                    el ? (pointsRef.current[index] = el) : "";
                  }}
                  className={`timeline__point ${
                    index === activePeriodIndex ? "timeline__point--active" : ""
                  }`}
                  onClick={() => setActivePeriod(index)}
                  data-number={period.id}
                  data-title={period.title}
                />
              ))}
            </div>

            <div className="timeline__navigation">
              <span className="timeline__counter">
                {String(activePeriodIndex + 1).padStart(2, "0")}/
                {String(totalPeriods).padStart(2, "0")}
              </span>
              <div className="timeline__navigation--buttons">
                <button
                  className={`timeline__nav-button ${activePeriodIndex === 0 ? "timeline__nav-button--disabled" : ""}`}
                  onClick={() => handleNavigation("prev")}
                  disabled={activePeriodIndex === 0}
                  key={0}
                >
                  <svg
                    width="9"
                    height="14"
                    viewBox="0 0 9 14"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M7.66418 0.707108L1.41419 6.95711L7.66418 13.2071"
                      stroke="#42567A"
                      strokeWidth="2"
                    />
                  </svg>
                </button>

                <button
                  className={`timeline__nav-button ${activePeriodIndex === totalPeriods - 1 ? "timeline__nav-button--disabled" : ""}`}
                  onClick={() => handleNavigation("next")}
                  disabled={activePeriodIndex === totalPeriods - 1}
                  key={1}
                >
                  <svg
                    width="9"
                    height="14"
                    viewBox="0 0 9 14"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M0.707092 0.707108L6.95709 6.95711L0.707093 13.2071"
                      stroke="#42567A"
                      strokeWidth="2"
                    />
                  </svg>
                </button>
              </div>
            </div>

            <div className="timeline__events" ref={eventsRef}>
              <EventsSlider events={currentPeriod.events} />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Timeline;
