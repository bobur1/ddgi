"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.fi = factory()));
})(void 0, function () {
  'use strict';

  var fi = {
    code: "fi",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "Edellinen",
      next: "Seuraava",
      today: "Tänään",
      month: "Kuukausi",
      week: "Viikko",
      day: "Päivä",
      list: "Tapahtumat"
    },
    weekLabel: "Vk",
    allDayText: "Koko päivä",
    eventLimitText: "lisää",
    noEventsMessage: "Ei näytettäviä tapahtumia"
  };
  return fi;
});