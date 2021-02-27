"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.lt = factory()));
})(void 0, function () {
  'use strict';

  var lt = {
    code: "lt",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "Atgal",
      next: "Pirmyn",
      today: "Šiandien",
      month: "Mėnuo",
      week: "Savaitė",
      day: "Diena",
      list: "Darbotvarkė"
    },
    weekLabel: "SAV",
    allDayText: "Visą dieną",
    eventLimitText: "daugiau",
    noEventsMessage: "Nėra įvykių rodyti"
  };
  return lt;
});