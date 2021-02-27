"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.et = factory()));
})(void 0, function () {
  'use strict';

  var et = {
    code: "et",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "Eelnev",
      next: "Järgnev",
      today: "Täna",
      month: "Kuu",
      week: "Nädal",
      day: "Päev",
      list: "Päevakord"
    },
    weekLabel: "näd",
    allDayText: "Kogu päev",
    eventLimitText: function eventLimitText(n) {
      return "+ veel " + n;
    },
    noEventsMessage: "Kuvamiseks puuduvad sündmused"
  };
  return et;
});