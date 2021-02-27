"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.mk = factory()));
})(void 0, function () {
  'use strict';

  var mk = {
    code: "mk",
    buttonText: {
      prev: "претходно",
      next: "следно",
      today: "Денес",
      month: "Месец",
      week: "Недела",
      day: "Ден",
      list: "График"
    },
    weekLabel: "Сед",
    allDayText: "Цел ден",
    eventLimitText: function eventLimitText(n) {
      return "+повеќе " + n;
    },
    noEventsMessage: "Нема настани за прикажување"
  };
  return mk;
});