"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.sv = factory()));
})(void 0, function () {
  'use strict';

  var sv = {
    code: "sv",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "Förra",
      next: "Nästa",
      today: "Idag",
      month: "Månad",
      week: "Vecka",
      day: "Dag",
      list: "Program"
    },
    weekLabel: "v.",
    allDayText: "Heldag",
    eventLimitText: "till",
    noEventsMessage: "Inga händelser att visa"
  };
  return sv;
});