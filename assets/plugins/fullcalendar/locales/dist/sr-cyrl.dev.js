"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales['sr-cyrl'] = factory()));
})(void 0, function () {
  'use strict';

  var srCyrl = {
    code: "sr-cyrl",
    week: {
      dow: 1,
      doy: 7 // The week that contains Jan 1st is the first week of the year.

    },
    buttonText: {
      prev: "Претходна",
      next: "следећи",
      today: "Данас",
      month: "Месец",
      week: "Недеља",
      day: "Дан",
      list: "Планер"
    },
    weekLabel: "Сед",
    allDayText: "Цео дан",
    eventLimitText: function eventLimitText(n) {
      return "+ још " + n;
    },
    noEventsMessage: "Нема догађаја за приказ"
  };
  return srCyrl;
});