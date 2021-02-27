"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales['ar-ma'] = factory()));
})(void 0, function () {
  'use strict';

  var arMa = {
    code: "ar-ma",
    week: {
      dow: 6,
      doy: 12 // The week that contains Jan 1st is the first week of the year.

    },
    dir: 'rtl',
    buttonText: {
      prev: "السابق",
      next: "التالي",
      today: "اليوم",
      month: "شهر",
      week: "أسبوع",
      day: "يوم",
      list: "أجندة"
    },
    weekLabel: "أسبوع",
    allDayText: "اليوم كله",
    eventLimitText: "أخرى",
    noEventsMessage: "أي أحداث لعرض"
  };
  return arMa;
});