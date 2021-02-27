"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.fa = factory()));
})(void 0, function () {
  'use strict';

  var fa = {
    code: "fa",
    week: {
      dow: 6,
      doy: 12 // The week that contains Jan 1st is the first week of the year.

    },
    dir: 'rtl',
    buttonText: {
      prev: "قبلی",
      next: "بعدی",
      today: "امروز",
      month: "ماه",
      week: "هفته",
      day: "روز",
      list: "برنامه"
    },
    weekLabel: "هف",
    allDayText: "تمام روز",
    eventLimitText: function eventLimitText(n) {
      return "بیش از " + n;
    },
    noEventsMessage: "هیچ رویدادی به نمایش"
  };
  return fa;
});