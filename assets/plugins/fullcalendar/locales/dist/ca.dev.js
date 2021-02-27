"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.ca = factory()));
})(void 0, function () {
  'use strict';

  var ca = {
    code: "ca",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "Anterior",
      next: "Següent",
      today: "Avui",
      month: "Mes",
      week: "Setmana",
      day: "Dia",
      list: "Agenda"
    },
    weekLabel: "Set",
    allDayText: "Tot el dia",
    eventLimitText: "més",
    noEventsMessage: "No hi ha esdeveniments per mostrar"
  };
  return ca;
});