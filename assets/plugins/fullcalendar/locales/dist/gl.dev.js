"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.gl = factory()));
})(void 0, function () {
  'use strict';

  var gl = {
    code: "gl",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "Ant",
      next: "Seg",
      today: "Hoxe",
      month: "Mes",
      week: "Semana",
      day: "Día",
      list: "Axenda"
    },
    weekLabel: "Sm",
    allDayHtml: "Todo<br/>o día",
    eventLimitText: "máis",
    noEventsMessage: "Non hai eventos para amosar"
  };
  return gl;
});