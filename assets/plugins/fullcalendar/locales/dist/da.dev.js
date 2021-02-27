"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.da = factory()));
})(void 0, function () {
  'use strict';

  var da = {
    code: "da",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "Forrige",
      next: "Næste",
      today: "I dag",
      month: "Måned",
      week: "Uge",
      day: "Dag",
      list: "Agenda"
    },
    weekLabel: "Uge",
    allDayText: "Hele dagen",
    eventLimitText: "flere",
    noEventsMessage: "Ingen arrangementer at vise"
  };
  return da;
});