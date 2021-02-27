"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.kk = factory()));
})(void 0, function () {
  'use strict';

  var kk = {
    code: "kk",
    week: {
      dow: 1,
      doy: 7 // The week that contains Jan 1st is the first week of the year.

    },
    buttonText: {
      prev: "Алдыңғы",
      next: "Келесі",
      today: "Бүгін",
      month: "Ай",
      week: "Апта",
      day: "Күн",
      list: "Күн тәртібі"
    },
    weekLabel: "Не",
    allDayText: "Күні бойы",
    eventLimitText: function eventLimitText(n) {
      return "+ тағы " + n;
    },
    noEventsMessage: "Көрсету үшін оқиғалар жоқ"
  };
  return kk;
});