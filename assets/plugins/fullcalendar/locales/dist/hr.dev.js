"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.hr = factory()));
})(void 0, function () {
  'use strict';

  var hr = {
    code: "hr",
    week: {
      dow: 1,
      doy: 7 // The week that contains Jan 1st is the first week of the year.

    },
    buttonText: {
      prev: "Prijašnji",
      next: "Sljedeći",
      today: "Danas",
      month: "Mjesec",
      week: "Tjedan",
      day: "Dan",
      list: "Raspored"
    },
    weekLabel: "Tje",
    allDayText: "Cijeli dan",
    eventLimitText: function eventLimitText(n) {
      return "+ još " + n;
    },
    noEventsMessage: "Nema događaja za prikaz"
  };
  return hr;
});